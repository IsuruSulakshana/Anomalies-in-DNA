def includeData(a,b):
    list = ["Changes:"+str(a)+'\n',"Adding:"+str(b)]
    file1 = open("report.txt",'w')
    file1.writelines(list)
    file1.close()

    file1 = open("report.txt","r")
    while(True):
        line = file1.readline()
        if not line:
            break
        print(line.strip())
    file1.close()

if __name__ == "__main__":
    includeData()