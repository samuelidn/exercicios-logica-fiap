valor_carro = float(input("Digite o preço do carro: "))
desconto = valor_carro * 0.20
valor_a_vista = valor_carro - desconto

print(f"O preço final á vista com desconto de 20% é: R${valor_a_vista}")

for parcelas in range(6, 61, 6):
    percentual = parcelas * 0.5 / 100
    acrescimo = valor_carro * percentual
    preco_final = valor_carro + acrescimo
    valor_parcela = preco_final / parcelas

    print(f"O preço final parcelado em {parcelas:.0f} X é de R$ {preco_final:.2f} com parcelas de R$ {valor_parcela:.2f} ")