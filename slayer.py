print("Guess a six digit number SLAYER so that following equation is true where each letter stands for the digit in the position shown:")
print()
print("SLAYER + SLAYER + SLAYER = LAYERS\n\n")


def slayer():
    while True:
        slayer = input("Enter your guess for SLAYER: ")
        if len(slayer) != 6:
            print('SLAYER must be a 6-digit number.')
            break
        slayer = int(slayer)
        r = slayer % 10
        e = (slayer // 10) % 10
        y = (slayer // 10 // 10) % 10
        a = (slayer // 10 // 10 // 10) % 10
        l = (slayer // 10 // 10 // 10 // 10) % 10
        s = (slayer // 10 // 10 // 10 // 10 // 10) % 10
        layers = int("%s%s%s%s%s%s" % (l, a, y, e, r, s))
        if slayer + slayer + slayer == layers:
            print("Your guess is correct:")
            print("SLAYER + SLAYER + SLAYER =", layers)
            print("LAYERS =", layers)
            print("Thanks for playing.")
            break
        else:
            print("Your guess is incorrect:")
            print("SLAYER + SLAYER + SLAYER =", layers)
            print("LAYERS =", layers)
            print("Thanks for playing.")
            break

slayer()
