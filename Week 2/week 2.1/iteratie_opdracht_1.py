omgedraaide_lijst = [1,8,5,4,2]
print("Lijst gedraaid : ",omgedraaide_lijst)
reversed_list = []
for nummer in omgedraaide_lijst:
  reversed_list = [nummer] + reversed_list
print("Lijst niet gedraaid : ", reversed_list)