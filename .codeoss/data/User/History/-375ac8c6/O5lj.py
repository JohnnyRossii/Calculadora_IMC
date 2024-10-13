def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros (utilize ponto ao inves de virgula): "))
        
        imc = calcular_imc(peso, altura)
        
        print(f"Seu IMC é: {imc:.2f}")
        
        if imc < 18.5:
            print("Você está abaixo do peso.")
        elif 18.5 <= imc < 24.9:
            print("Você está com peso normal.")
        elif 25 <= imc < 29.9:
            print("Você está com sobrepeso.")
        else:
            print("Você está com obesidade.")
    
    except ValueError:
        print("Insira valores numéricos válidos para peso e altura.")

if __name__ == "__main__":
    main()