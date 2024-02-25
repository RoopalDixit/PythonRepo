a=[[]]
with open('/Users/roopaldixit/Documents/Inputs/Euler11.txt', 'r') as file:
     
         for i in range(0,20):
                 b=[int(x) for x in file.read(60).split()]

                 a.append(b)
            
print(a)
                





    





    






