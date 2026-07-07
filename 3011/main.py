"""[LEARNING LOGS] Colors"""
def main():
    """[LEARNING LOGS] Colors"""
    color1 = input().lower()
    color2 = input().lower()
    if color1 in ('red', 'yellow') and color2 in ('red', 'yellow'):
        print("Orange")
    elif color1 in ('red', 'blue') and color2 in ('red', 'blue'):
        print("Violet")
    elif color1 in ('blue', 'yellow') and color2 in ('blue', 'yellow'):
        print("Green")
    else:
        print("Error")
main()
