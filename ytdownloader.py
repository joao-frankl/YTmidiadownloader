import os
import yt_dlp

def baixar_video(url, somente_audio=False):
    """
    Baixa um vídeo do YouTube e opcionalmente extrai o áudio como MP3.

    :param url: URL do vídeo do YouTube
    :param somente_audio: Se verdadeiro, baixa apenas o áudio como MP3
    """
    try:
        ydl_opts = {
            'format': 'bestaudio/best' if somente_audio else 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }] if somente_audio else []
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download e conversão concluídos com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    url = input("Digite a URL do vídeo do YouTube: ")
    escolha = input("Deseja extrair apenas o áudio em MP3? (s/n): ").strip().lower()

    if escolha == 's':
        baixar_video(url, somente_audio=True)
    else:
        baixar_video(url, somente_audio=False)

if __name__ == '__main__':
    main()
