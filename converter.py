import os
import subprocess

# --- CONFIGURAÇÃO ---
PASTA_ENTRADA = "musicas_originais"
PASTA_SAIDA = "musicas_432hz"

# Cria a pasta de saída se não existir
if not os.path.exists(PASTA_SAIDA):
    os.makedirs(PASTA_SAIDA)

# Verifica se o FFmpeg está na pasta
if not os.path.exists("ffmpeg.exe"):
    print("ERRO CRÍTICO: O arquivo ffmpeg.exe não foi encontrado!")
    print("Por favor, copie o ffmpeg.exe para dentro desta pasta.")
    input("Pressione ENTER para sair...")
    exit()

# Lista as músicas
arquivos = [f for f in os.listdir(PASTA_ENTRADA) if f.endswith(('.mp3', '.wav', '.flac', '.m4a'))]
total = len(arquivos)

print(f"--- INICIANDO CONVERSÃO CORRIGIDA DE {total} MÚSICAS ---")
print("Ajustando frequência para 432Hz e corrigindo a velocidade...")
print("-" * 50)

for i, arquivo in enumerate(arquivos):
    caminho_entrada = os.path.join(PASTA_ENTRADA, arquivo)
    caminho_saida = os.path.join(PASTA_SAIDA, arquivo)
    
    # O SEGREDO ESTÁ NESTA LINHA ABAIXO:
    # asetrate=44100*0.9818 (Baixa o tom)
    # atempo=1.0185 (Acelera a velocidade de volta ao normal)
    comando = [
        "ffmpeg.exe", "-y", "-i", caminho_entrada,
        "-af", "asetrate=44100*0.9818,atempo=1.0185",
        caminho_saida
    ]
    
    # Roda o comando escondendo os textos técnicos do ffmpeg
    subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print(f"[{i+1}/{total}] Feito: {arquivo}")

print("-" * 50)
print("--- TUDO PRONTO! ---")
print("Pode fechar esta janela e ouvir suas músicas.")
input()