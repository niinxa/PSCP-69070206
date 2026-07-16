"""[LEARNING LOGS] Temperature"""
def main():
    """[LEARNING LOGS] Temperature"""
    t = float(input())
    text1 = input()
    text2 = input()

    k_c = t - 273.15
    f_c = (t - 32) / 1.8
    r_c = (t / 1.8) - 273.15

    if text1 == "K":
        if text2 == "C":
            print(k_c)
        elif text2 == "F":
            f = k_c * 1.8 + 32
            print(f)
        elif text2 == "R":
            r = (k_c + 273.15) * 1.8
            print(r)

    elif text1 == "F":
        if text2 == "C":
            print(f_c)
        elif text2 == "K":
            k = f_c + 273.15
            print(k)
        elif text2 == "R":
            r = (f_c + 273.15) * 1.8
            print(r)

    elif text1 == "R":
        if text2 == "C":
            print(r_c)
        elif text2 == "F":
            f = r_c * 1.8 + 32
            print(f)
        elif text2 == "K":
            k = r_c + 273.15
            print(k)

    elif text1 == "C":
        if text2 == "F":
            f = t * 1.8 + 32
            print(f)
        elif text2 == "K":
            k = t + 273.15
            print(k)
        elif text2 == "R":
            r = (t + 273.15) * 1.8
            print(r)
main()
