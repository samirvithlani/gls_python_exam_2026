choice = int(input(f"press 1 for add \n press 2 for sub"))

match choice:
    case 1:
        print("add called...")
    case 2:
        print("sub called...")    
    case _:
        print("invalid choice..")    
        