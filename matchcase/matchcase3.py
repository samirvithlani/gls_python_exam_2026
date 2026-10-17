choice = input(f"press y for continue press n for exit")

match choice:
    case "y" | "Y" | "YES":
        print("coninueing...")
    case "n" | "N" | "NO":
        print("exit..")
        