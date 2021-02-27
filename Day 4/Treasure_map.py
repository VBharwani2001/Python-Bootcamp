row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Please enter where you want to put the treasre?:   ")
column = int(position[0])-1
row = int(position[1])-1
map[row][column] = "X"
print(f"{row1}\n{row2}\n{row3}\n")
