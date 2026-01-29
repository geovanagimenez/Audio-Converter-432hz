# 🎵 Conversor de Frequência 432Hz (Python + FFmpeg)

Uma ferramenta de automação desenvolvida em Python para processar lotes de arquivos de áudio, convertendo a frequência padrão (440Hz) para 432Hz.

O script utiliza a biblioteca **FFmpeg** para manipulação de DSP (Digital Signal Processing), aplicando uma lógica de correção de tempo para evitar que a música fique lenta (efeito *slow motion*) durante a alteração de frequência.

## 🚀 Funcionalidades
- Leitura automática de diretórios.
- Conversão em massa (Batch Processing).
- Correção automática de Pitch e BPM (Tempo).
- Interface simples via terminal.

## 🛠 Tecnologias
- Python 3.x
- FFmpeg (Audio Engine)
- Biblioteca `os` e `subprocess`

## 📦 Como usar este projeto
Como o FFmpeg é uma ferramenta externa, siga estes passos para rodar no seu PC:

1. Tenha o **Python** instalado.
2. Baixe este repositório (os arquivos `.py` e `.bat`).
3. **Importante:** Baixe o executável do [FFmpeg](https://ffmpeg.org/download.html) e coloque o arquivo `ffmpeg.exe` na mesma pasta do script.
4. Crie uma pasta chamada `musicas_originais` e coloque seus áudios lá.
5. Execute o arquivo `rodar.bat`.

---
*Desenvolvido por Geovana Domingos Gimenez*
