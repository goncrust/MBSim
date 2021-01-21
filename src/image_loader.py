from PIL import Image, ImageTk

IMAGEDIR = 'assets/images/'

botao_file = Image.open(IMAGEDIR + 'botao.png')
#botao_file = botao_file.resize((180, 180))
botao = ImageTk.PhotoImage(botao_file)
