rows = int(input("Enter number of rows: "))

ascii_value = 97

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print()

# chr(65-90) ------- A-Z
# chr(97-122) ------- a-z