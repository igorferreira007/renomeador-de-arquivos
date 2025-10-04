import os

# Caminho da pasta onde estão os vídeos
pasta = r"C:\Users\Igor\dwhelper"

# Lista todos os arquivos da pasta
arquivos = [f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]

# Ordena pela data de criação
arquivos.sort(key=lambda f: os.path.getctime(os.path.join(pasta, f)))

# Renomeia adicionando números
for i, nome in enumerate(arquivos, start=1):
    caminho_antigo = os.path.join(pasta, nome)
    novo_nome = f"{i} {nome}"
    caminho_novo = os.path.join(pasta, novo_nome)
    os.rename(caminho_antigo, caminho_novo)

print(f"{len(arquivos)} arquivos renomeados com sucesso!")
