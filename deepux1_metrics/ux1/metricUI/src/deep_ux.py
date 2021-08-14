import os
import subprocess
import argparse
import threading
import time
import json
import base64

import traverser as tv
from traverser import Traverser
from metricscreator import MetricsCreator
from metricsevaluator import MetricsEvaluator


MODULE_OUTPUT_PATH = r"./data"

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
# parser.add_argument("-a", action="store", dest="apk_path", required=True,
#                         help="The file path to target APK")
parser.add_argument("-a", action="store", dest="apk_path", required=False, default=r"./de.rki.coronawarnapp_1.9.1.apk",
                        help="The file path to target APK")
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

if not os.path.exists(MODULE_OUTPUT_PATH): os.makedirs(MODULE_OUTPUT_PATH)
MODULE_OUTPUT_PATH = os.path.abspath(MODULE_OUTPUT_PATH)

traverser = Traverser(is_emulator=args.is_emulator,
        grant_perm=args.grant_perm,
        keep_env=args.keep_env,
        apk_path=args.apk_path,
        device_serial=args.device_serial,
        count=args.count,
        interval=args.interval,
        timeout=args.timeout)


print("Starting...")
try:
    droidbot_thread = threading.Thread(target=traverser.run_droidbot)
    droidbot_thread.daemon = True
    droidbot_thread.start()

    evaluation_json = []

    #while droidbot_thread.is_alive():
        #time.sleep(5)
    print("Checking for new images")
    new_filepaths = traverser.cleanup_output()

    for filepath in new_filepaths:
        print("Process image %s" % os.path.basename(filepath))
        with open(filepath, "rb") as f:
            image_base64 = base64.b64encode(f.read()).decode("utf-8")

        metrics = MetricsCreator.getMetrics(image_base64)
        evaluations = MetricsEvaluator.getEvaluations(metrics)
        grouped_evaluations = {"image": os.path.basename(filepath), "evaluations": evaluations}
        evaluation_json.append(grouped_evaluations)
            
    with open(MODULE_OUTPUT_PATH + r"/evaluations.json", "w") as file:
        file.write(json.dumps(evaluation_json, indent=4))
            

    print("Execution done")
except (KeyboardInterrupt, SystemExit):
    exit()
