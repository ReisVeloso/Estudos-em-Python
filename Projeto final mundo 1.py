import gtts
from time import sleep
from playsound import playsound

nomeDoUsuario = str(input('\033[1;34mDigite seu nome: \033[m'))
print('''\n\n\n \t\t\t\t Olá \033[1;31m{}\033[m, tudo bem contigo? espero que sim!
 \t\t\t\t\tSeja bem-vindo à nossa plataforma!
Hoje vou lhe mostrar os exercícios desenvolvidos durante o \033[4;32mCurso de Python\033[m 
ministrado pelo professor \033[4;32mGustavo Guanabara\033[m na plataforma do \033[4;32mCurso em Vídeo!\033[m'''.format(nomeDoUsuario.title()))
print('''Para facilitar a navegação, fizemos um sumário para você!
Basta digitar o numero do exercicio para executá-lo. ''')
print(12*'\033[0;33m#==#==#\033[m')

with open('introducao.txt','r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha,lang='pt-br')
        frase.save('introducao.mp3')
        playsound('introducao.mp3')

sleep(2) # Para esperar 2 segundos antes de mostrar o sumário

op = 'sim'
while op == 'sim':

    print('''SUMÁRIO
    1  - Olá Mundo                          19 - Sorteio de nomes
    2  - Boas vindas                        20 - Embaralhando nomes na lista
    3  - Soma numérica                      21 - Tocando MP3
    4  - Identificando Classes              22 - Aplicando conceitos a str
    5  - Antecessor Sucessor                23 - ----------------------
    6  - Dobro, triplo e Raiz               24 - A cidade tem Santo no início do nome?
    7  - Média de Notas                     25 - Há a palavra Santo no nome
    8  - Conversor de metros                26 - Qual é a posição da letra 'o' no nome?
    9  - Taboada                            27 - Detectando o primeiro e o ultimo nome
    10 - Conversor de Real p/ Dolar         28 - Jogo de adivinha
    11 - Pintando uma parede                29 - Radar e calculo de multa
    12 - Desconto em produtos               30 - Identificador de número par ou impar
    13 - Aumento de Salário                 31 - Valor da passagem
    14 - Conversor de Temperatura           32 - O ano é bissexto?
    15 - Aluguel de carro                   33 - Identificando o maior e menor número da lista
    16 - Parte inteira de número Float      34 - Aumento de salário
    17 - Calculando hipotenusa              35 - Formando triângulos 
    18 - Sen, Cos, Tang
    ''')
    escolha = input('Temos um sumário para facilitar a sua navegação, ou seja, basta você digitar o número do exercício para executá-lo:\n ')

    if escolha == '1':
        print('Olá, mundo!')
        print('\033[1;31mProcessando código fonte . . .\033[m')
        sleep(5)
        print('''\n\n\033[1;33m#==#==#==#==#==#==#==#==\033[1;34mCÓDIGO FONTE\033[1;33m==#==#==#==#==#==#==#==#==#==\033[m\n''')
        print('''print('Olá, mundo!')''')
        print('''\n\033[1;33m#==#==#==#==#==#==#==#==#==\033[1;34mFIM\033[1;33m==#==#==#==#==#==#==#==#==#==#==#==\033[m''')
    elif escolha == '2':
        nome = str(input('Digite seu nome: '))
        print('Bem vindo ao mundo sr {}. '.format(nome))
        print('\033[1;31mProcessando código fonte . . .\033[m')
        sleep(5)
        print('''\n\n\033[1;33m#==#==#==#==#==#==#==#==\033[1;34mCÓDIGO FONTE\033[1;33m==#==#==#==#==#==#==#==#==#==\033[m\n''')
        print('''
        nome = str(input('Digite seu nome: '))
        print('Bem vindo ao mundo sr {}. '.format(nome))''')
        print('''\n\033[1;33m#==#==#==#==#==#==#==#==#==\033[1;34mFIM\033[1;33m==#==#==#==#==#==#==#==#==#==#==#==\033[m''')

    elif escolha == '3':
        i = 0
        lista = []
        while i < 2:
            numero = float(input('Digite um número: '))
            lista.append(numero)
            print(lista)
            i = i+1
        print('A soma dos números é {}. '.format(lista[0]+lista[1]))

    elif escolha == '4':
        n = input('Digite algo: ')
        print('{} é numérico? '.format(n))
        print(n.isnumeric())
        print('{} é alfabético? '.format(n))
        print(n. isalpha())

    elif escolha == '5':
        num1 = int(input('Digite um número: '))
        print('O número é {0}, o antecessor é {1} e o sucessor é {2} \n {1}-{0}-{2}'.format(num1,(num1-1),(num1+1)))

    elif escolha == '6':
        num2 = int(input('Digite um número: '))
        print('O dobro é {}, o triplo é {} e a raiz quadrada é {:.2f} '.format((num2*2),(num2*3),(num2**(1/2))))

    elif escolha == '7':
        nome = input('Digite o nome do aluno: ')
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        print('A média das notas de {} é {} pontos.'.format((nome),((nota1+nota2)/2)))

    elif escolha == '8' :
        varm = float(input("Digite a quantidade de metros a ser convertida: "))
        print('{} m equivalem a: \n {} cm \n {} mm'.format(varm,(varm*100),(varm*1000)))

    elif escolha == '9':
        num = float(input('Digite um número: '))
        i=0
        while i < 11:
            taboada = num*i
            i = i+1
            print('{:2} x {} = {}'.format((i-1),num,taboada)) # o {:2} --> Todos tem 2 dígitos... formatou alinhado, retire e rode o prog para ver

    elif escolha == '10':
        real = float(input('Digite um valor em real para converter em dolar: R$ '))
        cotacao = float(input('Digite a cotação atual do Dolar: '))
        print('{} reais equivalem a {:.2f} dolares.'.format(real,(real/cotacao)))

    elif escolha == '11':
        l = float(input('Digite o valor da largura: '))
        h = float(input('Digite o valor da altura: '))
        t = float(input('Quantos m² 1 l de tinta pinta? '))
        area = l*h
        print('Sua parede tem {} m² de área e precisará de {} l de tinta para ser totalmente pintada. '.format(area,(area/t)))

    elif escolha =='12':
        valor_inicial = float(input('Digite o valor do produto: '))
        valor_do_desconto = float(input('Digite o valor do desconto em % "não precisa colocar o simbolo de %": '))
        valor_final= valor_inicial-((valor_do_desconto/100)*(valor_inicial))
        print('O produto é {:.2f} reais \n O desconto é de {:.2f} reais \n O valor final é de {:.2f} reais'.format(valor_inicial, valor_do_desconto, valor_final))

    elif escolha == '13':
        salario = float(input('Digite o valor do salário do funcionário: '))
        aumento = float(input('Digite o valor do aumento em %: '))
        print('O salário atualizado é {:.2f} reais '.format(salario+(salario*(aumento/100))))

    elif escolha == '14':
        c = float(input('Digite uma temperatura em ºC: '))
        k = float(c+273)
        f = float((c*1.8)+32)
        r = float(c*(9/5)+491.67)
        print('{:.2f} Cº equivalem a: \n{:.2f} k \n{:.2f} f \n{:.2f} r'.format(c,k,f,r))

    elif escolha == '15':
        dias = int(input('Digite a quantidade de dias: '))
        km = float(input('Digite a quantidade de km rodados: '))
        val_dias = float(input('Digite o valor referente a cada dia rodado: '))
        val_km = float(input('Digite o valor referente a cada km rodado: '))
        print('Você deverá pagar {} reais.\n OBRIGADO PELA PREFERÊNCIA '.format((dias*val_dias)+(km*val_km)))

    elif escolha == '16':
        from math import trunc
        var = float(input('Digite um número float para demonstrar a parte inteira: '))
        print('O número é {} e a parte inteira é {}. '.format(var,trunc(var)))

    elif escolha == '17':
        from math import pow, sqrt
        cat_op = float(input('Digite o valor do cateto oposto: '))
        cat_adj = float(input('Digite o valor do cateto adjacente: '))
        hip = sqrt((pow(cat_op, 2) + pow(cat_adj, 2))) # pow(x,y) = x**y que é x elevado a y.
        print('A hipotenusa equivalente vale {:.2f} '.format(hip))
        # Pode ser utilizado o comando math.hypot(cat_op,cat_adj) para facilitar

    elif escolha == '18':
        import math

        num = float(input('Digite o valor do ângulo desejado: '))
        sen = float(math.sin(math.radians(num)))
        cos = float(math.cos(math.radians(num)))
        tan = float(math.tan(math.radians(num))) # Repare que está convertendo o a tangente em radianos para n aparecer um grau.
        print('O seno é {:.2f}, o Cosseno é {:.2f} e a Tangente é {:.2f}. '.format(sen,cos,tan))

    elif escolha == '19':
        import random # ou from random import choice
        lista = []
        op = input('Deseja incluir um nome à lista? ')
        while op == 'sim':
            nome = input('Digite um nome: ')
            lista.append(nome)
            print(lista)
            op = input('Deseja adicionar mais um nome? ')
        print('A lista de nomes é {} e o nome sorteado foi: {} '.format(lista,random.choice(lista)))

    elif escolha == '20':
        import random
        lista = []
        op = input('Deseja adicionar um nome à lista? ')
        while op == 'sim':
            nome = input('Digite um nome: ')
            lista.append(nome)
            print(lista)
            op = input('Deseja adicionar outro nome? ')
        random.shuffle(lista)
        print(lista)

    elif escolha == '21':
        from playsound import playsound
        playsound("ex021.mp3")

    elif escolha == '22':
        nome = str(input('Digite seu nome completo: '))
        print('O nome em maiúsculo é {} e minúsculo é {} '.format( nome.upper(),nome.lower() ))
        print('O nome tem {} posições com espaço e {} sem espaço '.format(len(nome),len(nome.replace(' ',''))))
        listando = nome.split()
        print('O primeiro nome é {} e ele tem {} posições'.format(listando[0], len(listando[0])))

    elif escolha == '23':
        print('Rever aula de exercícios 23')

    elif escolha == '24':
        nome = str(input('Digite o nome da cidade: '))
        converte = nome.upper()
        tt = converte.find('SANTO')
        print(tt)# ta aqui só para mostrar que  o comando converte.find da a posição
        if tt == 0:
            print('Tem a palavra santo no início')
        else:
            print('Não tem a palavra santo no início')

    elif escolha == '25':
        nome = input('Digite o nome da pessoa: ')
        converter = nome.upper()
        print('Ha a palavra santos no nome da pessoa? {} '.format('SANTOS' in converter))

    elif escolha == '26':
        cid = str(input('Digite o nome da cidade: ')).strip().lower()
        var1 = cid.find('o')# Onde está o primeiro O
        var2 = cid.rfind('o')# onde esta localizado o ultimo
        print('A primeira posição do o é {} e o ultimo é {} '.format(var1+1, var2+1))# a maquina começa a contar do zero e a gente começa do 1

    elif escolha == '27':
        nome = input('Digite o primeiro nome: ')
        nome = nome.strip()
        nome = nome.title()
        nome = nome.split()
        conta = len(nome)
        print('O primeiro nome é {} e o ultimo é {} '.format(nome[0], nome[conta - 1]))
        # Poderia ter utilizado o find e rfind, para facilitar.

    elif escolha == '28':
        import random
        numero = random.randint(0,5)
        usuario = int(input('Digite um número de 0 a 5: '))
        if numero == usuario:
            print('Você brilhou, o número {} foi o escolhido. '.format(usuario))
        else:
            print('O número escolhido por você foi {} e o Sorteado foi {}. '.format(usuario,numero))
        print('Obrigado por jogar comigo!')

    elif escolha == '29':
        velocidade = float(input('vmax = 80km/h. Digite a velocidade do veículo: '))
        if velocidade > 80:
            print('Você ultrapassou o limite de velocidade em {} km/h e deverá pagar R${:.2f} de multa. '.format(velocidade-80,(velocidade-80)*7))

    elif escolha == '30':
        numero = int(input('Digite um número: '))
        var = numero%2
        if var == 1:
            print('É impar')
        else:
            print('É par')

    elif escolha == '31':
        distancia = float(input('Quantos km até o seu destino? '))
        if distancia <= 200:
            print('O valor da sua passagem é de R${} '.format(distancia*0.5))
        else:
            print('O valor da sua passagem é R${} '.format(distancia*0.45))
        print('Boa Viagem')

    elif escolha == '32':
        import calendar
        op = int(input('digite o ano: '))
        calendario = calendar.month(op, 2) # Var calendário recebe o caendario do ano input e mes 2 que é o que varia no ano bisexto
        print(calendario)
        calendario = calendario.replace('\n','').replace(' ', '') # Calendário escrito todo em linha sem espaço e \n
        calendario = calendario[26:] #inicia a contagem da posição 26 pra frente, para ignorar o texto February2000MoTuWeThFrSaSu, ou seja, inicia a contagem de posição do dia 1 e vê se vai até 28 ou 29 dias
        print(len(calendario))
        if len(calendario) == 49:# é 49 pois o número 0 ocupa uma posição mas o número 10 contabiliza duas posições, a do 1 e a do 0.
            print('É bissexto')
        else:
            print('Não é bissexto')

    elif escolha == '33':
        op = str(input('Quer adicionar um número? ')).lower().strip()
        lista = []
        i=0
        if i==0:
            while i<=2:
                add = int(input('Digite um número: '))
                add = lista.append(add)
                print(lista)
                i=i+1

        op = str(input('Quer adicionar outro número? ')).lower().strip()
        while op == 'sim':
            add = int(input('Digite um número: '))
            add = lista.append(add)
            print(lista)
            op = str(input('Quer adicionar outro número?'))
        print('Sua lista é {} e o maior número é o {}, equanto o menor é {} .'.format(lista, max(lista), min(lista))) # max(lista) mostra o maior número da lista e o mesmo vale para o min.

    elif escolha == '34':
        salario = int(input('Digite o valor do salário: '))
        if salario > 1250:
            aumento = salario*0.1
            print('O aumento é de {} e o novo salário é {} .'.format(aumento,salario+aumento))
        else:
            aumento = salario*0.15
            print('O aumento é de {} e o novo salário é {} .'.format(aumento, salario+aumento))
        print(' Obrigado por trabalhar conosco!')
    elif escolha == '35':
        import statistics # Para chamar a função 'median' e pegar o número do meio da lista ou a média dos números do meio da lista
        lista = []
        i=0
        if i==0:
            while i<3:
                lado = float(input('Digite o valor do lado: '))
                lado = lista.append(lado)
                i=i+1
        print('Os lados são {}. '.format(lista))
        print('O maior lado é {} e o menor lado é {} .'.format(max(lista), min(lista)))
        if max(lista)< (min(lista)+(statistics.median(lista))):
            print('Os números {} podem formar triângulo. '.format(lista))
        else:
            print('Os números {} não podem formar triângulo'.format(lista))
    op = str(input('Deseja executar outro exercício? '))
    op = op.lower().strip()
if op != 'sim':
    opCodFon = str(input('Gostaria de ver meu código fonte? ')).strip().lower()
    if opCodFon == 'sim':
        print('\033[1;31mProcessando código fonte . . .\033[m')
        sleep(10)
        print('''\n\n\033[1;33m#==#==#==#==#==#==#==#==\033[1;34mCÓDIGO FONTE\033[1;33m==#==#==#==#==#==#==#==#==#==\033[m\n''')
        print('''CODIGO FONTE AQUI via link ou arquivo''')
        print('''\n\033[1;33m#==#==#==#==#==#==#==#==#==\033[1;34mFIM\033[1;33m==#==#==#==#==#==#==#==#==#==#==#==\033[m''')

        print('Obrigado por utilizar nossos programas')
    else:
        print('Obrigado por utilizar nossos programas')