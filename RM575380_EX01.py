#variaveis
n_colaboradores = int(input("Por favor, informe o número de colaboradores: "))
dia1 = 0
dia2 = 0
dia3 = 0
dia4 = 0
dia5 = 0

#votacao
for colaboradores in range(1, n_colaboradores + 1, 1):
    dia = input("Por favor, informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").lower()
    if dia == "segunda-feira":
        dia1 += 1 
    elif dia == "terça-feira":
        dia2 += 1
    elif dia == "quarta-feira":
        dia3 += 1
    elif dia == "quinta-feira":
        dia4 += 1
    elif dia == "sexta-feira":
        dia5 += 1

maior = dia1
if dia2 > maior:
    maior = dia2
if dia3 > maior:
    maior = dia3
if dia4 > maior:
    maior = dia4
if dia5 > maior:
    maior = dia5

maior_quantidade = 0

if dia1 == maior:
    maior_quantidade += 1
if dia2 == maior:
    maior_quantidade += 1
if dia3 == maior:
    maior_quantidade += 1
if dia4 == maior:
    maior_quantidade += 1 
if dia5 == maior:
    maior_quantidade += 1

if maior_quantidade == 1:
    if dia1 == maior:
        print("O dia escolhido pelos colaboradores foi segunda-feira.")
    elif dia2 == maior:
        print("O dia escolhido pelos colaboradores foi terça-feira.")
    elif dia3 == maior:
        print("O dia escolhido pelos colaboradores foi quarta-feira.")
    elif dia4 == maior:
        print("O dia escolhido pelos colaboradores foi quinta-feira.")
    elif dia5 == maior:
        print("O dia escolhido pelos colaboradores foi sexta feira")
else:
    print("Ouve empate entre: ")
    if dia1 == maior:
        print("segunda-feira")
    if dia2 == maior:
        print("terça-feira")
    if dia3 == maior:
        print("quarta-feira")
    if dia4 == maior:
        print("quinta-feira")
    if dia5 == maior:
        print("sexta-feira")