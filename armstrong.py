number = raw_input("enter a number: ")
order = len(number)
armStrong = 0

for i in number :
    armStrong += int(i)** order
    
if number == str(armStrong):
    print str(armStrong) + " is an armstrong number"

else:
    print str(armStrong) + " is not an armstrong number"

