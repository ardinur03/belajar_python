def methodKu(number1 =10, number2 =20, number3 = 30):
    for x in range(number1, number2 + 1):
        if (x < number3):
            continue
        print(x)

def main():
    methodKu(1, 10, 5)

main()
