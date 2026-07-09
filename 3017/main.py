"""[LEARNING LOGS] Bill"""
def main():
    """[LEARNING LOGS] Bill"""
    cost = int(input())
    service = (10 / 100) * cost
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    vat = (7 / 100) * (cost + service)
    total = cost + service + vat
    print(f"{total:.2f}")
main()
