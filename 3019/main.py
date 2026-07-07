"""Safe Password"""
def main():
    """safe Password"""
    char = input()
    digits = int(input())
    password = "H 4567"
    if char in password and str(digits) in password:
        print("safe unlocked")
    elif char in password:
        print("safe locked - change digit")
    elif str(digits) in password:
        print("safe locked - change char")
    else:
        print("safe locked")
main()
