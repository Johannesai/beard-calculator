def main():

    beard = input("How long do you want to save your beard in month?: ")
    days = float(beard) * 1.25
    print(days)
    restart = input("Do you want to start again?  ").lower()
    if restart == "yes":
        main()

    else:
        exit()

main()
