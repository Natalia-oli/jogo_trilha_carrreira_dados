def divisoria():
    print("*" * 80)


def texto():

    print("As profissões ligadas a análises de dados estão cada vez mais em alta no mercado. \n"
    "Isso tem acontecido graças ao aumento da importância de tratar e interpretar os grandes \n"
    "fluxos de dados gerados pela sociedade. \n") 
    espaco()
    print("As análises de Big Data têm possibilitado que as empresas captem insights poderosos \n"
    "sobre seus consumidores, permitindo que elas tomem decisões estratégicas para seus negócios.\n"
    "O volume de dados gerado constantemente se tornou um dos principais desafios das empresas na \n" 
    "atualidade. Portanto, elas passaram a depender, cada vez mais, de profissionais capacitados \n"
    "a realizarem todas as etapas de uma análise de dados - armazenar, separar, traduzir e fazer \n"
    "bom uso das informações. \n")


def andar():
    andar = input(print("Digite a letra A para andar e abrir a porta seguinte:")).upper()


def espaco():
    print("\n")


def falta():
    falta_aulas = int(input("> QUANTAS AULAS FALTOU ATÉ O MOMENTO?"))
    return falta_aulas


def qualified():
    atividades_qualified = int(input(" > INDIQUE COM O NÚMERO CORRESPONDENTE:QUANTAS ATIVIDADES DO QUALIFIED DEIXOU DE FAZER:"))
    return atividades_qualified


def resultado(pontos_feitos):
    if (pontos_feitos > 0 ) and (pontos_feitos <= 62):
        print("Sua pontuação total foi {} e por isso, quando para o MM2 (MÓDULO 2)chegar, voce corre o risco de ficar perdido, então, foi derrotado pelo Modulo 1. PERDEU!".format(contador_pontos))
        
    elif (pontos_feitos > 63) and (pontos_feitos <= 70):
        print("Sua pontuação foi de {} e por isso, voce conseguiu driblar o MM1(MÓDULO 1), será bem sucedido na luta contra os outros módulos. VENCEU! PARABENS!".format(contador_pontos))
        
    elif pontos_feitos >= 71:
        print("Sua pontuação foi de {} e conseguiu vencer o MM1(MÓDULO 1) com perfeição. PARABENS! Foi uma otima performace!".format(contador_pontos))
        
    elif pontos_feitos < 0:
        print("Sua pontuação foi de {} e por isso voce foi infinitamente derrotado pelo MM1 (MÓDULO 1)".format(contador_pontos))
        
    elif pontos_feitos >= -40:
        print("Voce perdeu feio!")


contador_pontos = 0 

#PARTE 1 - VISUAL 
espaco()
espaco()
divisoria()
print("TRILHA DO PROFISSIONAL DE ANÁLISE DE DADOS - MODULO 1\n")

divisoria()
print("NUNCA SALAS FORAM TÃO DECISIVAS NA SUA VIDA!\n ")

divisoria()
print("VOCÊ CONHECE O MM1? NÃO? CONHECERÁ HOJE!!!\n ")

divisoria()
print("2021 - #VAMOAI - RESILIA E IFOOD")
divisoria()
texto()


#PARTE 2 - DESCRIÇÃO DOS AVATARES
print("Para chegar mais próximo de ser um analista de dados será necessário\n" 
"escolher quem você quer ser nessa jornada: \n"
"1 - O ser que faz as coisas sempre no último segundo - poster \n" 
"2 - Está sempre disponível e disposto a ajudar e tenta cumprir tudo no prazo - onipresente \n"
"3 - O 'deixa a vida me levar e faz do jeito que dá certo' - ondestou \n"
"4 - Oferece o máximo de si, apesar das circuntâncias - esformax")

espaco()

print("Mas é necessário que passe por um primeiro teste * ELIMINÁRIO * primeiro, no qual \n" 
"poderá ser derrotado de primeira, ou não [...] \n")


#PARTE 3 - TESTE INICIAL E ESCOLHA DOS AVATARES
primeiro_teste = falta()
segundo_teste = qualified()

if (primeiro_teste >= 3) or (segundo_teste >= 3):
    print("Não insista. Você já foi derrotado!")
else:
    print("PASSOU NOS PRIMEIROS DOIS TESTES. AGORA ESTÁ LIBERADO PARA ESCOLHER SEU AVATAR ^-^")
    avatar = int(input("Digite o número referente a sua escolha de avatar:\n\n"))
    avatar_do_jogo = avatar

    if avatar == 1:
        print ("Olá, Poster, nessa trilha para alcançar a formação plena com enfâse na análise de dados,\n"
        "voce passará por um corredor com algumas salas e entrará em cada uma, lendo as perguntas dos \n "
        "telões e respondendo com sinceridade :) \n"  
        "****Há um monstro invisivel, chamado de MM1[Mostro Módulo 1],para derrota-ló, \n"
        "suas respostas são as armas e depende de você, elas serem poderosas ou não! \n\n\n"
        "BOA SORTE! AO FINAL, SABEREMOS ONDE SEU PERCURSO LHE LEVOU NESSE MM1!****\n")

    elif avatar == 2:
        print ("Olá, onipresente, nessa trilha para alcançar a formação plena com enfâse na análise de dados, \n "
        "voce passará por um corredor com algumas salas e entrará em cada uma, lendo as perguntas dos\n"
        "telões e respondendo com sinceridade :) \n "
        "****Há um monstro invisivel, chamado de MM1(Mostro Módulo 1),para derrota-ló, \n"
        "suas respostas são as armas e depende de você, elas serem poderosas ou não!\n \n \n"
        "BOA SORTE! AO FINAL, SABEREMOS ONDE SEU PERCURSO LHE LEVOU NESSE MM1!****\n")

    elif avatar == 3:
        print ("Olá, ondestou, nessa trilha para alcançar a formação plena com enfâse na análise de dados,\n"
        "voce passará por um corredor com algumas salas e entrará em cada uma, lendo as perguntas dos \n"
        "telões e respondendo com sinceridade :) \n"
        "****Há um monstro invisivel, chamado de MM1(Mostro Módulo 1), para derrota-ló,\n"
        "suas respostas são as arcas e depende de você, elas serem poderosas ou não! \n\n\n"
        "BOA SORTE! AO FINAL, SABEREMOS ONDE SEU PERCURSO LHE LEVOU NESSE MM1!\n")

    elif avatar == 4:
        print ("Olá, esformax, nessa trilha para alcançar a formação plena com enfâse na análise de dados,\n"
        "voce passará por um corredor com algumas salas e entrará em cada uma, lendo as perguntas dos \n" 
        "telões e respondendo com sinceridade :)\n"
        "Há um monstro invisivel, chamado de MM1(Mostro Módulo 1), para derrota-ló, \n"
        "suas respostas são as arcas e depende de você, elas serem poderosas ou não! \n\n\n"
        "BOA SORTE! AO FINAL, SABEREMOS ONDE SEU PERCURSO LHE LEVOU NESSE MM1! \n")

#PRINCIPAL
if (avatar == 1) or (avatar == 2) or (avatar == 3) or (avatar_do_jogo == 4):
    modulo1 = int(input("O predio é vermelho e as salas lhe atraem como imãs e você é levado \n"
    "como que sem entender o porque e como. A primeira sala que entrou é conhecida como SALA TECH|\n"
    "SOFT, com uma tela expressando a seguinte frase:\n" 
    "> VOCE SENTE QUE APRENDEU TODOS OS CONCEITOS|CONTEÚDOS DE SOFT E TECH DO MÓDULO 1?\n"
    "(1) - SIM \n (2) - NÃO, DEIXEI DE COMPREENDER ALGUNS|ALGUM:\n"))
    if modulo1 == 1:
        contador_pontos = contador_pontos + 10
        print("PARABENS! VOCE ADQUIRIU {} PONTOS E ESTÁ MAIS FORTE PARA DERROTAR O MM1!\n \n ".format(contador_pontos))
        andar()
    else:
        contador_pontos = contador_pontos - 10
        print("VOCE JÁ COMEÇOU PERDENDO 10 PONTOS: {} E POR ISSO PRECISARÁ IR PARA A SALA DO REFORÇO, \n"
        "REVISAR PARA CHEGAR MAIS FORTE AO MM2!\n\n ".format(contador_pontos))
        andar()


    ajuda = int(input("Agora, voce é expulso para o corredor e a sala mais a frente é a SALA DA AJUDA.\n "
    "O telão exibe a pergunta:\n"
    "> VOCE AJUDOU ALGUÉM, DE ALGUMA MANEIRA, DURANTE O MÓDULO 1?\n (1) - SIM \n (2) - NÃO: \n"))
    if ajuda == 1:
        contador_pontos = contador_pontos + 10
        print("PARABENS! VOCE AGORA ESTA COM {} PONTOS!".format(contador_pontos))
        print("DEVIDO ISSO, TORNOU-SE MAIS FORTE NO CONCEITO SOFT SKILSS! AS EMPRESAS GOSTAM! <3\n\n")
        andar()
    else:
        contador_pontos = contador_pontos - 10
        print("VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
        print("REFLITA SOBRE A IMPORTÂNCIA DO TRABALHO E EVOLUÇÃO EM GRUPO , QUANDO ENSINAMOS APRENDEMOS.\n" 
        "DIRIJA-SE A SALA DA AJUDA!\n\n")
        for i in range (1, 5):
            print("aprendendo sobre a importancia da evolução em grupo: {} dia".format(i))
            andar()
            
    monitoria = input("A próxima sala é a SALA DA MONITORIA, que apresenta a seguinte pergunta:\n"
    "> VOCE PARTICIPOU DAS MONITORIAS ?  \n (1) - ENTRE 1 E 3 MONITORIAS \n (2) - ENTRE 4 - 6 \n"
    "(3)- MAIS DE 7 \n (4) - NENHUMA DAS ALTERNATIVAS:")
    if monitoria == 1:
        contador_pontos = contador_pontos + 10
        print("PARABENS! AGORA VOCE ESTA COM:{} PONTOS".format(contador_pontos))
        andar()
    elif monitoria == 2:
        contador_pontos = contador_pontos + 20
        print("PARABENS! VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
        andar()
    elif monitoria == 3: 
        contador_pontos = contador_pontos + 30
        print("PARABENS! VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
        andar()
    elif monitoria == 4:
        contador_pontos = contador_pontos - 10
        print( "VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
        andar()
    else:
        print("Digite um dos numeros indicados\n\n\n")
        andar()
    
    curso_alura = int(input("Seguindo nas salas,a próxima é a SALA DA ALURA, com a seginte pergunta:\n"
    "> VOCE FEZ ALGUM CURSO COMPLETO NA ALURA?:\n (1) - SIM, UM OU MAIS DE UM \n (2) - NÃO, NENHUM:\n\n\n"))
    if curso_alura == 1:
        contador_pontos = contador_pontos + 10
        print("PARABENS! VOCE AGORA ESTA COM {} PONTOS!".format(contador_pontos))
        andar()
    else:
        contador_pontos = contador_pontos - 10
        print("VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
        andar()

    atividades_pdf = int(input("A outra pergunta realizada está na SALA DOS PDFS:\n"
    "> ATÉ AQUI, VOCE CONSUMIU TUDO ENVIADO NOS PDFS? \n (1) - SIM \n (2) - NÃO,\n (3) - MAIS OU MENOS:\n\n\n "))
    if atividades_pdf == 1:
        contador_pontos = contador_pontos + 10
        print("PARABENS! VOCE AGORA ESTA COM {} PONTOS!\n\n".format(contador_pontos))
        
    elif atividades_pdf == 2:
        contador_pontos = contador_pontos - 10
        print("VOCE AGORA ESTA COM {} PONTOS\n\n".format(contador_pontos))
        
    elif atividades_pdf == 3:
        contador_pontos = contador_pontos + 4
        print("VOCE AGORA ESTA COM {} PONTOS\n\n".format(contador_pontos))
        
    else:
        print("Digite um número válido!\n\n")
    

#CHAMADA DA FUNÇÃO QUE VAI APRESENTAR O RESULTADO DO JOGO
pontos_feitos = contador_pontos
resultado(pontos_feitos)







    

  
    
        

    


