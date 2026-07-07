"""Pro"""
def main():
    """Pro"""
    a = int(input())
    b = int(input())
    money = int(input())
    people = int(input())
    pro = b * money
    if people % a == 0:
        x = (people // a) * pro
        print(x)
    else:
        x = ((people // a) * pro) + (people % a) * money
        print(x)
main()
