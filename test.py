def comparisons(x, y):
    if (x > y):
        print (x, " is greater than", y)
        if (x < y):
            print (x, " is less than", y)
        else:
            print (x, " is not less than", y)
    else:
        print (x, " is not greater than", y)



while(True):
    x = int (input("Enter a number for x: "))
    y = int (input("Enter a number for y: "))
    comparisons(x,y)