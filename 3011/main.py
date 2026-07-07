"""[LEARNING LOGS] Colors"""
def main():
    """[LEARNING LOGS] Colors"""
    color1 = input()
    color2 = input()
    if color1 in ('Red', 'Yellow') and color2 in ('Red', 'Yellow'):
        print("Orange")
    elif color1 in ('Red', 'Blue') and color2 in ('Red', 'Blue'):
        print("Violet")
    elif color1 in ('Blue', 'Yellow') and color2 in ('Blue', 'Yellow'):
        print("Green")
    else:
        print("Error")
main()
