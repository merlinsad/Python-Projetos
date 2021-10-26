import PySimpleGUI as sg 

print("                                                             |---------------------/////////////////////////////////////---------------------------------|")
print("                                                             |                                 Seja bem vindo(a)!!!!                                     |")
print("                                                             |        Agora que você adentrou no Reino de Vesquer. Pressione 'Enter' para começarmos.    |")
print("                                                             |---------------------/////////////////////////////////////---------------------------------|")
iniciar = input("")

classe1 = 'Mago'
classe2 = 'Guerreiro'
classe3 = 'Tank'
classe4 = 'Arqueiro'
decisao_mapa_mago = 1
certeza_mapa_mago = 1
decisao_mapa_guerreiro = 1
certeza_mapa_guerreiro = 1
decisao_mapa_Arqueiro = 1
certeza_mapa_arqueiro = 1
decisao_mapa_Tank = 1
certeza_mapa_tank = 1

retornoInfo = 2
#Informações sobre as classes
while(retornoInfo == 2):
    classeInfo = input("|Para começarmos, temos as 4 classes: Mago, Guerreiro, Tank e Arqueiro.|\n|Caso queira informações sobre classes, digite abaixo o nome da mesma, |\n|se quiser, pode apertar 'Enter', para continuar.                      |\n")
    if(classeInfo == 'Mago') or (classeInfo == 'mago'):
        print("Mago: A classe que vai te permitir, utilizar de todos os 4 elementos para enfrentar seus inimigos, ou até mesmo, dependendo do quanto for sua determinação,\npode alterar suas magias para direcioná-las ao seus alidos, e poder fortalece-los e os auxiliando em batalha.\nAlém de poder combinar os elementos e criar poderes totalmente únicos, com essa clase, a única limitação é sua imaginação e determinação de correr atrás dos poderes.")
        print("                                                  |---------------------------////////////////////////////////////////////////////////-----------------------------|")
        print("                                                  |                                                Atributos iniciais:                                             |")
        print("                                                  |                                                      HP: 150                                                   |")
        print("                                                  |                                                     Mana: 200                                                  |")
        print("                                                  |                                                    Ataque: 80                                                  |")
        print("                                                  |                                                  Estamina: 100                                                 |")
        print("                                                  |                                                   Defesa: 90                                                   |")
        print("                                                  |                                                  Agilidade: 90                                                 |")
        print("                                                  |                                                Inteligência: 180                                               |")
        print("                                                  |---------------------------////////////////////////////////////////////////////////-----------------------------|")
        retornoInfo = int(input("Gostaria de retornar a tela de classes para mais informações, ou avançar e escolher sua classe?\n1- Escolher Classe\n2- Mais inforamções\n- "))
    if(classeInfo == 'Guerreiro') or (classeInfo == 'guerreiro'):
        print("Guerreiro: A classe que vai fazer ser o Mestre das Armas, você será capaz de utilizar qualquer coisa como arma, e poder utiliza-la como maestria, sendo sua única limitação, sua própria prática, quanto mais praticar, mais forte irá se tornar, podendo utilizar desde um simples graveto como arma, até um martelo com duas vezes seu tamanho.\nUníca limitação que vai perdurar em você é o limite do seu corpo, que é o que você pode treinar ao longo tempo.")
        print("                                                  |---------------------------////////////////////////////////////////////////////////-----------------------------|")
        print("                                                  |                                                Atributos iniciais:                                             |")
        print("                                                  |                                                      HP: 180                                                   |")
        print("                                                  |                                                     Mana: 100                                                  |")
        print("                                                  |                                                    Ataque: 140                                                 |")
        print("                                                  |                                                  Estamina: 150                                                 |")
        print("                                                  |                                                   Defesa: 110                                                  |")
        print("                                                  |                                                  Agilidade: 80                                                 |")
        print("                                                  |                                                Inteligência: 110                                               |")
        print("                                                  |---------------------------////////////////////////////////////////////////////////-----------------------------|")
        retornoInfo = int(input("Gostaria de retornar a tela de classes para mais informações, ou avançar e escolher sua classe?\n1- Escolher Classe\n2- Mais inforamções\n- "))
    if(classeInfo == 'Tank') or (classeInfo == 'tank'):
        print("Tank: Nessa você vai tomar porrada, ah se vai tomar, porém, como um bom Tank, você vai aguentar, e conforme o tempo for passando, inúmeros ataques que já fizeram efeito em você, não chegarão nem a arranhar sua armadura. Você possui a capacidade inata de se fortalaecer com as fraquezas, até que chegue num ponto que será preciso muito dano para lhe derrotar.\nAlém de que em sua pele, qualquer armadura começa a se reconstruir, afinal você parte de uma classe que foi feita para lutar e aguentar tudo que vier pela frente, sem medo da batalha.")
        print("                                                  |---------------------------////////////////////////////////////////////////////////-----------------------------|")
        print("                                                  |                                                Atributos iniciais:                                             |")
        print("                                                  |                                                      HP: 250                                                   |")
        print("                                                  |                                                     Mana: 70                                                   |")
        print("                                                  |                                                    Ataque: 90                                                  |")
        print("                                                  |                                                  Estamina: 100                                                 |")
        print("                                                  |                                                   Defesa: 200                                                  |")
        print("                                                  |                                                  Agilidade: 60                                                 |")
        print("                                                  |                                                Inteligência: 100                                               |")
        print("                                                  |---------------------------////////////////////////////////////////////////////////-----------------------------|")
        retornoInfo = int(input("Gostaria de retornar a tela de classes para mais informações, ou avançar e escolher sua classe?\n1- Escolher Classe\n2- Mais inforamções\n- "))
    if(classeInfo == 'Arqueiro') or (classeInfo == 'arqueiro'):
        print("Arqueiro: Sendo desta classe, você vai ter a melhor visão de todas, sendo possível acertar alvos a quilômetros de distância, conforme for fortalecendo e melhorando suas habilidades, cada vez será possível você fortalecer suas flechas, afinal, no mundo de Vesquer, todos os arqueiros vieram de linhagens Élficas, e assim sendo, você consiguira imbuir suas flechas com seus poderes, sendo possível, tornar-las rápidas como uma bala, atear fogo nela ao contato, e muitas outras habilidades ainda ocultas, do tão misterioso povo Élfico, os Myers.")
        print("                                                  |---------------------------////////////////////////////////////////////////////////-----------------------------|")
        print("                                                  |                                                Atributos iniciais:                                             |")
        print("                                                  |                                                      HP: 100                                                   |")
        print("                                                  |                                                     Mana: 130                                                  |")
        print("                                                  |                                                    Ataque: 130                                                 |")
        print("                                                  |                                                  Estamina: 120                                                 |")
        print("                                                  |                                                   Defesa: 90                                                   |")
        print("                                                  |                                                  Agilidade: 150                                                |")
        print("                                                  |                                                Inteligência: 140                                               |")
        print("                                                  |---------------------------////////////////////////////////////////////////////////-----------------------------|")
        retornoInfo = int(input("Gostaria de retornar a tela de classes para mais informações, ou avançar e escolher sua classe?\n1- Escolher Classe\n2- Mais inforamções\n- "))
    if (retornoInfo == 1) or (classeInfo == ""):
                escolhaClasse = input("Então vamos lá, qual vai ser sua escolha de classe?\n- Guerreiro\n- Mago\n- Tank\n- Arqueiro\nEscreva a opção: ")
                #Escolha da classe Mago
                if(escolhaClasse == 'Mago') or (escolhaClasse == 'mago'):
                        escolhaMago = input("Você selecinou a classe Mago, tem certeza disso?\nR: ")
                        if(escolhaMago == 'Sim') or (escolhaMago == 'sim'):
                            print("Você escolheu Mago!")
                            escolha_Nome_Mago = input("Agora que você escolheu sua classe. Me diga, qual seu nome?\nR: ")
                            certeza_Nome_Mago = input("Tem certeza de seu nome?\n- ")
                            if(certeza_Nome_Mago == 'nao') or (certeza_Nome_Mago == 'não') or (certeza_Nome_Mago == 'Não') or (certeza_Nome_Mago == 'Nao'):
                                escolha_Nome_Mago = input("Então qual seu nome?\n- ")
                                certeza_Nome_Mago = input("Tem certeza de seu nome?\n- ")
                                certeza_absoluta = input("Ta, mas você tem CERTEZA ABSOLUTA?\n R: ")
                            if(certeza_Nome_Mago == 'Sim') or (certeza_Nome_Mago == 'sim') or (certeza_Nome_Mago == 'SIM'):
                                inicio_Jogo_Mago = input(f'Pois bem.\nSeja Muito bem vindo(a) {escolha_Nome_Mago} ao Mundo de Vesquer!!!!!')
                                retornoInfo = retornoInfo - 1
                                if(inicio_Jogo_Mago == "") or (inicio_Jogo_Mago != ""):
                                        print("--------------------")
                                        #Escolher mapa do Mago
                                        while(decisao_mapa_mago == 1) or (certeza_mapa_mago == 'Não') or (inicio_Jogo_Mago == "") or (inicio_Jogo_Mago != ""):
                                            print("Entre os mais inteligentes Magos de Vesquer, inúmeros começaram sua jornada em cidades simples, com muitos livros e muita vontade de aprender, aos que nascem com o dom da magia, uma visão do mundo diferente\né sua realidade, e são poucos lugares que lhe permitem crescer explorando suas capacidades desde pequeno.")
                                            escolha_mapa_Mago = input("Entre as 4 opções, temos:\n- Sindlar\n- Tylum\n- Poltor\n- Feldar\nGostaria de obter informações sobre algum mapa, ou apenas escolher qualquer mapa e iniciar sua jornada?\nCaso, queira obter informações, digite o nome do mapa, caso contrário, tecle Enter, que o menu de seleção vai aparecer.\n- ")
                                            if(escolha_mapa_Mago == 'Sindlar'):
                                                print("Sindlar: A terra dos sábios, aqueles que anceiam por conhecimento, onde todo conhecimento é livre, e que reconhecem que o verdadeiro poder não está em ter o corpo mais bruto ou saber como usar uma arma, mas sim vencer uma luta com o poder da mente.")
                                                decisao_mapa_mago_sindlar = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                                if(decisao_mapa_mago_sindlar == ""):
                                                    mapa_escolhido_mago = input(f"Então meu caro {escolha_Nome_Mago}, qual será sua nação de origem?\n- Feldar\n- Poltor\n- Tylum\n- Sindlar\nEscreva o nome do mapa:\n- ")
                                                    if(mapa_escolhido_mago == 'Sindlar') or (mapa_escolhido_mago == 'Feldar') or (mapa_escolhido_mago == 'Poltor') or (mapa_escolhido_mago == 'Tylum') or (decisao_mapa_mago_sindlar == ""):
                                                        certeza_mapa_mago = input(f"Você tem certeza da escolha {mapa_escolhido_mago}?\nSim ou Não\n- ")
                                                        if(certeza_mapa_mago == 'Sim') or (certeza_mapa_mago == 'sim'):
                                                            print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Mago} ao mundo de Vesquer, no reino de {mapa_escolhido_mago}!")
                                                            #Iniciar jogo Mago-Sindlar
                                                            inicio_sindlar_mago = input("Sua jornada, está apenas começando.....")
                                                            break
                                            #Escolha inválida
                                            if(escolha_mapa_Mago == ""):
                                                    mapa_escolhido_mago = input(f"Então meu caro {escolha_Nome_Mago}, qual será sua nação de origem?\n- Feldar\n- Poltor\n- Tylum\n- Sindlar\nEscreva o nome do mapa:\n- ")
                                                    if(mapa_escolhido_mago == 'Sindlar') or (mapa_escolhido_mago == 'Feldar') or (mapa_escolhido_mago == 'Poltor') or (mapa_escolhido_mago == 'Tylum'):
                                                        certeza_mapa_mago = input(f"Você tem certeza da escolha {mapa_escolhido_mago}?\nSim ou Não\n- ")
                                                        if(certeza_mapa_mago == 'Sim') or (certeza_mapa_mago == 'sim'):
                                                            print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Mago} ao mundo de Vesquer, no reino de {mapa_escolhido_mago}!")
                                                            #Iniciar jogo Mago-Sindlar
                                                            inicio_sindlar_mago = input("Sua jornada, está apenas começando.....")
                                                            break
                                            if(escolha_mapa_Mago == 'Tylum'):
                                                print("Tylum: O lar do conselho onde os prodígios se reúnem para partilhar de seus conhecimentos, é possível dizer, que o lugar certo para se começar com apoio de pessoas experientes é aqui.")
                                                decisao_mapa_mago_tylum = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                                if(decisao_mapa_mago_tylum == "") or (escolha_mapa_Mago == ""):
                                                    mapa_escolhido_mago = input(f"Então meu caro {escolha_Nome_Mago}, qual será sua nação de origem?\n- Feldar\n- Poltor\n- Tylum\n- Sindlar\nEscreva o nome do mapa:\n- ")
                                                    if(mapa_escolhido_mago == 'Sindlar') or (mapa_escolhido_mago == 'Feldar') or (mapa_escolhido_mago == 'Poltor') or (mapa_escolhido_mago == 'Tylum') or (decisao_mapa_mago_sindlar == ""):
                                                        certeza_mapa_mago = input(f"Você tem certeza da escolha {mapa_escolhido_mago}?\nSim ou Não\n- ")
                                                        if(certeza_mapa_mago == 'Sim') or (certeza_mapa_mago == 'sim'):
                                                            print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Mago} ao mundo de Vesquer, no reino de {mapa_escolhido_mago}!")
                                                            #Iniciar jogo Mago-Sindlar
                                                            inicio_sindlar_mago = input("Sua jornada, está apenas começando.....")
                                                            break
                                            if(escolha_mapa_Mago == ""):
                                                    mapa_escolhido_mago = input(f"Então meu caro {escolha_Nome_Mago}, qual será sua nação de origem?\n- Feldar\n- Poltor\n- Tylum\n- Sindlar\nEscreva o nome do mapa:\n- ")
                                                    if(mapa_escolhido_mago == 'Sindlar') or (mapa_escolhido_mago == 'Feldar') or (mapa_escolhido_mago == 'Poltor') or (mapa_escolhido_mago == 'Tylum') or (decisao_mapa_mago_sindlar == ""):
                                                        certeza_mapa_mago = input(f"Você tem certeza da escolha {mapa_escolhido_mago}?\nSim ou Não\n- ")
                                                        if(certeza_mapa_mago == 'Sim') or (certeza_mapa_mago == 'sim'):
                                                            print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Mago} ao mundo de Vesquer, no reino de {mapa_escolhido_mago}!")
                                                            #Iniciar jogo Mago-Sindlar
                                                            inicio_sindlar_mago = input("Sua jornada, está apenas começando.....")
                                                            break
                                            if(escolha_mapa_Mago == 'Poltor'):
                                                print("Poltor: É possível dizer que neste lugar, reina o povo que se mantém conectado a natureza, onde todos estão em perfeita hármonia, todos prezam pela magia que mantém o equilibro da terra com os humanos, um povo tipicamente pacífico, que permanece em paz há séculos.")
                                                decisao_mapa_mago_poltor = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                                if(decisao_mapa_mago_poltor == "") or (escolha_mapa_Mago == ""):
                                                    mapa_escolhido_mago = input(f"Então meu caro {escolha_Nome_Mago}, qual será sua nação de origem?\n- Feldar\n- Poltor\n- Tylum\n- Sindlar\nEscreva o nome do mapa:\n- ")
                                                    if(mapa_escolhido_mago == 'Sindlar') or (mapa_escolhido_mago == 'Feldar') or (mapa_escolhido_mago == 'Poltor') or (mapa_escolhido_mago == 'Tylum') or (decisao_mapa_mago_sindlar == ""):
                                                        certeza_mapa_mago = input(f"Você tem certeza da escolha {mapa_escolhido_mago}?\nSim ou Não\n- ")
                                                        if(certeza_mapa_mago == 'Sim') or (certeza_mapa_mago == 'sim'):
                                                            print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Mago} ao mundo de Vesquer, no reino de {mapa_escolhido_mago}!")
                                                            #Iniciar jogo Mago-Sindlar
                                                            inicio_sindlar_mago = input("Sua jornada, está apenas começando.....")
                                                            break
                                            if(escolha_mapa_Mago == ""):
                                                    mapa_escolhido_mago = input(f"Então meu caro {escolha_Nome_Mago}, qual será sua nação de origem?\n- Feldar\n- Poltor\n- Tylum\n- Sindlar\nEscreva o nome do mapa:\n- ")
                                                    if(mapa_escolhido_mago == 'Sindlar') or (mapa_escolhido_mago == 'Feldar') or (mapa_escolhido_mago == 'Poltor') or (mapa_escolhido_mago == 'Tylum') or (decisao_mapa_mago_sindlar == ""):
                                                        certeza_mapa_mago = input(f"Você tem certeza da escolha {mapa_escolhido_mago}?\nSim ou Não\n- ")
                                                        if(certeza_mapa_mago == 'Sim') or (certeza_mapa_mago == 'sim'):
                                                            print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Mago} ao mundo de Vesquer, no reino de {mapa_escolhido_mago}!")
                                                            #Iniciar jogo Mago-Sindlar
                                                            inicio_sindlar_mago = input("Sua jornada, está apenas começando.....")
                                                            break
                                            if(escolha_mapa_Mago == 'Feldar'):
                                                print("Feldar: Um povo que vive em união com os Élfos, que aprenderam a viver em harmonia, povos que buscam a igualdade, perante o preconceito que os Élfos sofrem em meio a sociedade, e a soberania da raça humana perante o reino de Vesquer, um país tipicamente político que persiste em manter igualdade entre as raças, e almeja juntar novamente as nações que um dia ja foram uma só. ")
                                                decisao_mapa_mago_feldar = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                                if(decisao_mapa_mago_feldar == "") or (escolha_mapa_Mago == ""):
                                                    mapa_escolhido_mago = input(f"Então meu caro {escolha_Nome_Mago}, qual será sua nação de origem?\n- Feldar\n- Poltor\n- Tylum\n- Sindlar\nEscreva o nome do mapa:\n- ")
                                                    if(mapa_escolhido_mago == 'Sindlar') or (mapa_escolhido_mago == 'Feldar') or (mapa_escolhido_mago == 'Poltor') or (mapa_escolhido_mago == 'Tylum') or (decisao_mapa_mago_sindlar == ""):
                                                        certeza_mapa_mago = input(f"Você tem certeza da escolha {mapa_escolhido_mago}?\nSim ou Não\n- ")
                                                        if(certeza_mapa_mago == 'Sim') or (certeza_mapa_mago == 'sim'):
                                                            print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Mago} ao mundo de Vesquer, no reino de {mapa_escolhido_mago}!")
                                                            #Iniciar jogo Mago-Sindlar
                                                            inicio_sindlar_mago = input("Sua jornada, está apenas começando.....")
                                                            break
                                            if(escolha_mapa_Mago == ""):
                                                    mapa_escolhido_mago = input(f"Então meu caro {escolha_Nome_Mago}, qual será sua nação de origem?\n- Feldar\n- Poltor\n- Tylum\n- Sindlar\nEscreva o nome do mapa:\n- ")
                                                    if(mapa_escolhido_mago == 'Sindlar') or (mapa_escolhido_mago == 'Feldar') or (mapa_escolhido_mago == 'Poltor') or (mapa_escolhido_mago == 'Tylum') or (decisao_mapa_mago_sindlar == ""):
                                                        certeza_mapa_mago = input(f"Você tem certeza da escolha {mapa_escolhido_mago}?\nSim ou Não\n- ")
                                                        if(certeza_mapa_mago == 'Sim') or (certeza_mapa_mago == 'sim'):
                                                            print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Mago} ao mundo de Vesquer, no reino de {mapa_escolhido_mago}!")
                                                            #Iniciar jogo Mago-Sindlar
                                                            inicio_sindlar_mago = input("Sua jornada, está apenas começando.....")
                                                            break
                #Escolha de classe Guerreiro
                if(escolhaClasse == 'Guerreiro') or (escolhaClasse == 'guerreiro'):
                            escolhaGuerreiro = input("Você selecinou a classe Guerreiro, tem certeza disso?\nR: ")
                            if(escolhaGuerreiro == 'Sim') or (escolhaGuerreiro == 'sim'):
                                print("Você escolheu Guerreiro!")
                                escolha_Nome_Guerreiro = input("Agora que você escolheu sua classe. Me diga, qual seu nome?\nR: ")
                                certeza_Nome_Guerreiro = input("Tem certeza de seu nome?\n- ")
                            if(certeza_Nome_Guerreiro == 'nao') or (certeza_Nome_Guerreiro == 'não') or (certeza_Nome_Guerreiro == 'Não') or (certeza_Nome_Guerreiro == 'Nao'):
                                escolha_Nome_Guerreiro = input("Então qual seu nome?\n- ")
                                certeza_Nome_Guerreiro = input("Tem certeza de seu nome?\n- ")
                                certeza_absoluta = input("Ta, mas você tem CERTEZA ABSOLUTA?\n R: ")
                            if(certeza_Nome_Guerreiro == 'Sim') or (certeza_Nome_Guerreiro == 'sim') or (certeza_Nome_Guerreiro == 'SIM'):
                                    inicio_Jogo_Guerreiro = input(f'Pois bem.\nSeja Muito bem vindo(a) {escolha_Nome_Guerreiro} ao Mundo de Vesquer!!!!!')
                                    retornoInfo = retornoInfo - 1
                                    if(inicio_Jogo_Guerreiro == "") or (inicio_Jogo_Guerreiro != ""):
                                        print("--------------------")
                                        #Escolher mapa do Guerreiro
                                        while(decisao_mapa_guerreiro == 1) or (certeza_mapa_guerreiro == 'Não') or (inicio_Jogo_Guerreiro == "") or (inicio_Jogo_Guerreiro != ""):
                                            print("Entre os mais bravos Guerreiros de Vesquer, inúmeros começaram sua jornada em cidades simples, ao todos aos Guerreiros temos 4 indicações de lugares iniciais para se começar.")
                                            escolha_mapa_Guerreiro = input("Entre as 4 opções, temos:\n- Garex\n- Sebix\n- Tequest\n- Ryugar\nGostaria de obter informações sobre algum mapa, ou apenas escolher qualquer mapa e iniciar sua jornada?\nCaso, queira obter informações, digite o nome do mapa, caso contrário, tecle Enter, que o menu de seleção vai aparecer.\n- ")
                                            if(escolha_mapa_Guerreiro == 'Garex'):
                                                print("Garex: O lar dos indomáveis Vikings, um povo onde se vive a base da caça e a brutalidade reina, desde pequeno são treinados para se adaptar e matar sem compaixão seus inimigos.")
                                                decisao_mapa_guerreiro_garex = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                                if(decisao_mapa_guerreiro_garex == "") or (escolha_mapa_Guerreiro == ""):
                                                            mapa_escolhido_guerreiro = input(f"Então meu caro {escolha_Nome_Guerreiro}, qual será sua nação de origem?\n- Garex\n- Sebix\n- Tequest\n- Ryugar\nEscreva o nome do mapa:\n")
                                                            if(mapa_escolhido_guerreiro == 'Garex') or (mapa_escolhido_guerreiro == 'Tequest') or (mapa_escolhido_guerreiro == 'Sebix') or (mapa_escolhido_guerreiro == 'Ryugar'):
                                                                    certeza_mapa_guerreiro = input(f"Você tem certeza da escolha {mapa_escolhido_guerreiro}?\nSim ou Não\n- ")
                                                                    if(certeza_mapa_guerreiro == 'Sim') or (certeza_mapa_guerreiro == 'sim'):
                                                                        print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Guerreiro} ao mundo de Vesquer, no reino de {mapa_escolhido_guerreiro}!")
                                                                        inicio_garex_guerreiro = input("Sua jornada, está apenas começando.....")
                                                                        break
                                            if(escolha_mapa_Guerreiro == ""):
                                                        mapa_escolhido_guerreiro = input(f"Então meu caro {escolha_Nome_Guerreiro}, qual será sua nação de origem?\n- Garex\n- Sebix\n- Tequest\n- Ryugar\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_guerreiro == 'Garex') or (mapa_escolhido_guerreiro == 'Tequest') or (mapa_escolhido_guerreiro == 'Sebix') or (mapa_escolhido_guerreiro == 'Ryugar'):
                                                                    certeza_mapa_guerreiro = input(f"Você tem certeza da escolha {mapa_escolhido_guerreiro}?\nSim ou Não\n- ")
                                                                    if(certeza_mapa_guerreiro == 'Sim') or (certeza_mapa_guerreiro == 'sim'):
                                                                        print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Guerreiro} ao mundo de Vesquer, no reino de {mapa_escolhido_guerreiro}!")
                                                                        inicio_garex_guerreiro = input("Sua jornada, está apenas começando.....")
                                                                        break
                                            if(escolha_mapa_Guerreiro == 'Sebix'):
                                                print("Sebix: O país da guerra, onde todos os recém-nascidos, por conta das suas gerações passadas estarem em constante guerra, já nascem com tendências a perseguir o caminho da batalha, um país onde apenas os fortes sobrevivem.")
                                                decisao_mapa_guerreiro = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                                if(decisao_mapa_guerreiro == ""):
                                                            mapa_escolhido_guerreiro = input(f"Então meu caro {escolha_Nome_Guerreiro}, qual será sua nação de origem?\n- Garex\n- Sebix\n- Tequest\n- Ryugar\nEscreva o nome do mapa:\n")
                                                            if(mapa_escolhido_guerreiro == 'Garex') or (mapa_escolhido_guerreiro == 'Tequest') or (mapa_escolhido_guerreiro == 'Sebix') or (mapa_escolhido_guerreiro == 'Ryugar'):
                                                                    certeza_mapa_guerreiro = input(f"Você tem certeza da escolha {mapa_escolhido_guerreiro}?\nSim ou Não\n- ")
                                                                    if(certeza_mapa_guerreiro == 'Sim') or (certeza_mapa_guerreiro == 'sim'):
                                                                        print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Guerreiro} ao mundo de Vesquer, no reino de {mapa_escolhido_guerreiro}!")
                                                                        inicio_garex_guerreiro = input("Sua jornada, está apenas começando.....")
                                                                        break
                                            if(escolha_mapa_Guerreiro == ""):
                                                        mapa_escolhido_guerreiro = input(f"Então meu caro {escolha_Nome_Guerreiro}, qual será sua nação de origem?\n- Garex\n- Sebix\n- Tequest\n- Ryugar\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_guerreiro == 'Garex') or (mapa_escolhido_guerreiro == 'Tequest') or (mapa_escolhido_guerreiro == 'Sebix') or (mapa_escolhido_guerreiro == 'Ryugar'):
                                                                    certeza_mapa_guerreiro = input(f"Você tem certeza da escolha {mapa_escolhido_guerreiro}?\nSim ou Não\n- ")
                                                                    if(certeza_mapa_guerreiro == 'Sim') or (certeza_mapa_guerreiro == 'sim'):
                                                                        print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Guerreiro} ao mundo de Vesquer, no reino de {mapa_escolhido_guerreiro}!")
                                                                        inicio_garex_guerreiro = input("Sua jornada, está apenas começando.....")
                                                                        break
                                            if(escolha_mapa_Guerreiro == 'Ryugar'):
                                                print("Ryugar: Onde inúmeros guerreiros escolhem descansar após anos de batalha, o lar de vários tenentes e generais, que em seu ápice eram capazes de acabar com um país sozinhos, os nascidos neste lugar já nascem vindo de familiares militares, e com uma enorme carga de expectativa em cima de si. ")
                                                decisao_mapa_guerreiro = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                                if(decisao_mapa_guerreiro == ""):
                                                            mapa_escolhido_guerreiro = input(f"Então meu caro {escolha_Nome_Guerreiro}, qual será sua nação de origem?\n- Garex\n- Sebix\n- Tequest\n- Ryugar\nEscreva o nome do mapa:\n")
                                                            if(mapa_escolhido_guerreiro == 'Garex') or (mapa_escolhido_guerreiro == 'Tequest') or (mapa_escolhido_guerreiro == 'Sebix') or (mapa_escolhido_guerreiro == 'Ryugar'):
                                                                    certeza_mapa_guerreiro = input(f"Você tem certeza da escolha {mapa_escolhido_guerreiro}?\nSim ou Não\n- ")
                                                                    if(certeza_mapa_guerreiro == 'Sim') or (certeza_mapa_guerreiro == 'sim'):
                                                                        print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Guerreiro} ao mundo de Vesquer, no reino de {mapa_escolhido_guerreiro}!")
                                                                        inicio_garex_guerreiro = input("Sua jornada, está apenas começando.....")
                                                                        break
                                            if(escolha_mapa_Guerreiro == ""):
                                                        mapa_escolhido_guerreiro = input(f"Então meu caro {escolha_Nome_Guerreiro}, qual será sua nação de origem?\n- Garex\n- Sebix\n- Tequest\n- Ryugar\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_guerreiro == 'Garex') or (mapa_escolhido_guerreiro == 'Tequest') or (mapa_escolhido_guerreiro == 'Sebix') or (mapa_escolhido_guerreiro == 'Ryugar'):
                                                                    certeza_mapa_guerreiro = input(f"Você tem certeza da escolha {mapa_escolhido_guerreiro}?\nSim ou Não\n- ")
                                                                    if(certeza_mapa_guerreiro == 'Sim') or (certeza_mapa_guerreiro == 'sim'):
                                                                        print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Guerreiro} ao mundo de Vesquer, no reino de {mapa_escolhido_guerreiro}!")
                                                                        inicio_garex_guerreiro = input("Sua jornada, está apenas começando.....")
                                                                        break
                                            if(escolha_mapa_Guerreiro == 'Tequest'):
                                                print("Tequest: Uma cidade abandonada pela sociedade, onde nasce aqueles que precisam lutar para sobreviver, aqueles que nascem em um ambiente tão pobre e escasso de alimentos possuem apenas dois caminhos, ou ser o mais forte para sobreviver, ou se deixar vencer e aceitar o fim perante os que desejam ser os mais fortes. ")
                                                decisao_mapa_guerreiro = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                                if(decisao_mapa_guerreiro == ""):
                                                            mapa_escolhido_guerreiro = input(f"Então meu caro {escolha_Nome_Guerreiro}, qual será sua nação de origem?\n- Garex\n- Sebix\n- Tequest\n- Ryugar\nEscreva o nome do mapa:\n")
                                                            if(mapa_escolhido_guerreiro == 'Garex') or (mapa_escolhido_guerreiro == 'Tequest') or (mapa_escolhido_guerreiro == 'Sebix') or (mapa_escolhido_guerreiro == 'Ryugar'):
                                                                    certeza_mapa_guerreiro = input(f"Você tem certeza da escolha {mapa_escolhido_guerreiro}?\nSim ou Não\n- ")
                                                                    if(certeza_mapa_guerreiro == 'Sim') or (certeza_mapa_guerreiro == 'sim'):
                                                                        print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Guerreiro} ao mundo de Vesquer, no reino de {mapa_escolhido_guerreiro}!")
                                                                        inicio_garex_guerreiro = input("Sua jornada, está apenas começando.....")
                                                                        break
                                            if(escolha_mapa_Guerreiro == ""):
                                                        mapa_escolhido_guerreiro = input(f"Então meu caro {escolha_Nome_Guerreiro}, qual será sua nação de origem?\n- Garex\n- Sebix\n- Tequest\n- Ryugar\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_guerreiro == 'Garex') or (mapa_escolhido_guerreiro == 'Tequest') or (mapa_escolhido_guerreiro == 'Sebix') or (mapa_escolhido_guerreiro == 'Ryugar'):
                                                                    certeza_mapa_guerreiro = input(f"Você tem certeza da escolha {mapa_escolhido_guerreiro}?\nSim ou Não\n- ")
                                                                    if(certeza_mapa_guerreiro == 'Sim') or (certeza_mapa_guerreiro == 'sim'):
                                                                        print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Guerreiro} ao mundo de Vesquer, no reino de {mapa_escolhido_guerreiro}!")
                                                                        inicio_garex_guerreiro = input("Sua jornada, está apenas começando.....")
                                                                        break
                #Escolha de classe Arqueiro
                if(escolhaClasse == 'Arqueiro') or (escolhaClasse == 'arqueiro'):
                            escolhaArqueiro = input("Você selecinou a classe Arqueiro, tem certeza disso?\nR: ")
                            if(escolhaArqueiro == 'Sim') or (escolhaArqueiro == 'sim'):
                                print("Você escolheu Arqueiro!")
                                escolha_Nome_Arqueiro = input("Agora que você escolheu sua classe. Me diga, qual seu nome?\nR: ")
                                certeza_Nome_Arqueiro = input("Tem certeza de seu nome?\n- ")
                            if(certeza_Nome_Arqueiro == 'nao') or (certeza_Nome_Arqueiro == 'não') or (certeza_Nome_Arqueiro == 'Não') or (certeza_Nome_Arqueiro == 'Nao'):
                                escolha_Nome_Arqueiro = input("Então qual seu nome?\n- ")
                                certeza_Nome_Arqueiro = input("Tem certeza de seu nome?\n- ")
                                certeza_absoluta = input("Ta, mas você tem CERTEZA ABSOLUTA?\n R: ")
                            if(certeza_Nome_Arqueiro == 'Sim') or (certeza_Nome_Arqueiro == 'sim') or (certeza_Nome_Arqueiro == 'SIM'):
                                        inicio_Jogo_Arqueiro = input(f'Pois bem.\nSeja Muito bem vindo(a) {escolha_Nome_Arqueiro} ao Mundo de Vesquer!!!!!')
                                        retornoInfo = retornoInfo - 1
                                        if(inicio_Jogo_Arqueiro == "") or (inicio_Jogo_Arqueiro != ""):
                                            print("--------------------")
                                            #Escolher mapa do Arqueiro
                                            print("Entre os mais bravos Arqueiros de Vesquer, inúmeros começaram sua jornada em cidades simples, ao todos aos Arqueiros temos 4 indicações de lugares iniciais para se começar.")
                                            escolha_mapa_Arqueiro = input("Entre as 4 opções, temos:\n- Talibur \n- Sirgex \n- Polux \n- Pleques \nGostaria de obter informações sobre algum mapa, ou apenas escolher qualquer mapa e iniciar sua jornada?\nCaso, queira obter informações, digite o nome do mapa, caso contrário, tecle Enter, que o menu de seleção vai aparecer.\n- ")
                                            if(escolha_mapa_Arqueiro == 'Talibur'):
                                                print("Talibur: O lar dos nobres e humildes que uma vez já foram os maiores atiradores entre o povo Élfico, cujo nome, há tanto tempo foi esquecido, abandonaram a vida de lutas e batalhas, para viver pacificamente, ainda se tem vestigios de suas lutas em seus corpos, e apenas desejam viver pacificamente, vivendo de contar suas histórias e auxiliar viajantes em suas aventuras. ")
                                                decisao_mapa_Arqueiro = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                                if(decisao_mapa_Arqueiro == "") or (escolha_mapa_Arqueiro == ""):
                                                            mapa_escolhido_arqueiro = input(f"Então meu caro {escolha_Nome_Arqueiro}, qual será sua nação de origem?\n- Talibur\n- Sirgex\n- Polux\n- Pleques\nEscreva o nome do mapa:\n")
                                                            if(mapa_escolhido_arqueiro == 'Talibur') or (mapa_escolhido_arqueiro == 'Sirgex') or (mapa_escolhido_arqueiro == 'Polux') or (mapa_escolhido_arqueiro == 'Pleques'):
                                                                    certeza_mapa_arqueiro = input(f"Você tem certeza da escolha {mapa_escolhido_arqueiro}?\nSim ou Não\n- ")
                                                                    if(certeza_mapa_arqueiro == 'Sim') or (certeza_mapa_arqueiro == 'sim'):
                                                                        print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Arqueiro} ao mundo de Vesquer, no reino de {mapa_escolhido_arqueiro}!")
                                                                        inicio_arqueiro = input("Sua jornada, está apenas começando.....")
                                                                        break
                                        if(escolha_mapa_Arqueiro == ""):
                                                        mapa_escolhido_arqueiro = input(f"Então meu caro {escolha_Nome_Arqueiro}, qual será sua nação de origem?\n- Talibur\n- Sirgex\n- Polux\n- Pleques\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_arqueiro == 'Talibur') or (mapa_escolhido_arqueiro == 'Sirgex') or (mapa_escolhido_arqueiro == 'Polux') or (mapa_escolhido_arqueiro == 'Pleques'):
                                                                certeza_mapa_arqueiro = input(f"Você tem certeza da escolha {mapa_escolhido_arqueiro}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_arqueiro == 'Sim') or (certeza_mapa_arqueiro == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Arqueiro} ao mundo de Vesquer, no reino de {mapa_escolhido_arqueiro}!")
                                                                    inicio_arqueiro = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Arqueiro == 'Sirgex'):
                                            print("Sirgex: O que falar da terra onde os Elfos vivem em união com todos os animais, em que é possível perceber que os Elfos criaram uma conexão tão forte com o reino animal, que dizem que eles conseguem conversar através de pensamentos, através de magias que são atualmente desoconhecidas para o restante do mundo.  ")
                                            decisao_mapa_Arqueiro = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                            if(decisao_mapa_Arqueiro == "") or (escolha_mapa_Arqueiro == ""):
                                                        mapa_escolhido_arqueiro = input(f"Então meu caro {escolha_Nome_Arqueiro}, qual será sua nação de origem?\n- Talibur\n- Sirgex\n- Polux\n- Pleques\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_arqueiro == 'Talibur') or (mapa_escolhido_arqueiro == 'Sirgex') or (mapa_escolhido_arqueiro == 'Polux') or (mapa_escolhido_arqueiro == 'Pleques'):
                                                                certeza_mapa_arqueiro = input(f"Você tem certeza da escolha {mapa_escolhido_arqueiro}\nSim ou Não\n- ")
                                                                if(certeza_mapa_arqueiro == 'Sim') or (certeza_mapa_arqueiro == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Arqueiro} ao mundo de Vesquer, no reino de {mapa_escolhido_arqueiro}!")
                                                                    inicio_arqueiro = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Arqueiro == ""):
                                                        mapa_escolhido_arqueiro = input(f"Então meu caro {escolha_Nome_Arqueiro}, qual será sua nação de origem?\n- Talibur\n- Sirgex\n- Polux\n- Pleques\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_arqueiro == 'Talibur') or (mapa_escolhido_arqueiro == 'Sirgex') or (mapa_escolhido_arqueiro == 'Polux') or (mapa_escolhido_arqueiro == 'Pleques'):
                                                                certeza_mapa_arqueiro = input(f"Você tem certeza da escolha {mapa_escolhido_arqueiro}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_arqueiro == 'Sim') or (certeza_mapa_arqueiro == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Arqueiro} ao mundo de Vesquer, no reino de {mapa_escolhido_arqueiro}!")
                                                                    inicio_arqueiro = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Arqueiro == 'Polux'):
                                            print("Polux:  Nação dos que se dedicam a venerar o Deus poderoso que criou o mundo de Vesquer, que apenas os antigos sabem pronunciar seu nome, vindo de uma lingua antiga, os que nascem desta terra, tendem a dedicar suas vidas a elevar seu espirito e lutam em nome de seu Deus, para que um dia possam se tornar dignos de repousar ao seu lado. ")
                                            decisao_mapa_Arqueiro = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                            if(decisao_mapa_Arqueiro == "") or (escolha_mapa_Arqueiro == ""):
                                                        mapa_escolhido_arqueiro = input(f"Então meu caro {escolha_Nome_Arqueiro}, qual será sua nação de origem?\n- Talibur\n- Sirgex\n- Polux\n- Pleques\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_arqueiro == 'Talibur') or (mapa_escolhido_arqueiro == 'Sirgex') or (mapa_escolhido_arqueiro == 'Polux') or (mapa_escolhido_arqueiro == 'Pleques'):
                                                                certeza_mapa_arqueiro = input(f"Você tem certeza da escolha {mapa_escolhido_arqueiro}\nSim ou Não\n- ")
                                                                if(certeza_mapa_arqueiro == 'Sim') or (certeza_mapa_arqueiro == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Arqueiro} ao mundo de Vesquer, no reino de {mapa_escolhido_arqueiro}!")
                                                                    inicio_arqueiro = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Arqueiro == ""):
                                                        mapa_escolhido_arqueiro = input(f"Então meu caro {escolha_Nome_Arqueiro}, qual será sua nação de origem?\n- Talibur\n- Sirgex\n- Polux\n- Pleques\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_arqueiro == 'Talibur') or (mapa_escolhido_arqueiro == 'Sirgex') or (mapa_escolhido_arqueiro == 'Polux') or (mapa_escolhido_arqueiro == 'Pleques'):
                                                                certeza_mapa_arqueiro = input(f"Você tem certeza da escolha {mapa_escolhido_arqueiro}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_arqueiro == 'Sim') or (certeza_mapa_arqueiro == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Arqueiro} ao mundo de Vesquer, no reino de {mapa_escolhido_arqueiro}!")
                                                                    inicio_arqueiro = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Arqueiro == 'Pleques'):
                                            print("Pleques: Um povo de élfos que se dedicam a viver pacificamente, e viver uma vida simples, vivendo do cultivo de ervas e frutas, usam de sua magia antiga, apenas para facilitar sua vida, pois não buscam mais entrar em batalhas, e os poucos que nascem com esta vontade nesta terra, tendem a deixar sua terra assim que tomam ciência de onde vivem, deixando apenas Elfos que buscam viver com tranquilidade.")
                                            decisao_mapa_Arqueiro = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                            if(decisao_mapa_Arqueiro == "") or (escolha_mapa_Arqueiro == ""):
                                                        mapa_escolhido_arqueiro = input(f"Então meu caro {escolha_Nome_Arqueiro}, qual será sua nação de origem?\n- Talibur\n- Sirgex\n- Polux\n- Pleques\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_arqueiro == 'Talibur') or (mapa_escolhido_arqueiro == 'Sirgex') or (mapa_escolhido_arqueiro == 'Polux') or (mapa_escolhido_arqueiro == 'Pleques'):
                                                                certeza_mapa_arqueiro = input(f"Você tem certeza da escolha {mapa_escolhido_arqueiro}\nSim ou Não\n- ")
                                                                if(certeza_mapa_arqueiro == 'Sim') or (certeza_mapa_arqueiro == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Arqueiro} ao mundo de Vesquer, no reino de {mapa_escolhido_arqueiro}!")
                                                                    inicio_arqueiro = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Arqueiro == ""):
                                                        mapa_escolhido_arqueiro = input(f"Então meu caro {escolha_Nome_Arqueiro}, qual será sua nação de origem?\n- Talibur\n- Sirgex\n- Polux\n- Pleques\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_arqueiro == 'Talibur') or (mapa_escolhido_arqueiro == 'Sirgex') or (mapa_escolhido_arqueiro == 'Polux') or (mapa_escolhido_arqueiro == 'Pleques'):
                                                                certeza_mapa_arqueiro = input(f"Você tem certeza da escolha {mapa_escolhido_arqueiro}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_arqueiro == 'Sim') or (certeza_mapa_arqueiro == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Arqueiro} ao mundo de Vesquer, no reino de {mapa_escolhido_arqueiro}!")
                                                                    inicio_arqueiro = input("Sua jornada, está apenas começando.....")
                                                                    break
                #Escolha de classe Tank
                if(escolhaClasse == 'Tank') or (escolhaClasse == 'tank'):
                            escolhaTank = input("Você selecinou a classe Tank, tem certeza disso?\nR: ")
                            if(escolhaTank == 'Sim') or (escolhaTank == 'sim'):
                                print("Você escolheu Tank!")
                                escolha_Nome_Tank = input("Agora que você escolheu sua classe. Me diga, qual seu nome?\nR: ")
                                certeza_Nome_Tank = input("Tem certeza de seu nome?\n- ")
                            if(certeza_Nome_Tank == 'nao') or (certeza_Nome_Tank == 'não') or (certeza_Nome_Tank == 'Não') or (certeza_Nome_Tank == 'Nao'):
                                escolha_Nome_Tank = input("Então qual seu nome?\n- ")
                                certeza_Nome_Tank = input("Tem certeza de seu nome?\n- ")
                                certeza_absoluta = input("Ta, mas você tem CERTEZA ABSOLUTA?\n R: ")
                            if(certeza_Nome_Tank == 'Sim') or (certeza_Nome_Tank == 'sim') or (certeza_Nome_Tank == 'SIM'):
                                        inicio_Jogo_Tank = input(f'Pois bem.\nSeja Muito bem vindo(a) {escolha_Nome_Tank} ao Mundo de Vesquer!!!!!')
                                        retornoInfo = retornoInfo - 1
                                        if(inicio_Jogo_Tank == "") or (inicio_Jogo_Tank != ""):
                                            print("--------------------")
                                        #Escolher mapa do Tank
                                        print("Entre os mais bravos Lutadores de Vesquer, inúmeros começaram sua jornada em cidades simples temos 4 indicações de lugares iniciais para se começar.")
                                        escolha_mapa_Tank = input("Entre as 4 opções, temos:\n- Tankolver \n- Braltes \n- Tilquer \n- Quelter \nGostaria de obter informações sobre algum mapa, ou apenas escolher qualquer mapa e iniciar sua jornada?\nCaso, queira obter informações, digite o nome do mapa, caso contrário, tecle Enter, que o menu de seleção vai aparecer.\n- ")
                                        if(escolha_mapa_Tank == 'Tankolver'):
                                            print("Tankolver: Lar dos maiores humanos de Vesquer, onde a pessoa mais baixa deve se ter por 2metros de altura, todos nesta cidade são amantes de coração por lutas e batalhas, constantemente estão testando seus limites. Todo dia se tem por constante torneios e lutas para decidir os maios fortes, e viver de riquezas ganhas, além de todos compartilhar a paixão pela batalha.")
                                            decisao_mapa_Tank = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                            if(decisao_mapa_Tank == "") or (escolha_mapa_Tank == ""):
                                                        mapa_escolhido_tank = input(f"Então meu caro {escolha_Nome_Tank}, qual será sua nação de origem?\n- Quelter\n- Tilquer\n- Braltes\n- Tankolver\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_tank == 'Quelter') or (mapa_escolhido_tank == 'Tilquer') or (mapa_escolhido_tank == 'Braltes') or (mapa_escolhido_tank == 'Tankolver'):
                                                                certeza_mapa_tank = input(f"Você tem certeza da escolha {mapa_escolhido_tank}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_tank == 'Sim') or (certeza_mapa_tank == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Tank} ao mundo de Vesquer, no reino de {mapa_escolhido_tank}!")
                                                                    inicio_tank = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Tank == ""):
                                                        mapa_escolhido_tank = input(f"Então meu caro {escolha_Nome_Tank}, qual será sua nação de origem?\n- Quelter\n- Tilquer\n- Braltes\n- Tankolver\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_tank == 'Quelter') or (mapa_escolhido_tank == 'Tilquer') or (mapa_escolhido_tank == 'Braltes') or (mapa_escolhido_tank == 'Tankolver'):
                                                                certeza_mapa_tank = input(f"Você tem certeza da escolha {mapa_escolhido_tank}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_tank == 'Sim') or (certeza_mapa_tank == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Tank} ao mundo de Vesquer, no reino de {mapa_escolhido_tank}!")
                                                                    inicio_tank = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Tank == 'Braltes'):
                                            print("Braltes: Nação dos mais destemidos e que possuem os melhores ferreiros, uma nação de pessoas dispostas a entrar na linha de frente com todas as suas frças, que com o tempo desenvolveram habilidades para se fortificar cada vez mais, conseguindo sempre aprimorar suas armaduras, visto que foram ensinados a lutarem e cuidar de suas próprias armaduras, dizem que ja ouve uma época em que existiu um guerreiro que ultrapassou 3m de altura, e foi o melhor ferreiro que quando construiu sua armadura, era imperável, ninguem conseguia ultrapassar sua defesa. Hoje em dia, muitos veem a esta terra para se mostrarem merecedores de um dia serem comparados a este bravo guerreiro.")
                                            decisao_mapa_Tank = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                            if(decisao_mapa_Tank == "") or (escolha_mapa_Tank == ""):
                                                        mapa_escolhido_tank = input(f"Então meu caro {escolha_Nome_Tank}, qual será sua nação de origem?\n- Quelter\n- Tilquer\n- Braltes\n- Tankolver\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_tank == 'Quelter') or (mapa_escolhido_tank == 'Tilquer') or (mapa_escolhido_tank == 'Braltes') or (mapa_escolhido_tank == 'Tankolver'):
                                                                certeza_mapa_tank = input(f"Você tem certeza da escolha {mapa_escolhido_tank}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_tank == 'Sim') or (certeza_mapa_tank == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Tank} ao mundo de Vesquer, no reino de {mapa_escolhido_tank}!")
                                                                    inicio_tank = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Tank == ""):
                                                        mapa_escolhido_tank = input(f"Então meu caro {escolha_Nome_Tank}, qual será sua nação de origem?\n- Quelter\n- Tilquer\n- Braltes\n- Tankolver\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_tank == 'Quelter') or (mapa_escolhido_tank == 'Tilquer') or (mapa_escolhido_tank == 'Braltes') or (mapa_escolhido_tank == 'Tankolver'):
                                                                certeza_mapa_tank = input(f"Você tem certeza da escolha {mapa_escolhido_tank}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_tank == 'Sim') or (certeza_mapa_tank == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Tank} ao mundo de Vesquer, no reino de {mapa_escolhido_tank}!")
                                                                    inicio_tank = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Tank == 'Tilquer'):
                                            print("Tilquer: Lar dos brutos e imparáveis, um povo que anseia por batalhas a todo momento, visto que após a grande guerra, foram eles quem procuraram posteriormente motivos para duelar contra as nações, pois estão constantemente tentando se provar a nação mais poderosa de Vesquer, anseiam por pessoas que o possam os derrotar em batalha.")
                                            decisao_mapa_Tank = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                            if(decisao_mapa_Tank == "") or (escolha_mapa_Tank == ""):
                                                        mapa_escolhido_tank = input(f"Então meu caro {escolha_Nome_Tank}, qual será sua nação de origem?\n- Quelter\n- Tilquer\n- Braltes\n- Tankolver\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_tank == 'Quelter') or (mapa_escolhido_tank == 'Tilquer') or (mapa_escolhido_tank == 'Braltes') or (mapa_escolhido_tank == 'Tankolver'):
                                                                certeza_mapa_tank = input(f"Você tem certeza da escolha {mapa_escolhido_tank}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_tank == 'Sim') or (certeza_mapa_tank == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Tank} ao mundo de Vesquer, no reino de {mapa_escolhido_tank}!")
                                                                    inicio_tank = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Tank == ""):
                                                        mapa_escolhido_tank = input(f"Então meu caro {escolha_Nome_Tank}, qual será sua nação de origem?\n- Quelter\n- Tilquer\n- Braltes\n- Tankolver\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_tank == 'Quelter') or (mapa_escolhido_tank == 'Tilquer') or (mapa_escolhido_tank == 'Braltes') or (mapa_escolhido_tank == 'Tankolver'):
                                                                certeza_mapa_tank = input(f"Você tem certeza da escolha {mapa_escolhido_tank}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_tank == 'Sim') or (certeza_mapa_tank == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Tank} ao mundo de Vesquer, no reino de {mapa_escolhido_tank}!")
                                                                    inicio_tank = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Tank == 'Quelter'):
                                            print("Quelter: Deste lugar nasce, os gigantes e poderes construtores, que utilizam de sua tamanha magnitude em força e tamanho para construir os mais belos fortes e esculturas para todo o reino de Vesquer, constantemente um povo pacifico, que nenhum outro reine há de se pensar em guerrear contra, visto que suas construções e defesas ultrapassam a de qualquer nação, até mesmo porque, toda nação utiliza de armas, que vieram de Quelter.")
                                            decisao_mapa_Tank = input("Tecle 'Enter' para anvaçar para a tela de 'Escolher mapa'\n")
                                            if(decisao_mapa_Tank == "") or (escolha_mapa_Tank == ""):
                                                        mapa_escolhido_tank = input(f"Então meu caro {escolha_Nome_Tank}, qual será sua nação de origem?\n- Quelter\n- Tilquer\n- Braltes\n- Tankolver\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_tank == 'Quelter') or (mapa_escolhido_tank == 'Tilquer') or (mapa_escolhido_tank == 'Braltes') or (mapa_escolhido_tank == 'Tankolver'):
                                                                certeza_mapa_tank = input(f"Você tem certeza da escolha {mapa_escolhido_tank}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_tank == 'Sim') or (certeza_mapa_tank == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Tank} ao mundo de Vesquer, no reino de {mapa_escolhido_tank}!")
                                                                    inicio_tank = input("Sua jornada, está apenas começando.....")
                                                                    break
                                        if(escolha_mapa_Tank == ""):
                                                        mapa_escolhido_tank = input(f"Então meu caro {escolha_Nome_Tank}, qual será sua nação de origem?\n- Quelter\n- Tilquer\n- Braltes\n- Tankolver\nEscreva o nome do mapa:\n")
                                                        if(mapa_escolhido_tank == 'Quelter') or (mapa_escolhido_tank == 'Tilquer') or (mapa_escolhido_tank == 'Braltes') or (mapa_escolhido_tank == 'Tankolver'):
                                                                certeza_mapa_tank = input(f"Você tem certeza da escolha {mapa_escolhido_tank}?\nSim ou Não\n- ")
                                                                if(certeza_mapa_tank == 'Sim') or (certeza_mapa_tank == 'sim'):
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Tank} ao mundo de Vesquer, no reino de {mapa_escolhido_tank}!")
                                                                    iinicio_tank = input("Sua jornada, está apenas começando.....")
                                                                    break
                                                                if(certeza_mapa_tank == 'Não') or (certeza_mapa_tank == 'Nao') or (certeza_mapa_tank == 'nao') or (certeza_mapa_tank == 'não'):
                                                                    certeza_tank = input("Então qual mapa?\nR: ")
                                                                    certeza_absoluta = input(f"Ta, mas você tem certeza de que é {certeza_tank}?\nR: ")
                                                                    print(f"Então tudo bem!\nEu oficialmente, lhe desejo as boas vindas {escolha_Nome_Tank} ao mundo de Vesquer, no reino de {mapa_escolhido_tank}!")
                                                                    inicio_tank = input("Sua jornada, está apenas começando.....")
                                                                    break



