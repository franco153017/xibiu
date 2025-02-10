import random

#lista de palavras para o jogo
palavras = ['maçã', 'banana', 'laranja', 'uva', 'morango']

def jogo_da_forca():
    #escolhe uma palavra aleatoria da lista
    palavra = random.choice(palavras)
    #cria uma lista para armazenar as letras corretas
    letra_corretas = ['_'] * len(palavra)
    #cria uma lista para armazebar as letras erradas
    letras_erradas = []
    #defina o numero de tentativas
    tentativa = 6

    print("bem-vindo ao jogo da forca!")
    print("você tem 6 tentativas para adivinhar a palavra. ")

    while tentativas > 0 and '_' in letra_corretas:
        #mostrar as palavras com as letra corretas
        print(''.join(letra_corretas))
        #pede para o usuario digitar uma letra
        letra = input ("digite uma letra: ").lower()
        #vereficar se a letra e correta
        if letra in  palavra:
            #subistitui as letras corretas na lista
            for i, l in enumerate(palavra):
                if l == letra:
                    letra_corretas[i] = letra
            else:
                #adiciona a letra errada a lista
                letras_erradas.append(letra)
                #diminui o numero de tentativas
                tentativa -= 1
        print(f"tentativas restantes: {tentativa}")
        print(f"letras erradas:{','.join(letras_erradas)}")
 
 #vereficar se o usuario ganhou ou perdeu
 if '_' not in letras_corretas
