A = input()
B = input()

A = int(A)

three = A * int(B[2])
four = A * int(B[1])
five = A * int(B[0])
six = three + four * 10 + five * 100

print(three, four, five, six, sep='\n')
