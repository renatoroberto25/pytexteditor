from guizero import App, TextBox, PushButton
from tkinter import filedialog

app = App(title="Editor de Texto", bg="green")

def save_text():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        text = text_box.value
        file.write(text)
        file.close()

def open_file():
    file = filedialog.askopenfilename()
    if file:
        with open(file, "r") as f:
            text_box.value = f.read()

# Criação dos botões de salvar e mudar cor
save_button = PushButton(app, command=save_text, text="Salvar", grid=[3,1], align="bottom", width=20, height=2)
save_button.text_color = "black"
save_button.bg = "blue"

open_button = PushButton(app, command=open_file, text="Abrir", grid=[3,2], align="bottom", width=20, height=2)
open_button.text_color = "black"
open_button.bg = "blue"

close_button = PushButton(app, command=exit, text="Sair", grid=[3,0],align="bototm", width=1, height=1)
close_button.text_color = "black"
close_button.bg = "red"
# grid=[3,1]
# Criação da caixa de texto
text_box = TextBox(app, multiline=True, width=50, height=50)
text_box.bg = "black"
text_box.text_color = "green"

app.display()
