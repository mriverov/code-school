numbers = [3,8,1,5,4,-1, 89] #[1,3,5,8]

currentMin = numbers[0] # currentMin=3
ordered = []  #ordered= []

for current in numbers:  #current = 3
   if(current <= currentMin): # current <= 3
     ordered.insert(0,current)
     print("estado lista current " + str(ordered))
     currentMin = current
   else:
     print("caso else with current " + str(current))
     cont = 0
     for currentInOrdered in ordered: #[1,3,5,8]
       if(current > currentInOrdered):
        cont = cont + 1
     ordered.insert(cont, current)  
     

print(str(ordered))
