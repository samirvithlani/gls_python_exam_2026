choice = input("enter season ")

match choice:
    case "summer":
        print("summer season")
    #no break
    case "winter":
        print("winter season..")    
        print("find your sw...")
    case "monsoon":
        print("monsoon season")    
    case _:
        print("invalid choice..")    
        