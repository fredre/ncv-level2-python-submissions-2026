while True:
    valid = False
    mark_in = (input("mark (-1 ends): "))
    if mark_in == "-1":
        break
    elif mark_in.isdigit():
        mark = int(mark_in)
        if 0 <= mark <= 39:
            print("not achieved")
            valid = True

        if 40 <= mark <= 49:
            print("not yet competent")
            valid = True
        
        if 50 <= mark <= 59:
            print("competent")
            valid = True
        
        if 70 <= mark <= 79:
            print("highly competent")
            valid = True
        
        if 80 <= mark <= 100:
            print("Outstanding")
            valid = True
        
        if valid == False:
            print("invalid entry")
    else:
        print("enter numbers only")
