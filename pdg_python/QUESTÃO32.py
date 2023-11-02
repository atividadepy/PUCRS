def main():
    for i in range(5):
        a = int(input("Digite o valor de a (inteiro e positivo): "))
        b = int(input("Digite o valor de b (inteiro e positivo, maior que a): "))
        
        
        if a < b:
            print("Número pares no interval de", a, "a", b, "são:")
            for num in range(a, b + 1):
                if num % 2 == 0:
                    print(num)
        
        
        
        else:
            print("O valor de b deve ser maior que a.")
            
            
if  __name__ == "__main__":
    
    main()
    
        
