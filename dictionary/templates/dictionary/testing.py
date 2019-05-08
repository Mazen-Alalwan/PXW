while True:
    height = input("are you tall?\n")
    gender = input("what's you gender\n")
    if height == "yes":
        height = "tall"
    elif height == "stop" or gender == "stop":
        break

    else:
        height = "short"
    print(" You're a " + gender + " and your " + height)
