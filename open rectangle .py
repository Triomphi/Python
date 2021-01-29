height = int(input('enter the height '))
breadth = int(input('enter the breadth '))

print('*'*breadth)
for i in range(height-2):
	print('*', ' '*(breadth-4), '*')
print('*'*breadth)
