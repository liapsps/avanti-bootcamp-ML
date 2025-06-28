from PIL import Image
import os

pasta = "archive/images/"  

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