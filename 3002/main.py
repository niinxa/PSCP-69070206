"""Cyan's password generator"""
def main():
    """Cyan's password generator"""
    name = input()
    surname = input()
    age = input()
    if len(name) >= 5 and len(surname) >= 5:
        x = name[:2] + surname[-1] + age[-1]
    else:
        x = name[0] + age + surname[-1]

    print(x)
main()
