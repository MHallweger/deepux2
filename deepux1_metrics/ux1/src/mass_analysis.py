import os
import csv
import subprocess
import collections
import base64
import datetime
import time
import re
import json
from multiprocessing import Pool, current_process

from metricscreator import MetricsCreator
from metricsevaluator import MetricsEvaluator

DATA_PATH = r"../data/combined"
NUM_WORKER_THREADS = 4
CHECKPOINT_AFTER_N_FILES = 64
START_INDEX = 0

def analyse_image(filename):
    print("[%s] %s: Processing %s" % (datetime.datetime.now().strftime("%H:%M:%S"), current_process().name, filename))
    path_pic = os.path.join(DATA_PATH, filename)

    with open(path_pic, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    metrics, exec_times = MetricsCreator.getMetrics(image_base64)
    evaluations = MetricsEvaluator.getEvaluations(metrics)

    output_dict = {}
    output_dict["image"] = os.path.basename(filename)

    with open(path_pic.replace(".jpg",".json").replace(".png",".json")) as json_file:
        data = json.load(json_file)
        output_dict["package_name"] = data["activity_name"].split("/")[0]

    output_dict.update(flatten(evaluations))
    output_dict.update(exec_times)

    return output_dict

def flatten(d, parent_key='', sep='_'):
    """
    Source: https://stackoverflow.com/a/6027615
    """
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sorted_nicely(list): 
    """
    Sort the given iterable in the way that humans expect.
    Source: https://stackoverflow.com/a/2669120
    """ 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(list, key = alphanum_key)

def sorted_nicely_dict(list, dict_key): 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key[dict_key]) ] 
    return sorted(list, key = alphanum_key)


if __name__ == '__main__': 
    start_time = time.time()

    if not os.path.exists(DATA_PATH): 
        print("Path does not exist!")
        exit()

    try:
        evaluation_csv = []
        print("Reading filelist")
        file_list = [filename for filename in os.listdir(DATA_PATH) if filename.endswith(".png") or filename.endswith(".jpg")]
        file_list = sorted_nicely(file_list)
        file_list = file_list[START_INDEX:]
        #file_list = file_list[:16]

        chunked_list = [file_list[i:i + CHECKPOINT_AFTER_N_FILES] for i in range(0, len(file_list), CHECKPOINT_AFTER_N_FILES)]
        len_cunked = len(chunked_list)
        for idx, sub_file_list in enumerate(chunked_list):
            print("###")
            print("Start distributing sub file list %s/%s with file %s to %s" % (idx+1, len_cunked, sub_file_list[0], sub_file_list[-1]))
            with Pool(NUM_WORKER_THREADS) as p:
                result = p.map(analyse_image, sub_file_list)
                evaluation_csv.extend(result)

            evaluation_csv = sorted_nicely_dict(evaluation_csv, "image") 
            print("Writing evaluations to file. (Time so far: %s)" % datetime.timedelta(seconds=time.time() - start_time))
            with open(r"../data/mass_evaluations.csv", 'w', newline='') as csv_file:
                dict_writer = csv.DictWriter(csv_file, evaluation_csv[0].keys())
                dict_writer.writeheader()
                dict_writer.writerows(evaluation_csv)


        print("All work completed (%sx images)" % len(evaluation_csv))
        print("--- %s seconds ---" % datetime.timedelta(seconds=time.time() - start_time))
    except (KeyboardInterrupt, SystemExit):
        exit()
