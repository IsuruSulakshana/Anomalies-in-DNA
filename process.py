#Import input file & output file
import input
import output
#Call function in input file
input = input.convertData()
#Assign retirement variables
list = []
a = input[0]
b = input[1]
#Python code to count differences between a & b
def difference(x,y):
    size = len(x)
    if size == 0:
        return list
    else:
        if x[0] != y[0]:
            if x[0] == y[1]:
                y = y[1:]
            else:
                list.append(1)
        difference(x[1:],y[1:])
difference(a,b)
#Count changes
changes = len(list)
#Count adding
adding = len(b)-len(a) 
#Call function in output file
output.includeData(changes,adding)

