tipo_investimento = int(input("Digite o tipo de investimento\n 1. CDB\n 2. LCI\n 3. LCA\n Insira o desejado: "))

valor_resgate = float(input("Digite o valor a ser resgatado: R$"))
quantidade_dias = int(input("Digite o número de dias que o valor permaneceu investido: "))


if tipo_investimento == 1:
    if quantidade_dias <= 180:
        aliquota = 0.225
    elif quantidade_dias >= 181 and quantidade_dias <= 360:
        aliquota = 0.20
    elif quantidade_dias >= 361 and quantidade_dias <= 720:
        aliquota = 0.175
    else:
        aliquota = 0.15
    
    valor_imposto = valor_resgate * aliquota
    print(f"O valor do imposto de renda a ser pago é: R${valor_imposto:.2f} ")
        
elif tipo_investimento == 2:
    aliquota = 0
    valor_imposto = valor_resgate * aliquota
    print(f"O valor do imposto de renda a ser pago é: R${valor_imposto:.2f} ")

elif tipo_investimento == 3:
    aliquota = 0
    valor_imposto = valor_resgate * aliquota
    print(f"O valor do imposto de renda a ser pago é: R${valor_imposto:.2f} ")

else:
    print("Opção inválida, reinicie o programa e tente novamente")

