
popul = int(input("Type the population in our universe: "))
if popul % 2 == 0:
    surviv = popul // 2
else:
    surviv = (popul + 1) // 2

print(surviv)