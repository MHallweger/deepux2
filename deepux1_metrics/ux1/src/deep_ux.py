import os
import subprocess
import argparse
import threading
import time
import json
import base64
import numpy
import datetime
from shutil import copy2
from distutils.dir_util import copy_tree

import traverser as tv
from traverser import Traverser
from metricscreator import MetricsCreator
from metricsevaluator import MetricsEvaluator
from recommendation import Recommendator

RUN_DROIDBOT = True
RICO_DATA_PATH = r"../data/combined"
MODULE_OUTPUT_PATH = r"../data"
DROIDBOT_OUTPUT_PATH = MODULE_OUTPUT_PATH + r"/droidbot_output"

## DEBUG CODE
subprocess.run("cls", shell=True)

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument("-is_emulator", action="store_true", dest="is_emulator", default=True,
                        help="Declare the target device to be an emulator, which would be treated specially by DroidBot.")
parser.add_argument("-grant_perm", action="store_true", dest="grant_perm", default=True,
                        help="Grant all permissions while installing. Useful for Android 6.0+.")
parser.add_argument("-keep_env", action="store_true", dest="keep_env",
                        help="Keep the test environment (eg. minicap and accessibility service) after testing.")
parser.add_argument("-a", action="store", dest="apk_path", required=True,
                        help="The file path to target APK")
# parser.add_argument("-a", action="store", dest="apk_path", required=False, default=r"./de.rki.coronawarnapp_1.9.1.apk",
#                         help="The file path to target APK")
parser.add_argument("-d", action="store", dest="device_serial", required=False,
                        help="The serial number of target device (use `adb devices` to find)")
parser.add_argument("-count", action="store", dest="count", default=tv.DEFAULT_EVENT_COUNT, type=int,
                        help="Number of events to generate in total. Default: %d" % tv.DEFAULT_EVENT_COUNT)
parser.add_argument("-interval", action="store", dest="interval", default=tv.DEFAULT_EVENT_INTERVAL,
                        type=int,
                        help="Interval in seconds between each two events. Default: %d" % tv.DEFAULT_EVENT_INTERVAL)
parser.add_argument("-timeout", action="store", dest="timeout", default=tv.DEFAULT_TIMEOUT, type=int,
                        help="Timeout in seconds, -1 means unlimited. Default: %d" % tv.DEFAULT_TIMEOUT)
args = parser.parse_args()

traverser = Traverser(is_emulator=args.is_emulator,
        grant_perm=args.grant_perm,
        keep_env=args.keep_env,
        apk_path=args.apk_path,
        device_serial=args.device_serial,
        count=args.count,
        interval=args.interval,
        timeout=args.timeout)

if not os.path.exists(MODULE_OUTPUT_PATH): os.makedirs(MODULE_OUTPUT_PATH)
if not os.path.exists(DROIDBOT_OUTPUT_PATH + r"/recommendations"): os.makedirs(DROIDBOT_OUTPUT_PATH + r"/recommendations")


def convert_numpy(o):
    """
    Fix numpy serialization error
    Source: https://stackoverflow.com/a/50577730
    """
    if isinstance(o, numpy.int32): return int(o)  
    raise TypeError

def copy_recom_images(metric_dict):
    if("recommendations" not in metric_dict): return
    recom_list = metric_dict["recommendations"]
    for image in recom_list:
        copy2(RICO_DATA_PATH + "/" + image, DROIDBOT_OUTPUT_PATH + r"/recommendations")



print("Starting...")
recommendator = Recommendator()

try:
    droidbot_thread = threading.Thread(target=traverser.run_droidbot)
    droidbot_thread.daemon = True
    if RUN_DROIDBOT: 
        droidbot_thread.start()

        while droidbot_thread.is_alive() and not os.path.exists(DROIDBOT_OUTPUT_PATH):
            time.sleep(0.5)

    if not os.path.exists(DROIDBOT_OUTPUT_PATH):
        print("ERROR: Droidbot output path '%s' does not exist!" % os.path.abspath(DROIDBOT_OUTPUT_PATH))
        exit()

    copy_tree("./dashboard_resources", DROIDBOT_OUTPUT_PATH)
    evaluation_json = []

    while True:
        print("Checking for new images")
        new_filepaths = traverser.cleanup_output()

        for filepath in new_filepaths:
            print("Start processing image %s" % os.path.basename(filepath))
            with open(filepath, "rb") as f:
                image_base64 = base64.b64encode(f.read()).decode("utf-8")

            start_time = time.time()
            metrics, execution_times = MetricsCreator.getMetrics(image_base64)
            evaluations = MetricsEvaluator.getEvaluations(metrics)
            eval_w_recommendations = recommendator.getRecommendations(evaluations)

            for metric_name in eval_w_recommendations:
                metric_dict = eval_w_recommendations[metric_name]
                if "value" not in metric_dict:
                    for sub_metric in metric_dict: copy_recom_images(metric_dict[sub_metric])
                else:
                    copy_recom_images(metric_dict)


            grouped_evaluations = {"image": os.path.basename(filepath), "evaluations": eval_w_recommendations, "execution_times": execution_times}
            evaluation_json.append(grouped_evaluations)
                
            eval_json = json.dumps(evaluation_json, indent=4, default=convert_numpy)
            with open(MODULE_OUTPUT_PATH + r"/evaluations.json", "w") as file:
                file.write(eval_json)

            with open(DROIDBOT_OUTPUT_PATH + r"/evaluations.js", "w") as file:
                file.write("var evaluations = \n")
                file.write(eval_json)

            print("Done image %s in %s" % (os.path.basename(filepath), datetime.timedelta(seconds=time.time() - start_time)))

        if not RUN_DROIDBOT: break
        if not droidbot_thread.is_alive() and not new_filepaths: break
        if not new_filepaths and RUN_DROIDBOT:
            time.sleep(5)

    print("Execution done")
except (KeyboardInterrupt, SystemExit):
    exit()
