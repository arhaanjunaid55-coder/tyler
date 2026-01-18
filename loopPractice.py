# input1 = int(input("enter something"))
while (input1 != -1):
    print("you entered", input1)
    input1 = int(input("enter something"))
    
# print("loop exited")

# ranged for loop
x = [4, 6, 3, 7]
  # [0, 1, 2, 3]

# for each loop
for i in range(4):
    print(f"index: {i}, element: {x[i]}")
    
for i in x:
    print(i)