from time import sleep
from random import randint

introducao = '  O navio pirata "Maré Negra" corta as águas revoltas em busca de tesouros escondidos nos destroços \nde naufrágios. Sob o comando do temido Capitão Dante Sangueiro, a tripulação embarca em aventuras \nousadas e perigosas. Entretanto, quando um dos tripulantes é encontrado assassinado em uma noite \ntempestuosa, o navio se torna palco de um mistério intrigante. \n   O membro assassinado é o segundo-mestre Jonas Barba-Ruiva, conhecido por sua astúcia. Seu corpo \né descoberto no convés. Com o caos se instaurando entre a tripulação, a tensão entre os membros aumenta.\nCada um deles tem seus próprios motivos e histórias que poderiam estar relacionadas ao crime. \n  VOCÊ, Capitão Dante Sangueiro, está sentado  junto aos tripulantes restantes na mesa de reuniões \ne precisa investigar profundamente, entender as motivações e segredos de seus companheiros, e desvendar \no mistério antes que a confiança no "Maré Negra" se desfaça e o caos se instale definitivamente.'

nomes = ['RITTA', 'SANTIAGO', 'TALIA', 'ULISSES', 'VITOR']

desc = [['\nRITTA "A Víbora" é a navegadora do "Maré Negra". Pequena e ágil, com olhos penetrantes e cabelos negros \nondulados, ela é conhecida por sua habilidade de traçar rotas em águas traiçoeiras e por seu conhecimento \nenciclopédico dos mapas antigos.\n', '\nInteligente e misteriosa, RITTA tem um temperamento frio e calculista. Sua lealdade ao Capitão \nDante é inquestionável, mas ela guarda muitos segredos, e há rumores de que possa ter um passado sombrio.\n', '\nRITTA busca um artefato lendário que acredita estar escondido em algum lugar do oceano, algo que lhe \nfoi prometido por um antigo mentor.\n'],
        ['\nSANTIAGO "Punho de Ferro" é o contramestre, responsável por manter a disciplina e a ordem a bordo. \nAlto e musculoso, com uma cicatriz que atravessa seu rosto, ele é uma presença intimidante e um \nlutador formidável.\n', '\nLeal e justo, mas implacável com aqueles que desafiam a autoridade do Capitão. SANTIAGO é respeitado \ne temido pela tripulação por sua força e sua habilidade com as armas.\n', '\nEle tem um senso profundo de honra e dever, devotado a proteger a tripulação e cumprir as ordens do \nCapitão Dante a qualquer custo.\n'], 
        ['\nTALIA "Olhos de Águia" é a atiradora do navio, famosa por sua precisão com a pistola e o mosquete. \nCom cabelos ruivos flamejantes e olhos azuis penetrantes, ela é uma figura imponente.\n', '\nTALIA é corajosa e determinada, com um espírito aventureiro e uma língua afiada. Ela é conhecida por \nsua bravura em combate e por sua habilidade de ver perigo a quilômetros de distância.\n', '\nEla procura vingança contra um navio mercante que massacrou sua antiga tripulação e deseja encontrar \njustiça pelos seus companheiros mortos.\n'], 
        ['\nULISSES "O Curandeiro" é o médico e o alquimista do "Maré Negra". Envolto em vestes gastas e com \ncabelos grisalhos presos em um rabo de cavalo, ele carrega consigo uma bolsa cheia de poções e remédios.\n', '\nSábio e tranquilo, ULISSES tem um temperamento paciente e é uma figura paternal para muitos na \ntripulação. Ele tem um vasto conhecimento de ervas e medicina, bem como uma compreensão profunda \ndas artes místicas.\n', '\nULISSES procura uma cura para uma doença misteriosa que aflige sua família em terras distantes, usando \nos recursos e os conhecimentos adquiridos em suas viagens.\n'],
        ['\nVITOR "O Sorridente" é o mestre de armas do "Maré Negra", responsável pelo treinamento e manutenção \ndas armas a bordo. Sempre visto com um sorriso astuto, ele é um espadachim habilidoso e um estrategista nato.\n', '\nCharme e astúcia são suas marcas registradas. VITOR é carismático e espirituoso, muitas vezes usando \nseu humor para desarmar situações tensas. Ele é extremamente leal ao Capitão Dante, mas é sabido que \ntem uma queda por apostas arriscadas.\n', '\nVITOR busca redenção por um erro do passado que custou a vida de seu irmão mais novo. Ele vê sua lealdade \nao Capitão e suas ações a bordo do "Maré Negra" como um caminho para reparar suas falhas.\n']]

dicas = [['l: "Você escutou Talia chorando sozinha em seu quarto quando o assassinato aconteceu e passou o dia com VITOR”', 'r: "Jonas e Talia tiveram uma discussão antes do assassinato"', 's: "Barba-ruiva encontrou um mapa de um tesouro lendário"', 't: "Estava tudo bem entre JONAS e TALIA”', 'u: "ULISSES passou o dia inteiro cuidando das feridas do Miguel”', 'v: "RITTA havia afiado a sua adaga alguns dias antes”'],
         ['l: "Você deu boa noite para TALIA enquanto ela subia na torre de vigia"', 'r: "RITTA viu SANTIAGO confrontando JONAS no dia do assassinato"', 's: "Jonas e Talia tiveram uma discussão antes do assassinato"', 't: "TALIA estava na torre de vigia durante a noite toda"', 'u: "SANTIAGO sempre foi duro com quem desafiasse a autoridade."', 'v: "VITOR estava junto com ULISSES arrumando o estoque de armamentos."'],
         ['l: "Você viu o corpo de JONAS com vários cortes"', 'r: "TALIA estava discutindo intensamente com JONAS pouco antes de ele ser encontrado morto"', 's: "SANTIAGO estava treinando junto com ULISSES"', 't: "Foi encontrada uma adaga de VITOR  próxima ao corpo de JONAS"', 'u: "JONAS era tripulante de um navio mercante no passado"', 'v: "Quando VITOR chegou no corpo, ULISSES já estava lá"'],
         ['l: "Você passou o dia limpando o navio junto com VITOR"', 'r: "RITTA passou o dia discutindo o próximo destino com TALIA"', 's: "JONAS havia encontrado uma planta misteriosa na última ilha em que visitaram"', 't: "ULISSES estava preparando uma poção"', 'u: "Um frasco de teste de ULISSES foi encontrado nos pertences de VITOR"', 'v: "VITOR estava limpando o ferrolho de alguns mosquetes"'],
         ['l: "JONAS sempre foi um homem que não gostava de correr riscos"', 'r: "RITTA, SANTIAGO e TALIA estavam comendo juntos na hora do assassinato"', 's: "VITOR queria fazer uma aposta arriscada"', 't: "VITOR e JONAS estavam discutindo intensamente na noite do assassinato"', 'u: "ULISSES estava lendo um diário de Don Yohan Collumbine"', 'v: "VITOR estava em seu quarto estudando os mapas"']]

motivacao = ['m: "RITTA busca um artefato lendário que acredita estar escondido em algum lugar do oceano, algo que lhe foi prometido por um antigo mentor."', 'm: "SANTIAGO é devotado a proteger a tripulação e cumprir as ordens do Capitão Dante a qualquer custo."', 'm: "TALIA procura vingança contra um navio mercante que massacrou sua antiga tripulação"', 'm: "ULISSES procura uma cura para uma doença misteriosa que aflige sua família em terras distantes"', 'm: "VITOR tem uma queda por apostas arriscadas"']

assassino = ['a: "RITTA matou JONAS"', 'a: "SANTIAGO matou JONAS"', 'a: "TALIA matou JONAS"', 'a: "ULISSES matou JONAS"', 'a: "VITOR matou JONAS"']

dedução = [['u -> s', 'l -> v ^ t ^ (~r)',  'm ^ s -> a'], ['l -> t ^ (~s)', 'v -> u', 'u ^ m ^ r -> a'], ['s -> u', 'u ^ m ^ r -> a ^ (~t)'], ['l -> v', 'r -> t', 't ^ s ^ m -> a ^ (~u)'], ['r -> s ^ t', 'm ^ s ^ l ^ t -> a']]

resposta = ['JONAS Barba-ruiva havia encontrado o mapa do tesouro lendário que RITTA almejava e não queria mostrá-lo para ela. \nEm um surto repentino, ela acaba matando-o com sua adaga', 'SANTIAGO havia escutado uma conversa entre JONAS Barba-ruiva e um ex-companheiro no convés para \nroubar o próximo tesouro do CAPITÃO. \nEnfurecido, ele parte pra cima de jonas e o mata. \nArrependido, tenta esconder o fato da tripulação', 'TALIA buscava vingança contra um navio mercante que massacrou sua antiga tripulação e, ao descobrir \nque JONAS era desse navio e não a informou disso, não teve piedade dele', 'JONAS Barba-ruiva havia encontrado uma planta misteriosa na última missão e decidiu dar de presente \npara ULISSES. \nEle não conhecia aquela planta, mas pelo cheiro doce decidiu fazer uma bebida e entregar para JONAS \nque adorava beber. \nQuando percebeu que a planta era venenosa e que havia matado o sub-comandante, já era tarde demais', 'VITOR tinha ouvido falar de uma passagem entre duas ilhas e que poderia conter diversos tesouros. \nSabendo que poderia ser uma armadilha, JONAS não podia permitir a campanha. \nIrritado por não poder realizar tal aposta e viver a aventura, VITOR mata JONAS com esperança de que \nninguém descobrisse']

sorteio = randint(0, len(dicas) - 1)
escolha = 0
chutar = True

def imprimirIntr():
    print('\n'+'=' * 45 + '  MISTÉRIO A BORDO  ' + '='*45)
    print('\n'+introducao+'\n')
    print('=' * 110)
    sleep(8)

def escolher():
    e = int(input('\n[0] Lembrar \n[1] Falar com RITTA "A Víbora" \n[2] Falar com SANTIAGO "Punho de Ferro" \n[3] Falar com TALIA "Olhos de Águia" \n[4] Falar com ULISSES "O Curandeiro" \n[5] Falar com VITOR "O Sorridente" \n[6] Concluir\n\nESCOLHA: '))
    if e in [1, 2, 3, 4, 5]:
        return opcao(e)
    elif e == 0:
        return imprimirEscolha(0, 0)
    elif e == 6:
        return confirmAcusar()
    else:
        print('ESCOLHA INVÁLIDA')
        return escolher()
    
def opcao(e):
    esc = e
    print('=' * 110)
    print(nomes[e - 1])
    opcao = int(input('\n[1] Descrição \n[2] Personalidade \n[3] Motivação \n[4] Dica \n\nESCOLHA: '))
    print('=' * 110)
    return imprimirEscolha(opcao, esc)

def imprimirEscolha(opcao, esc):
    if opcao in [1, 2, 3]:
        print(desc[esc - 1][opcao - 1] + '\n' + '=' * 110)
        sleep(3)

    elif opcao == 4:
        print('\n' + dicas[sorteio][esc] + '\n\n'+ '=' * 110)
        sleep(3) 

    elif opcao == 0:
        print('=' * 110 + '\n\n' + dicas[sorteio][esc] + '\n\n'+ '=' * 110)
        sleep(3)
    
    return True

def confirmAcusar():
    c = int(input('=' * 110 + '\n\n' + '[0] NÃO \n[1] SIM \n\nVOCÊ SÓ PODE ACUSAR UMA VEZ \nDESEJA MESMO FAZER ISSO? '))
    if c == 0:
        return True
    elif c == 1:
        return False
    else:
        print('OPÇÃO INVÁLIDA. DIGITE NOVAMENTE')
        return confirmAcusar()

def imprimirNomes():
    print('\n' + '=' * 110 + '\n')
    for i in range(len(nomes)):
        print(f'[{i + 1}] {nomes[i]}')

def acusar():
    chute = int(input('\nQUEM FOI O ASSASSINO? '))
    return verificarChute(chute)

def verificarChute(chute):
    print('\n' + '=' * 110)
    if chute == sorteio + 1:
        print('\nCORRETO! VOCÊ GANHOU!')
        sleep(2)
        return historiaFinal()
    else:
        print('\nERRADO!\n')
        sleep(2)
        print('\nVOCÊ EXPULSA A PESSOA ERRADA DA TRIPULAÇÃO E NÃO SABE DO CAOS QUE ESTÁ POR VIR\n')
        sleep(2)

def historiaFinal():
    print('\n' + '=' * 49 + '  DESFECHO  ' + '=' * 49 + '\n')
    print(resposta[sorteio])
    sleep(5)
    return imprimirDicas()

def imprimirDicas():
    print('\n' + '=' * 49 + '  RESPOSTA  ' + '=' * 49 + '\n')
    for dica in dicas[sorteio]:
        print(dica)
    print(motivacao[sorteio])
    print(assassino[sorteio])
    return imprimirResposta()

def imprimirResposta():
    print()
    for passo in dedução[sorteio]:
        print(passo)
    sleep(5)

imprimirIntr()
    
while chutar == True:
    chutar = escolher()

imprimirNomes()
acusar()


