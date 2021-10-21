import os
import shutil

nome = []

a = "C:/Users/topo/Desktop/REM05_MMT.txt"  #ENTRADA DE DADOS
listaNumeros = []

with open(a ,"r") as arquivo:  #LÊ ENTRADA  E ADICIONA EM UMA LISTA
    for a in arquivo:
        nome.append(a)

tamanho = len(nome)
panoramica = []
cont=0
chave = True

c = f"//ManausSt02/Projeto/OS703-19_PM-Manaus/Fotos_360//{nome[cont][0:11]}//08_Proj_Processing/Panoramica"
caminho= f"//ManausSt02/Projeto/OS703-19_PM-Manaus/Fotos_360//{nome[cont][0:11]}//08_Proj_Processing/Panoramica"
caminhoDestino = f"C:/Users/topo/Desktop/Foto/{nome[cont][0:11]}/PAN"

while (os.path.exists(c)):

    c = f"//ManausSt02/Projeto/OS703-19_PM-Manaus/Fotos_360//{nome[cont][0:11]}//08_Proj_Processing/Panoramica"
    caminhoDestino = f"C:/Users/topo/Desktop/Foto/{nome[cont][0:11]}/PAN"
    if nome[cont][0:17] != nome[cont-1][0:17] or chave == True:
        chave = False
        if not os.path.exists(caminhoDestino):
            print(('entrou'))
            os.makedirs(f"C:/Users/topo/Desktop/Foto/{nome[cont][0:11]}/PAN") #CRIA PASTA
            for fotos in os.listdir(c):
              panoramica.append(fotos)
    cont += 1
    if cont+1 >=tamanho:
        break

cont=0
l=10
listaR= []

for r in panoramica:
    for n in nome:
        if cont >= tamanho:
            break
        caminho = f"//ManausSt02/Projeto/OS703-19_PM-Manaus/Fotos_360//{nome[cont][0:11]}//08_Proj_Processing/Panoramica"
        caminhoAtual= f"C:/Users/topo/Desktop/Foto/{nome[cont][0:11]}/PAN"
        if (r[0:17] == n[0:17]) and not  r[0:17]  in  listaR:
            listaR = r[0:17]
            caminhoOrigem = caminho + "/" + r
            caminhoDestino = f"C:/Users/topo/Desktop/Foto/{nome[cont][0:11]}/PAN"
            os.chdir(f"//ManausSt02/Projeto/OS703-19_PM-Manaus/Fotos_360//{nome[cont][0:11]}//08_Proj_Processing/Panoramica")

            shutil.copy(caminhoOrigem,caminhoDestino)

            if cont == l :
                l+=10
                print("FOTOS COPIADAS: ",cont,'Dia: ',n[6:8] )
            cont += 1

            break


print("TERMINOU" )



