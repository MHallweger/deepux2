import base64
import re
import os
import time
import argparse
import xml.etree.ElementTree as ET
from xml.dom import minidom
from pprint import pprint
from subprocess import check_output
from subprocess import run

run("cls", shell=True)

# Arguments disabled for easier testing
# parser = argparse.ArgumentParser()
# parser.add_argument('apk_path', help="Path to the .apk file")
# parser.add_argument('-o', '--output', help="Path to the output location")
# args = parser.parse_args()

# apk_path = args.apk_path
# output = args.output

apk_path = ".\\de.rki.coronawarnapp_1.9.1.apk"
output = ".\\app_traverser\\output"
if not os.path.exists(output): os.makedirs(output)


# Functions
def take_screenshot(file_path):
    screenshot64 = check_output('adb exec-out "screencap -p | base64"')
    with open(file_path, "wb") as fh:
        fh.write(base64.decodebytes(screenshot64))

def get_current_activity():
    activities = check_output('adb shell dumpsys activity activities | findStr "mCurrentFocus"', shell=True).decode('utf-8')
    if "mCurrentFocus=null" in activities: return None
    
    return (re.split("%s/(.*?)}" % app_package_name, activities)[1]).replace(app_package_name + ".", "")

def hierarchy_dump(file_path=None):
    hierarchy_dump = check_output("adb exec-out uiautomator dump /dev/tty").decode('utf-8')
    hierarchy_dump = hierarchy_dump.replace("UI hierchary dumped to: /dev/tty", "")
    xml = ET.fromstring(hierarchy_dump)

    if file_path is not None:
        xmlstr = minidom.parseString(hierarchy_dump).toprettyxml(indent="\t")
        with open(file_path, "wb") as fh:
            fh.write(xmlstr.encode('utf-8'))  

    return xml
    

#Get package name and start activity from manifest
manifest_dump = check_output("aapt dump badging " + apk_path).decode('utf-8')

app_package_name = re.split("package: name='(.*?)'", manifest_dump)[1]
launch_activity = re.split("launchable-activity: name='(.*?)'", manifest_dump)[1]


# Install and Start
run("adb install -g" + apk_path)
run("adb shell am start -W -n '%s/%s'" % (app_package_name, launch_activity))


# Wait for the activity to come up
print("Waiting for the app to come up...")
must_end = time.time() + 10
while time.time() < must_end:
    if get_current_activity() is not None: break
    time.sleep(1)
if get_current_activity() is None: raise Exception("App did not started in time!")
print("Complete")


# hierarchy = hierarchy_dump()
# for btn in hierarchy.findall(".//node[@class='android.widget.Button']"):
#     bounds_str = btn.attrib['bounds'].replace("["," ").replace("]"," ").replace(","," ")

#     bounds = list( map( int, bounds_str.split() ) )
#     bounds = [(bounds[0], bounds[1]), (bounds[2], bounds[3])]
#     print(bounds)

    #bounds = btn.attrib['bounds'].split("][",1)
    #bounds = [x.replace("[","").replace("]","") for x in bounds]
    
    
    #pprint(btn.attrib['bounds'])
    #pprint(bounds)

    #adb shell input tap 63 1626

#hierarchy_dump("%s\\%s.xml" % (output, "screen2"))
#print(get_current_activity())

# Monkey the ui
# visited_activities = []
# for i in range(5):
#     cur_activity = get_current_activity()
#     if cur_activity not in visited_activities:
#         take_screenshot("%s\\%s.png" % (output, cur_activity))
#         hierarchy_dump("%s\\%s.xml" % (output, cur_activity))
#         visited_activities.append(cur_activity)

#     #run("adb shell monkey -p %s --pct-syskeys 0 1" % app_package_name)
#     #time.sleep(1)

# pprint(visited_activities)



