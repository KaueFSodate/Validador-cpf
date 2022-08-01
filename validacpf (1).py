

while True:
    nome = input('Digite o seu nome: ')
    data = input('Digite a sua data de nascimento: ')
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    # Loop do CPF
    #
    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf and not sequencia:
        print('Usuário cadastrado com cpf válido')
    else:
        print('Usuário nao cadastrado com cpf inválido')
