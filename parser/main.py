
class ViewObj:

    def __init__(self,id,index,space):
        self.id = id
        self.index = index
        self.spaces = space
        self.children = []

def load_file(name):
    listOfViewObj = []
    lines = []
    file = open(name, "r",encoding="ISO-8859-1", errors='ignore')

    i = 0
    for line in file:

        if "DONE." in line:
            print("end of file")
            break

        #Spezieller Fall
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
        id = line.lstrip().split()[0].split("@")[1]  ## ID of View
        lineIndex += 1

        for char in line:
            if char.isspace() is False:
                print("ID: " + str(id) + " Spaces: " + str(spaces))
                listOfViewObj.append(ViewObj(id,lineIndex,spaces))
                spaces = 0
                break

            spaces += 1

    matchChilds(listOfViewObj)



    lines_splited = []
    #Split Eigenschaften
    for line in lines:
        lines_splited.append(line.split( ))


def matchChilds(objects):

    for i in range(len(objects)):
        if objects[i].spaces == 0:
            print("Root")
            continue

        print(str(objects[i].id) + " child from : " + str(getParent(objects, i, objects[i].spaces).id))
        getParent(objects, i, objects[i].spaces).children.append(objects[i])


def getParent(testlist, index, spaces):

    while True:
        if testlist[index].spaces == spaces-1:
            return testlist[index]
        else:
            index -= 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_file('test1.li')



