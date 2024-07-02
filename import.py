import os

caminho_do_arquivo = "C/p/o/seu/arquivo.txt"

# Verifica se o arquivo existe antes de tentar removê-lo
if os.path.exists(caminho_do_arquivo):
    os.remove(caminho_do_arquivo)
    print("Arquivo removido com sucesso!")
else:
    print("O arquivo não existe.")