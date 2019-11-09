print("Hello World")
seter = int(input("Press 1 for addition ; Press 2 for multiplication ; Press 3 for deduction\n"  ))
if seter >= 4:
    print ("Error")
else:
    jes = float(input("Give me your two numbers \n "))
    jus = float(input("The other \n "))
    if seter == 1:
        juse = int(jes + jus)
        if (juse) == 9:
            print ("The oracle has said that thou shall pass")
        if (juse) == 6:
            print ("You're a DEMON!!!")
        else:
            print("The oracle has said that thou shant pass")
    elif seter == 2:
        juse = int(jes * jus)
        if (juse) == 9:
            print("The oracle has said that thou shall pass")
        elif (juse) == 6:
            print("You're a DEMON!!!")
        else:
            print("The oracle has said that thou shant pass")
    elif seter == 3:
        juse = int(jes - jus)
        if (juse) == 9:
            print("The oracle has said that thou shall pass")
        elif (juse) == 6:
            print("You're a DEMON!!!")
        else:
            print("The oracle has said that thou shant pass")