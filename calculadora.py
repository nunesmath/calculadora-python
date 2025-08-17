#Define uma função que soma e retorna o resultado entre dois argumentos
def soma(a, b): 
    return a + b
#Define uma função que subtrai e retorna o resultado entre dois argumentos
def subtracao(a, b): 
    return a - b
#Define uma função que multiplica e retorna o resultado entre dois argumentos
def multiplicacao(a, b): 
    return a * b
#Define uma função que divide e retorna o resultado entre dois argumentos(Obs: Caso o divisor seja '0', uma mensagem de erro será exibida)
def divisao(a, b): 
    if b == 0:
        return('Erro: Não é possível dividir por 0')
    else:
        return a / b
#Exibe no terminal o título 'Calculadora'
print('\nCalculadora')
#Loop (while) infinito que continuamente solicita informações ao usuário até que o mesmo selecione 'sair'
while True:
    #Variável que armazena a resposta do usuário à pergunta efetuada no terminal
    operacao = input('\nInforme a operação desejada: soma, subtracao, multiplicacao, divisao ou sair: ' )
    #Checagem que verifica SE a opção informada pelo usuário anteriormente é diferente de 'sair', sendo verdadeiro (True) o restante do código é executado
    #Obs: '.lower()' transforma a entrada do usuario no formato minusculo, a fim de garantir que a entrada do usuário seja convertida para o mesmo formato das funções
    if operacao.lower() != 'sair':
        #Variável que armazena a resposta do usuário à pergunta efetuada no terminal e converte para número decimal
        primeiro_numero = float(input('\nInforme o primeiro número: '))
        #Variável que armazena a resposta do usuário à pergunta efetuada no terminal e converte para número decimal
        segundo_numero = float(input('\nInforme o segundo número: '))
        #Checagem que verifica SE a operacao informada foi soma, sendo verdadeiro a função SOMA é chamada e o resultado é exibido no terminal
        if operacao.lower() == 'soma':
            print(f'\nA soma entre {primeiro_numero} e {segundo_numero} é {soma(primeiro_numero, segundo_numero)}')
        #Checagem que verifica SE a operacao informada foi subtração, sendo verdadeiro a função SUBTRACAO é chamada e o resultado é exibido no terminal
        elif operacao.lower() == 'subtracao':
            print(f'\nA subtração de {primeiro_numero} por {segundo_numero} é {subtracao(primeiro_numero, segundo_numero)}')
        #Checagem que verifica SE a operacao informada foi multiplicação, sendo verdadeiro a função MULTIPLICACAO é chamada e o resultado é exibido no terminal
        elif operacao.lower() == 'multiplicacao':
            print(f'\nA multiplicação entre {primeiro_numero} e {segundo_numero} é {multiplicacao(primeiro_numero, segundo_numero)}')
        #Checagem que verifica SE a operacao informada foi divisão, sendo verdadeiro a função DIVISAO é chamada e o resultado é exibido no terminal
        elif operacao.lower() == 'divisao':
            print(f'\nA divisão de {primeiro_numero} para {segundo_numero} é {divisao(primeiro_numero, segundo_numero)}')
        #Caso o usuário tenha inserido uma operação não configurada na calculadora, a mensagem descrita será exibida no terminal
        else:
            print('Operação informada não encontrada nesta calculadora!')
    #Se a opção informada pelo usuário for SAIR, o loop (while) é interrompido e o programa encerrado.
    else:
        break