import json

class ViewObj:

    def __init__(self, id,resourceId, index, space,android_class,layout_height,layout_width,location_on_screen_x,location_on_screen_y,visibility):
        self.id = id
        self.resourceId = resourceId
        self.index = index
        self.spaces = space
        self.visible_to_user = visibility
        self.android_class = android_class
        self.layout_height = layout_height
        self.layout_width = layout_width
        self.location_on_screen_x = location_on_screen_x
        self.location_on_screen_y = location_on_screen_y
        self.bounds = [location_on_screen_x,location_on_screen_y,layout_width,layout_height]
        self.children = []



def load_file(name):
    listOfViewObj = []
    lines = []
    file = open(name, "r", encoding="ISO-8859-1", errors='ignore')

    i = 0
    for line in file:

        if "DONE." in line:
            print("end of file")
            break

        # Spezieller Fall
        if i == 0 and "}" in line:
            indexOfBracket = line.index('}') + 1
            lineLength = len(line)
            lines.append(line[indexOfBracket:lineLength])
            continue

        lines.append(line)
        i += 1
    file.close()

    lineIndex = 0
    spaces = 0
    for line in lines:

        line = clearString(line)
        id = line.lstrip().split()[0].split("@")[1]  ## ID of View
        android_class = line.lstrip().split()[0].split("@")[0]
        layout_height = -1
        layout_width = -1
        getLocationOnScreen_x = -1
        getLocationOnScreen_y = -1
        getVisibility = False
        resourceId = -1
        for attributes in line.lstrip().split():
            if 'getHeight' in attributes:
                layout_height = attributes.split("=")[1].split(",")[1]
            elif 'getWidth' in attributes:
                layout_width = attributes.split("=")[1].split(",")[1]
            elif 'getLocationOnScreen_x' in attributes:
                getLocationOnScreen_x = attributes.split("=")[1].split(",")[1]
            elif 'getLocationOnScreen_y' in attributes:
                getLocationOnScreen_y = attributes.split("=")[1].split(",")[1]
            elif 'getVisibility' in attributes:
                getVisibility = attributes.split("=")[1].split(",")[1]
                if getVisibility == 'VISIBLE':
                    getVisibility = True
                else:
                    getVisibility = False
            elif 'mID' in attributes:
                resourceId = attributes.split("=")[1].split(",")[1]




        print(android_class)
        lineIndex += 1

        for char in line:
            if char.isspace() is False:
                print("ID: " + str(id) + " Spaces: " + str(spaces))
                listOfViewObj.append(ViewObj(id,
                                             resourceId,
                                             lineIndex,
                                             spaces,
                                             android_class,
                                             layout_height,
                                             layout_width,
                                             getLocationOnScreen_x,
                                             getLocationOnScreen_y,
                                             getVisibility))
                spaces = 0
                break

            spaces += 1

    listOfViewObj = matchChildren(listOfViewObj)

    toJson(listOfViewObj)

def toJson(listOfViewObj):
    jsonStr = json.dumps(listOfViewObj[0].__dict__)

    jsonStr = jsonStr.replace("visible_to_user","visible-to-user")
    jsonStr = jsonStr.replace("android_class","class")
    print(jsonStr)

def matchChildren(objects):
    for i in range(len(objects)):
        if objects[i].spaces == 0:
            print("Root")
            continue

        parent = getParent(objects, i, objects[i].spaces)
        print(str(objects[i].id) + " child from : " + str(parent.id))
        parent.children.append(objects[i].__dict__)

    return objects

def getParent(objects, index, spaces):
    while True:
        if objects[index].spaces == spaces - 1:
            return objects[index]
        else:
            index -= 1


def clearString(string):
    # clean String
    string = string.replace('\x00', '')
    string = string.replace('\0', '')
    string = string.replace('\0', '')
    string = string.replace('z\4', '')
    string = string.replace('x', '')
    string = string.replace('4', '')
    string = string.replace('', '')
    string = string.replace('', '')

    return string

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_file('test7.li')
