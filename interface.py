# importar as Bibliotecas a Usar --------------------------------------------------------------------
from tkinter import *
from tkinter.ttk import Combobox, Progressbar
#----------------------------------------------------------------------------------------------------












# defenir as Cores a Usar --------------------------------------------------------------------------
co0='#ffffff' # Fundo e janela
co1='#ddf0f0' # Botões
co2='#e1e9eb' # label Imagen
co3='#000000' # cor letra
#----------------------------------------------------------------------------------------------------
# configurar a Nossa Janela -------------------------------------------------------------------------
Janela = Tk()
Janela.geometry('600x380+100+100')
Janela.resizable(0,0)
Janela.title('Youtube Downloader V0 DevJoel PT 2024 © interface')
Janela.config(bg=co0)
Janela.iconbitmap('C:\\Users\\HP\\Desktop\\Projectos\\DownloadV0\\icon.ico')
#----------------------------------------------------------------------------------------------------
# criar a barra de endreço ------------------------------------------------------------------------------------------
Eurl = Entry(Janela, bg=co2, font=('arial 13'),width=63)
Eurl.place(x=10, y=0)
#--------------------------------------------------------------------------------------------------------------------
# criar o label para apresentar a capa do video ---------------------------------------------------------------------
Limagem = Label(Janela, width=62, height=20,)
Limagem.place(x=10, y=30)
#--------------------------------------------------------------------------------------------------------------------
# criar a combobox qualidade ----------------------------------------------------------------------------------------
Qualidade = Combobox(Janela, width=9, font=('arial 14'))
Qualidade.set('Qualidade')
Qualidade.place(x=459, y=30)
#--------------------------------------------------------------------------------------------------------------------
# criar a variavel mais Radiobutons Mp3 e Mp4------------------------------------------------------------------------
escolha = StringVar()
escolha.set(None)
mp3 = Radiobutton(Janela, text='Mp3', font=('arial 17 bold'), bg=co0, variable=escolha, value='MP3')
mp3.place(x=460, y=65)
mp4 = Radiobutton(Janela, text='Mp4', font=('arial 17 bold'), bg=co0, variable=escolha, value='MP4')
mp4.place(x=460, y=120)
#--------------------------------------------------------------------------------------------------------------------
# Criar Os Botões ---------------------------------------------------------------------------------------------------
BMostrar = Button(Janela, text='Mostrar', font=('arial 14'), relief=RAISED, overrelief=RIDGE, width=10, bg=co1)
BMostrar.place(x=460, y=170)
BDown = Button(Janela, text='BDownload', font=('arial 14'), relief=RAISED, overrelief=RIDGE, width=10, bg=co1)
BDown.place(x=460, y=220)
BDown = Button(Janela, text='Limpar', font=('arial 14'), relief=RAISED, overrelief=RIDGE, width=10, bg=co1)
BDown.place(x=460, y=270)
#--------------------------------------------------------------------------------------------------------------------
# criar uma barra de progresso --------------------------------------------------------------------------------------
Avanco = Progressbar(Janela, length=570, mode='determinate')
Avanco.place(x=10, y=345)
#--------------------------------------------------------------------------------------------------------------------
# iniciar a Nossa Janela --------------------------------------------------------------------------------------------
Janela.mainloop()
#--------------------------------------------------------------------------------------------------------------------