def main():
    dentro_intervalo = 0
    fora_intervalo = 0
    
    
    for i in range(10):
        valor = int(input("Digite um valor:"))
        
        if 10 <= valor <= 20: 
            dentro_intervalo += 1
            
        else:
            fora_intervalo += 1
            
            
    print("Valores dentro do intervalo [10,20]:", dentro_intervalo)
    print("Valores fora do intervalo [10, 20]:", fora_intervalo)
    

if __name__ == "__main__":
    main()
    