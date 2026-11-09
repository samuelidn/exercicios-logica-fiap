valor_divida = float(input("Digite o valor da dívida: "))
quantidade_parcelas = 1 #coloquei a primeira parcela aqui pois nao consegui fazer ela aparecer no loop
percentual = 0
juros = valor_divida * percentual
total = valor_divida + juros
valor_parcela = total / quantidade_parcelas

print(f"Total: R$ {total:.2f}  Juros: R$ {juros:.2f}  Número de parcelas: {quantidade_parcelas}  Valor da parcela: {valor_parcela:.2f}")

for quantidade_parcelas in range(3, 13, 3):
    percentual = ((quantidade_parcelas / 3) + 1) * 0.05
    juros = valor_divida * percentual
    total = valor_divida + juros
    valor_parcela = total / quantidade_parcelas

    print(f"Total: R$ {total:.2f} Juros: R$ {juros:.2f} Número de parcelas: {quantidade_parcelas}  Valor da parcela: {valor_parcela:.2f}")