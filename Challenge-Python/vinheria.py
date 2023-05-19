tipos = ['Opções de tipos de vinho:','1: Tinto','2: Branco','3: Rosé','8: Esvaziar carrinho','9: Sair']
tinto = ['Opções de vinho Tinto:','1: Cabernet Sauvignon R$100','2: Pinot Noir R$120','3: Tinto Malbec R$80','4: Tinto Merlot R$90','5: Tinto Syrah R$100','0: Voltar']
branco = ['Opções de vinho Branco:','1: Chardonnay R$80','2: Sauvignon Blanc R$70','3: Riesling R$90','4: Pinot Grigio R$60','0: Voltar']
rose = ['Opções de vinho Rosé:','1: Cabernet Franc R$70','2: Syrah R$80','3: Grenache R$60','0: Voltar']
escolha = 0
escolhaTinto = 0
escolhaBranco = 0
escolhaRose = 0
quantidade = 0
valorTotal = 0
quantidadeTotal = 0
confirmar = 0
msgQuantidade = "Insira a quantidade (valor negativo para retirar): "

#preços

#tinto

#1
CabernetSauvignon = 100

#2
PinotNoir = 120

#3
TintoMalbec = 80

#4
TintoMerlot = 90

#5
TintoSyrah = 100

#branco

#1
Chardonnay = 80

#2
SauvignonBlanc = 70

#3
Riesling = 90

#4
PinotGrigio = 60

#rose

#1
CabernetFranc = 70

#2
Syrah = 80

#3
Grenache = 60

print('')

def quantidadeCheck(quantidade):
    quantidade = int(input(msgQuantidade))
    if (quantidade > 10):
        quantidade = 0
        print('')
        print("Valor muito grande. Máximo: 10")
    return quantidade

def valor(valorTotal,quantidade, vinho):

    valorTotal = quantidade * vinho + valorTotal
    if (valorTotal < 0):
        valorTotal = 0
    print('')
    print(f"Valor total: {valorTotal}")
    return valorTotal


while True:
    try:
        #menu vinho tinto -----------
        if (quantidadeTotal < 0 or valorTotal < 0):
            quantidadeTotal = 0

        #1 CabernetSauvignon
        elif(escolhaTinto == 1):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, CabernetSauvignon)
            escolhaTinto = 0

        #2 PinotNoir
        elif(escolhaTinto == 2):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, PinotNoir)
            escolhaTinto = 0
            
        #3 TintoMalbec
        elif(escolhaTinto == 3):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, TintoMalbec)
            escolhaTinto = 0


        #4 TintoMerlot
        elif(escolhaTinto == 4):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, TintoMerlot)
            escolhaTinto = 0

        #5 TintoSyrah
        elif(escolhaTinto == 5):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, TintoSyrah)
            escolhaTinto = 0

        #menu vinho branco -----------

        #1 Chardonnay
        elif(escolhaBranco == 1):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, Chardonnay)
            escolhaBranco = 0

        #2 SauvignonBlanc
        elif(escolhaBranco == 2):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, SauvignonBlanc)
            escolhaBranco = 0

        #3 Riesling
        elif(escolhaBranco == 3):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, Riesling)
            escolhaBranco = 0

        #4 PinotGrigio
        elif(escolhaBranco == 4):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, PinotGrigio)
            escolhaBranco = 0

        #menu vinho rose -----------

        #1 CabernetFranc
        elif(escolhaRose == 1):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, CabernetFranc)
            escolhaRose = 0

        #2 Syrah
        elif(escolhaRose == 2):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, Syrah)
            escolhaRose = 0
            
        #3 Grenache
        elif(escolhaRose == 3):
            quantidade = quantidadeCheck(quantidade)
            quantidadeTotal = quantidade + quantidadeTotal
            valorTotal = valor(valorTotal, quantidade, Grenache)
            escolhaRose = 0
                                    
        #menu tipos -----------

        #Trigger para ativar o menu / 0
        elif (escolha == 0):
            for item in tipos:
                print(item)
            print(f'Valor total: {valorTotal}')
            print(f'Quantidade: {quantidadeTotal}')
            escolha = int(input('Escolha uma opção: '))
            print('')

        #Tinto / 1
        elif(escolha == 1):
            for item in tinto:
                print(item)
            escolhaTinto = int(input('Escolha o vinho desejado: '))
            print('')
            if escolhaTinto == 0:
                escolha = 0

        #Branco / 2
        elif(escolha == 2):
            for item in branco:
                print(item)
            escolhaBranco = int(input('Escolha o vinho desejado: '))
            print('')
            if escolhaBranco == 0:
                escolha = 0

        #Rose / 3
        elif(escolha == 3):

            for item in rose:
                print(item)
            escolhaRose = int(input('Escolha o vinho desejado: '))
            print('')
            if escolhaRose == 0:
                escolha = 0

        #Esvaziar carrinho / 8
        elif(escolha == 8):
            confirmar = int(input('Pressione 8 para confirmar ou 0 para voltar: '))
            print('')
            if (confirmar == 0):
                escolha = 0
            elif (confirmar == 8):
                valorTotal = 0
                quantidadeTotal = 0
                escolha = 0
                print('Carrinho esvaziado')
                print('')

        #Encerrar programa
        elif(escolha == 9):
            confirmar = int(input('Pressione 9 para confirmar ou 0 para voltar: '))
            print('')
            if (confirmar == 0):
                escolha = 0
            elif (confirmar == 9):
                break

        #Rever opções de input
        else:
            print('Opção inválida, tente novamente')
            print('')
            escolha = 0

    #Repetir em caso de erro
    except Exception:
        print('')
        print('Algo deu errado, tente novamente:')
        print('')

print("Fim do programa")
print('')