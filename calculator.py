digits = "0 1 2 3 4 5 6 7 8 9 .".split()
ops = "+ - * /".split()
currentNums=[""]
currentOps=[]
question=input("Enter math expression: ")
counter=0
opCounter=0
for char in question:
  if char in digits: currentNums[counter]+=char
  elif char in ops: 
    currentOps.append("")
    currentOps[opCounter]+=char
    opCounter+=1
    counter+=1
    currentNums.append("")
total=float(currentNums[0])
for i in range(len(currentOps)):
  if currentOps[i] == "+":
    total+=float(currentNums[i+1])
  elif currentOps[i] == "-":
    total-=float(currentNums[i+1])
  elif currentOps[i] == "*":
    total*=float(currentNums[i+1])
  elif currentOps[i] == "/":
    total/=float(currentNums[i+1])
print(total)
