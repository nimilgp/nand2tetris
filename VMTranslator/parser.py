#unpacks the asm file and removes all the white spaces and comments

def remove_whitelines(lineslist):#removes all empty lines
    forwardlist = []
    for line in lineslist:
        if line == "\n":
            continue    
        else:
            line = line[:-1]
            forwardlist.append(line.strip())
    return forwardlist

def remove_comments(lineslist):#removes all comments
    forwardlist = []
    for line in lineslist:
        templine = ""
        for element in line:
            if element == "/":
                break
            templine = templine + element
        if templine != "":
            forwardlist.append(templine.strip())
    return forwardlist

def seperate_into_parts(lineslist):#breaks into operator,memory segment,val
    forwardlist = []
    for line in lineslist:
        seperatedline = line.split()
        forwardlist.append(seperatedline)
    return forwardlist

def main(filename): #parses the file
    file = open(filename,"r")
    filelines = file.readlines()
    without_whitelines = remove_whitelines(filelines)
    without_whitelines_nor_comments = remove_comments(without_whitelines)
    lines_seperated_into_parts = seperate_into_parts(without_whitelines_nor_comments)
    return lines_seperated_into_parts
 
