#swaps out predefined symbols,labels and varaibles for memory locations

pre_def_symbols = {}

pre_def_symbols = {
    "SP": "0",
    "LCL": "1",
    "ARG": "2",
    "THIS": "3",
    "THAT": "4",
    "SCREEN": "16384",
    "KBD": "24576",
    }
for i in range(0,16):
  label = "R" + str(i)
  pre_def_symbols[label] = str(i)


var_and_lab = {}

def first_pass(parsedlist):
  pos = 0
  l = []
  for instruction in parsedlist:
    if instruction[0] == "(":
      var_and_lab[instruction[1:-1]] = str(pos)
    else:
      l.append(instruction)
      pos = pos + 1
  return l
    
def second_pass(templist):
  l = []
  var_lab_tracker = 16
  directly_allocated = []
  for instruction in templist:
    if instruction[0] == "@":
      if instruction[1:] in pre_def_symbols:
        l.append("@" + pre_def_symbols[instruction[1:]])
      elif instruction[1:] in var_and_lab:
        l.append("@" + var_and_lab[instruction[1:]])
      elif instruction[1:].isdigit():
        l.append(instruction)
        directly_allocated.append(int(instruction[1:]))
      else:
        while var_lab_tracker in directly_allocated:
          var_lab_tracker += 1
        l.append("@" + str(var_lab_tracker))
        var_and_lab[instruction[1:]] = str(var_lab_tracker)
        var_lab_tracker += 1
    else:
      l.append(instruction)
  return l


def main(parsedlist):
    templist = first_pass(parsedlist)
    forwardlist = second_pass(templist)
    return forwardlist














































