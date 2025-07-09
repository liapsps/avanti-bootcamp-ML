from PIL import Image
import os

pasta = "archive/images/"  

#verificando valores ausentes nos metadados
for nome in os.listdir(pasta):
    caminho = os.path.join(pasta, nome)

    if nome.lower().endswith('.png'):
        try:
            with Image.open(caminho) as img:
                if img.info:
                    print(f"[{nome}] Metadados encontrados:")
                    for chave, valor in img.info.items():
                        print(f"  - {chave}: {valor}")
                else:
                    print(f"[{nome}] Nenhum metadado encontrado.")
        except Exception as e:
            print(f"[{nome}] Erro ao abrir: {e}")

#media das alturas e larguras para saber se possui alguma dimensão fora do esperado
larguras = []
alturas = []

for nome in os.listdir(pasta):
    if nome.lower().endswith(".png"):
        try:
            with Image.open(os.path.join(pasta, nome)) as img:
                w, h = img.size
                larguras.append(w)
                alturas.append(h)
        except:
            continue

if larguras and alturas:
    print(f"Largura - min: {min(larguras)}, max: {max(larguras)}, media: {sum(larguras)//len(larguras)}")
    print(f"Altura  - min: {min(alturas)}, max: {max(alturas)}, media: {sum(alturas)//len(alturas)}")
else:
    print("Nenhuma imagem válida encontrada.")

#largura minima e maxima
largura_min, largura_max = 1280, 1280  
altura_min, altura_max = 720, 720   

for nome in os.listdir(pasta):
    caminho = os.path.join(pasta, nome)
    if nome.lower().endswith('.png'):
        try:
            with Image.open(caminho) as img:
                largura, altura = img.size
                #se a largura for maior que a minima e menor que a maxima 
                if not (largura_min <= largura <= largura_max) or not (altura_min <= altura <= altura_max):
                    print(f"Dimensões fora do esperado: {largura}x{altura}")
        except Exception as e:
            print(f"[{nome}] Erro ao abrir: {e}")
        try:
            #todas as imagens possuem mesma dimensão
            with Image.open(caminho) as img:
                largura, altura = img.size
                print(f"{nome} -> {largura}x{altura}")
        except Exception as e:
            print(f"[{nome}] Erro ao abrir: {e}")
