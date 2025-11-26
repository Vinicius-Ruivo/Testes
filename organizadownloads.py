# importando bibliotecas que for necessário
import os
import shutil
# Definindo o local onde vou organizar
diretorio_alvo = r"C:\Users\vinic\Downloads"
# Basicamente um dicionario onde vai dizer para o programa o que cada arquivo é para achar as pastas
regras = {
    ".pdf": "Documentos",
    ".txt": "Documentos",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".exe": "Instaladores",
    ".zip": "Compactados",
    ".m4a": "Audios"
}

for arquivo in os.listdir(diretorio_alvo):
    caminho_completo = os.path.join(diretorio_alvo, arquivo)

    # Verifica se é um arquivo mesmo (e não uma pasta)
    if os.path.isfile(caminho_completo):
        nome, extensao = os.path.splitext(arquivo)

        # Se a extensão estiver nas nossas regras...
        if extensao.lower() in regras:
            pasta_destino = regras[extensao.lower()]
            caminho_pasta = os.path.join(diretorio_alvo, pasta_destino)

            # Cria a pasta se ela não existir
            os.makedirs(caminho_pasta, exist_ok=True)

            # Move o arquivo
            shutil.move(caminho_completo, os.path.join(caminho_pasta, arquivo))
            print(f"✅ Movido: {arquivo} -> {pasta_destino}")

print("Organização concluída!")
