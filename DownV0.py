# importar as Bibliotecas a usar -----------------------------------------------------------------------------------------------------------------
from io import BytesIO
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox, Progressbar
from PIL import Image, ImageTk
from pytube import YouTube
import requests
#-------------------------------------------------------------------------------------------------------------------------------------------------
# criar a Função Mostrar -------------------------------------------------------------------------------------------------------------------------
def mostrar_imagem():
    try:
        yt = YouTube(Eurl.get())
        
        if escolha.get() == 'MP3':
            streams = yt.streams.filter(only_audio=True)
            qualidades = sorted(set([stream.abr for stream in streams if stream.abr]), reverse=True)
        elif escolha.get() == 'MP4':
            streams = yt.streams.filter(file_extension='mp4').order_by('resolution')
            qualidades = sorted(set([f"{stream.resolution} - {stream.type}" for stream in streams if stream.resolution != '144p']), reverse=True)
        
        messagebox.showinfo("Qualidades", "Qualidades disponíveis:\n" + "\n".join(qualidades))

        if not qualidades:
            messagebox.showinfo("Nenhuma", "Nenhuma qualidade disponível.")
            return
        
        CMBQualidade['values'] = qualidades
        CMBQualidade.current(0)  # Seleciona o primeiro item da lista por padrão
        
        thumb_url = yt.thumbnail_url
        image_data = requests.get(thumb_url).content
        image = Image.open(BytesIO(image_data))
        image = image.resize((435, 300))
        photo = ImageTk.PhotoImage(image)
        Limagem.configure(image=photo)
        Limagem.image = photo
        
    except Exception as e:
       messagebox.showerror("Erro", str(e))
#--------------------------------------------------------------------------------------------------------------------------------------------------
# cria a Função para Download Audio ---------------------------------------------------------------------------------------------------------------
def download_audio(stream):
    try:
        file_path = filedialog.asksaveasfilename(defaultextension='.mp3', filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            Avanco.start()  # Inicia a barra de progresso
            stream.download(output_path=file_path.rsplit('/', 1)[0])
            messagebox.showinfo("Download", f"Download concluído: {stream.default_filename}")
            Avanco.stop()  # Para a barra de progresso
    except Exception as e:
        messagebox.showerror("Erro", "Erro no download de áudio: " + str(e))
#--------------------------------------------------------------------------------------------------------------------------------------------------
# criar a Função para Fazer Download de video -----------------------------------------------------------------------------------------------------
def download_video():
    try:
        yt = YouTube(Eurl.get())
        qualidade_selecionada = CMBQualidade.get().split(" - ")[0]  # Obtendo apenas a resolução da qualidade selecionada

        if escolha.get() == 'MP3':
            stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
            if stream:
                download_audio(stream)
            else:
                messagebox.showinfo("Erro", "Stream de áudio não encontrado.")
        elif escolha.get() == 'MP4':
            resolutions = {'240p': 426, '360p': 640, '480p': 854, '720p': 1280, '1080p': 1920}
            target_resolution = resolutions.get(qualidade_selecionada)
            if target_resolution is not None:
                best_stream = None
                min_diff = float('inf')
                for available_stream in yt.streams.filter(file_extension='mp4', progressive=True):
                    if available_stream.resolution:
                        diff = abs(int(available_stream.resolution.split('p')[0]) - target_resolution)
                        if diff < min_diff:
                            best_stream = available_stream
                            min_diff = diff
                if best_stream:
                    download_video_stream(best_stream)
                else:
                    messagebox.showinfo("Erro", "Stream de vídeo não encontrado. Por favor, selecione outra qualidade.")
            else:
                messagebox.showinfo("Erro", "Resolução de vídeo selecionada inválida.")
    except Exception as e:
        messagebox.showerror("Erro", "Erro no download: " + str(e))
#------------------------------------------------------------------------------------------------------------------------------------------------
# Função Para Fazer Stream de Video -------------------------------------------------------------------------------------------------------------
def download_video_stream(stream):
    try:
        file_path = filedialog.asksaveasfilename(defaultextension='.mp4', filetypes=[("MP4 files", "*.mp4")])
        if file_path:
            Avanco.start()  # Inicia a barra de progresso
            stream.download(output_path=file_path.rsplit('/', 1)[0])
            messagebox.showinfo("Download", f"Download concluído: {stream.default_filename}")
            Avanco.stop()  # Para a barra de progresso
    except Exception as e:
        messagebox.showerror("Erro", "Erro no download de vídeo: " + str(e))
#------------------------------------------------------------------------------------------------------------------------------------------------
# função para Limpar Campos ---------------------------------------------------------------------------------------------------------------------
def limpar_campos():
    Eurl.delete(0, END)  # Limpa o campo de entrada
    Limagem.config(image=None)  # Remove a imagem exibida
    Limagem.image = None  # Limpa a referência à imagem
    CMBQualidade.set('Qualidade')  # Define o valor padrão para a combobox de qualidade
    escolha.set(None)  # Define o valor padrão para os botões de escolha
#------------------------------------------------------------------------------------------------------------------------------------------------
# defenir as Cores a usar -----------------------------------------------------------------------------------------------------------------------
co0='#ffffff' # Fundo e janela
co1='#ddf0f0' # Botões
co2='#e1e9eb' # label Imagen
co3='#000000' # cor letra
#------------------------------------------------------------------------------------------------------------------------------------------------
# configurar a Janela ---------------------------------------------------------------------------------------------------------------------------
Janela = Tk()
Janela.geometry('600x380+100+100')
Janela.resizable(0, 0)
Janela.title('Youtube Downloader V0 DevJoel PT 2024 ©')
Janela.config(bg=co0)
Janela.iconbitmap('C:\\Users\\HP\\Desktop\\Projectos\\DownloadV0\\icon.ico')
#------------------------------------------------------------------------------------------------------------------------------------------------
# criar a Barra de endreços ---------------------------------------------------------------------------------------------------------------------
Eurl = Entry(Janela, font=('arial 13'), width=63, bg=co2)
Eurl.place(x=10, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------
# criar o label para exbir a imagen do Video ----------------------------------------------------------------------------------------------------
Limagem = Label(Janela, bg=co2)
Limagem.place(x=10, y=30)
#------------------------------------------------------------------------------------------------------------------------------------------------
# criar a Combobox para exbir a qualidade -------------------------------------------------------------------------------------------------------
CMBQualidade = Combobox(Janela, width=9, font=('arial 14'))
CMBQualidade.set('Qualidade')
CMBQualidade.place(x=459, y=30)
#-------------------------------------------------------------------------------------------------------------------------------------------------
# criar as variaveis e os Radiobutons ------------------------------------------------------------------------------------------------------------
escolha = StringVar()
escolha.set(None)
RDMp3 = Radiobutton(Janela, text='Mp3', font=('arial 17 bold'), variable=escolha, value='MP3', bg=co0)
RDMp3.place(x=460, y=65)
RDMp4 = Radiobutton(Janela, text='Mp4', font=('arial 17 bold'), variable=escolha, value='MP4',bg=co0)
RDMp4.place(x=460, y=120)
#--------------------------------------------------------------------------------------------------------------------------------------------------
# criar os Botões ---------------------------------------------------------------------------------------------------------------------------------
BMostrar = Button(Janela, text='Mostrar', font=('arial 14'), relief=RAISED, overrelief=RIDGE, width=10, command=mostrar_imagem, bg=co1)
BMostrar.place(x=460, y=170)
BDownload = Button(Janela, text='Download', font=('arial 14'), relief=RAISED, overrelief=RIDGE, width=10, command=download_video, bg=co1)
BDownload.place(x=460, y=220)
BLimpar = Button(Janela, text='Limpar', font=('arial 14'), relief=RAISED, overrelief=RIDGE, width=10, command=limpar_campos, bg=co1)
BLimpar.place(x=460, y=270)
#---------------------------------------------------------------------------------------------------------------------------------------------------
# criar a Barra de progresso -----------------------------------------------------------------------------------------------------------------------
Avanco = Progressbar(Janela, length=570, mode='determinate')
Avanco.place(x=10, y=345)
#---------------------------------------------------------------------------------------------------------------------------------------------------
# iniciar a nossa janela ---------------------------------------------------------------------------------------------------------------------------
Janela.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------