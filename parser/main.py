import json

class ViewObj:

    def __init__(self, id, index, space):
        self.id = id
        self.index = index
        self.spaces = space
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
        # clean String
        line = line.replace('\x00', '')
        line = line.replace('\0', '')
        line = line.replace('\0', '')
        line = line.replace('z\4', '')

        id = line.lstrip().split()[0].split("@")[1]  ## ID of View
        lineIndex += 1

        for char in line:
            if char.isspace() is False:
                print("ID: " + str(id) + " Spaces: " + str(spaces))
                listOfViewObj.append(ViewObj(id, lineIndex, spaces))
                spaces = 0
                break

            spaces += 1

    listOfViewObj = matchChildren(listOfViewObj)
    jsonStr = json.dumps(listOfViewObj[0].__dict__)
    print(jsonStr)

    lines_splited = []
    # Split Eigenschaften
    for line in lines:
        lines_splited.append(line.split())


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_file('test1.li')
