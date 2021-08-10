import os
import shutil
import json
import re
import subprocess
import droidbot as dbot
from droidbot import input_policy

DEFAULT_EVENT_INTERVAL = 1
DEFAULT_EVENT_COUNT = 300
DEFAULT_TIMEOUT = -1

DROIDBOT_OUTPUT_PATH = r"../data/droidbot_output"
DROIDBOT_STATES_PATH = DROIDBOT_OUTPUT_PATH + r"/states"
MODULE_OUTPUT_PATH = r"../data/screenshots"


class Traverser:

    def __init__(self,
        is_emulator=True,
        grant_perm=True,
        keep_env=False,
        apk_path=None,
        device_serial=None,
        count=DEFAULT_EVENT_COUNT,
        interval=DEFAULT_EVENT_INTERVAL,
        timeout=DEFAULT_TIMEOUT
    ):

        # Check if APK given
        if not apk_path or not os.path.exists(apk_path):
            print("APK does not exist.")
            return

        # Make apk path absolute
        apk_path = os.path.abspath(apk_path)

        # Move working dir if not in module directory
        if os.path.dirname(os.path.abspath(__file__)).lower() != os.path.abspath(os.getcwd()).lower():
            os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # Delete old outputs
        if os.path.exists(MODULE_OUTPUT_PATH): shutil.rmtree(MODULE_OUTPUT_PATH)

        # Create output folders
        if not os.path.exists(DROIDBOT_OUTPUT_PATH): os.makedirs(DROIDBOT_OUTPUT_PATH)
        if not os.path.exists(MODULE_OUTPUT_PATH): os.makedirs(MODULE_OUTPUT_PATH)


        # Fire up droidbot to traverse the app and take some screenshots
        self.droidbot = dbot.DroidBot(
            app_path=apk_path,
            device_serial=device_serial,
            is_emulator=is_emulator,
            output_dir=DROIDBOT_OUTPUT_PATH,
            keep_env=keep_env,
            grant_perm=grant_perm,
            event_count=count,
            event_interval=interval,
            timeout=timeout,
            policy_name=input_policy.POLICY_GREEDY_DFS
        )

        #Get package name from manifest
        manifest_dump = subprocess.check_output("aapt dump badging " + apk_path).decode('utf-8')
        self.app_package_name = re.split("package: name='(.*?)'", manifest_dump)[1]

        self.cleaned_filenames = []


    def run_droidbot(self):
        self.droidbot.start()


    def cleanup_output(self):
        # Clean up droidbot output (e.g. sort out screenshots of other packages)
        new_filepaths = []
        if not os.path.exists(DROIDBOT_STATES_PATH): return []
        
        for filename in os.listdir(DROIDBOT_STATES_PATH):
            if not filename.endswith(".png") and not filename.endswith(".jpg"): continue
            if filename in self.cleaned_filenames: continue

            path_pic = os.path.join(DROIDBOT_STATES_PATH, filename)
            path_state = os.path.join(DROIDBOT_STATES_PATH, filename.replace("screen_","state_").replace(".png",".json"))
        
            #print(path_pic)

            with open(path_state) as state_file:    
                data = json.load(state_file)

            if self.app_package_name in data["foreground_activity"]:
                shutil.copy2(path_pic, MODULE_OUTPUT_PATH)
                self.cleaned_filenames.append(filename)
                new_filepaths.append(path_pic)

        return new_filepaths
