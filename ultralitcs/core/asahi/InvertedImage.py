import os
from PIL import Image

class InvertedImage:

    def inverted(self, diretorio):

        extensoes = ('.png', '.jpg', '.jpeg')

        for arquivo in os.listdir(diretorio):
            caminho_completo = os.path.join(diretorio, arquivo)

            if arquivo.lower().endswith(extensoes):
                try:
                    with Image.open(caminho_completo) as img:
                        largura, altura = img.size
                        if altura > largura:
                            print(f"Rotacionando {arquivo}...")

                            img_rotacionada = img.rotate(-90, expand=True)

                            img_rotacionada.save(caminho_completo)

                            print(f"{arquivo} foi rotacionada e salva.")
                except Exception as e:
                    print(f"Erro ao processar {arquivo}: {e}")