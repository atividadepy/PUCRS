def main():
    X = int(input("Digite o valor de X: "))

    for i in range(1, 21):
        termo = X ** i
        print(termo, end=" ")

if __name__ == "__main__":
    main()