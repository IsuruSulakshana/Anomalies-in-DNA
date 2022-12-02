list = []
#Python code to convert string to list character-wise
def separateData(str):
    list1 = []
    list1[:0] = str
    return list1 
#Python code to move to data set list from text file
def convertData():
    file1 = open("lab.txt",'r')
    while(True):
        line = file1.readline()
        if not line:
            break
        list.append(separateData(line.strip()))
    file1.close()
    return list

convertData()

if __name__ == "__main__":
    convertData()



