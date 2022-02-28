
def swapping(x,y):




    x = x * y
    y = x / y
    x = x / y


    if y > x:
        print("Older person y =", y)
        print("younger person x =", x)

    else:
        print("Older person x =", x)
        print("younger person y =", y)

swapping(100,50)