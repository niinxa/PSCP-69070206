"""Elo"""
def main():
    """Elo"""
    ra = int(input())
    rb = int(input())
    player = input()

    ea = 1 / (1 + 10**((rb - ra) / 400))
    eb = 1 / (1 + 10**((ra - rb) / 400))

    if player == "A":
        print(f"{ea:.2f}")
    elif player == "B":
        print(f"{eb:.2f}")
main()
