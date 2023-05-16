tipos = ['Opções de tipos de vinho:','1: Tinto','2: Branco','3: Rosé','9: Sair']
tinto = ['Opções de vinho Tinto:','1: Cabernet Sauvignon R$100','2: Pinot Noir R$120','3: Tinto Malbec R$80','4: Tinto Merlot R$90','5: Tinto Syrah R$100','0: Voltar']
branco = ['Opções de vinho Branco:','1: Chardonnay R$80','2: Sauvignon Blanc R$70','3: Riesling R$90','4: Pinot Grigio R$60','0: Voltar']
rose = ['Opções de vinho Rosé:','1: Cabernet Franc R$70','2: Syrah R$80','3: Grenache R$60','0: Voltar']
escolha = 0
escolhaTinto = 0
escolhaBranco = 0
escolhaRose = 0
print('')


while True:
    try:

        #menu vinho tinto
        if(escolhaTinto == 1):
            print('inf 1')
            break 

        elif(escolhaTinto == 2):
            print('inf 2')
            break

        elif(escolhaTinto == 3):
            print('inf 3')
            break

        elif(escolhaTinto == 4):
            print('inf 4')
            break

        elif(escolhaTinto == 5):
            print('inf 5')
            break

        #menu vinho branco
        elif(escolhaBranco == 1):
            print('inf 1')
            break

        elif(escolhaBranco == 2):
            print('inf 2')
            break

        elif(escolhaBranco == 3):
            print('inf 3')
            break

        elif(escolhaBranco == 4):
            print('inf 4')
            break

        #menu vinho rose
        elif(escolhaRose == 1):
            print('inf 1')
            break
        elif(escolhaRose == 2):
            print('inf 2')
            break

        elif(escolhaRose == 3):
            print('inf 3')
            break
                                    
        #menu tipos
        elif (escolha == 0):
            for item in tipos:
                print(item)
            escolha = int(input('Escolha o tipo de vinho desejado: '))
            print('')

        elif(escolha == 1):
            for item in tinto:
                print(item)
            escolhaTinto = int(input('Escolha o vinho desejado: '))
            print('')
            if escolhaTinto == 0:
                escolha = 0

        elif(escolha == 2):
            for item in branco:
                print(item)
            escolhaBranco = int(input('Escolha o vinho desejado: '))
            print('')
            if escolhaBranco == 0:
                escolha = 0

        elif(escolha == 3):

            for item in rose:
                print(item)
            escolhaRose = int(input('Escolha o vinho desejado: '))
            print('')
            if escolhaRose == 0:
                escolha = 0

        elif(escolha == 9):
            break
        else:
            print('Opção inválida, tente novamente')
            print('')
            escolha = 0

    except Exception:
        print('')
        print('Algo deu errado, tente novamente:')
        print('')
        escolha = 0

print("Fim do programa")
print('')