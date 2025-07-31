while True:

    b = input("Enter Marks or 'Exit' To Exit:")
    
    if b.lower() == "exit":
        print("EXITED WITH SUCCESS")
        break
    try:
        a = int(b)
        if a<0:
            print("Invalid Input")        
        elif a<=40:
            print("GRADE-F")        
        elif a<=59:
            print("GRADE-D")        
        elif a<=74:
            print("GRADE-C")        
        elif a<=89:
            print("GRADE-B")        
        elif a<=100:
            print("GRADE-A")        
        else:
            print("Invalid No Input")
    except ValueError:
        print("Enter marks not a string")