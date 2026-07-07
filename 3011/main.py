"""[LEARNING LOGS] Colors"""
def main():
    """[LEARNING LOGS] Colors"""
    color1 = input()
    color2 = input()
    if (color1 == "Red" or color1 == "Yellow" or color1 == "Blue") and (color2 == "Red" or color2 == "Yellow" or color2 == "Blue"):
        if (color1 == "Red" or color1 == "Yellow") and (color2 == "Yellow" or color2 == "Red"):
            print("Orange")
        elif (color1 == "Red" or color1 == "Blue") and (color2 == "Blue" or color2 == "Red"):
            print("Violet")
        elif (color1 == "Yellow" or color1 == "Blue") and (color2 == "Blue" or color2 == "Yellow"):
            print("Green")
    else:
        print("Error")
main()
