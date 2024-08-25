import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import yt_dlp
import os

def download_audio():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Entrada inválida", "Por favor, insira uma URL válida.")
        return
    
    try:
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # Caminho para o executável ffmpeg incluído no projeto
        ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg', 'bin', 'ffmpeg.exe')

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                'ffmpeg_location': ffmpeg_path  # Inclua o caminho do ffmpeg
            }],
            'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            status_label.config(text="Baixando áudio...", foreground="#007AFF")
            ydl.download([url])
            status_label.config(text=f"Download concluído! Salvo em {downloads_path}", foreground="#4CD964")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criação da janela principal
root = tk.Tk()
root.title("YouTube Audio Downloader")
root.geometry("400x200")
root.resizable(False, False)

# Estilo ttk inspirado no iOS
style = ttk.Style()
style.theme_use('clam')

# Cor de fundo da janela e dos widgets
root.configure(background='#F2F2F7')

# Estilo para os widgets
style.configure('TLabel', font=('San Francisco', 12), background='#F2F2F7', foreground='#000')
style.configure('TEntry', font=('San Francisco', 12), foreground='#000', padding=5)
style.configure('TButton', font=('San Francisco', 12, 'bold'), background='#007AFF', foreground='white', padding=5)
style.map('TButton', background=[('active', '#0051A8')], foreground=[('active', 'white')])

# Label e Entry para a URL
url_label = ttk.Label(root, text="URL do vídeo do YouTube:")
url_label.pack(pady=10)

url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

# Botão para iniciar o download
download_button = ttk.Button(root, text="Baixar Áudio", command=download_audio)
download_button.pack(pady=20)

# Label para exibir o status do download
status_label = ttk.Label(root, text="", background='#F2F2F7')
status_label.pack(pady=10)

# Inicia o loop principal do Tkinter
root.mainloop()
