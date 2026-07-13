"""[LEARNING LOGS] Season"""
def main():
    """[LEARNING LOGS] Season"""
    month = int(input())
    day = int(input())

    if month in (1,2,3):
        if month % 3 == 0 and day == 21:
            print("spring")
        else:
            print("winter")
    elif month in (4,5,6):
        if month % 6 == 0 and day == 21:
            print("summer")
        else:
            print("spring")
    elif month in (7,8,9):
        if month % 9 == 0 and day == 21:
            print("fall")
        else:
            print("summer")
    elif month in (10,11,12):
        if month % 12 == 0 and day == 21:
            print("winter")
        else:
            print("fall")

main()
