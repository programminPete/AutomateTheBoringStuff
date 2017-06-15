tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


			 
def printTable(Data):
	colWidths = [0] * len(Data)
	# Find length of longest string in each inner list
	for i in range(len(Data)):
		colWidths[i] = len(max(Data[i], key=len))

	# Set the right justified to 1 greater than that length.
	col = 0
	row = 0
	index = 0
	for row in range(len(Data)):
		for col in range(len(Data[row])):
			#print(Data[0][col].rjust(colWidths[0]),Data[1][col].rjust(colWidths[1]),Data[2][col].rjust(colWidths[2]))
			#print(Data[row][col].rjust(colWidths[row]),end=' ')
			
			# added this 3rd for loop level and break statement since previous two print
			# statements were just slightly off.
			for index in range(len(Data)):
				print(Data[index][col].rjust(colWidths[index]),end=' ')	
			print()
		break

printTable(tableData)