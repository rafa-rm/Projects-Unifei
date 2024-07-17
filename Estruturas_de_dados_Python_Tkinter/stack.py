import tkinter as tk
import tkinter.filedialog as fd
import dataStructures
from PIL import ImageTk, Image


COLORBG = '#F0FFFF'
COLORBUTTON = '#00BBFF'
COLORBUTTON2 = '#00DDFF'
CANVASBG = '#F8FFFF'

#Classe da pilha
class StackWindow(tk.Tk):
    def __init__(self):
        #Janela principal da pilha
        self.window = tk.Tk()
        self.window.title("Pilha")
        self.window.geometry("1280x720")
        self.window["bg"] = COLORBG

        #Canvas para a janela
        self.canvasStack = tk.Canvas(self.window,width = 1180, height = 720, bg = CANVASBG)   
        self.canvasStack.bind('<Button-1>',self.pushAux)
        self.canvasStack.bind('<Button-3>',self.popAux)
        self.canvasStack.pack()
        self.canvasStack.place(x=100,y=0)


        #Menu para a janela da pilha
        menu = tk.Menu(self.window,)
        file_menu = tk.Menu(menu,tearoff = 0,bg = COLORBG)
        file_menu.add_command(label="Abrir",command = self.openFile)
        file_menu.add_separator()
        file_menu.add_command(label = "Salvar",command = self.saveFile)
        menu.add_cascade(label = "Arquivo",menu = file_menu)
        menu.add_command(label = "Sobre", command = self.about)
        operation_menu = tk.Menu(menu,tearoff = 0,bg = COLORBG)
        operation_menu.add_command(label = "Inserir", command = self.push)
        operation_menu.add_command(label = "Remover", command = self.pop)
        operation_menu.add_command(label = "Limpar tela", command = self.deleteAll)
        operation_menu.add_command(label = "Retornar", command = self.returnMain)
        menu.add_cascade(label = "Operações", menu = operation_menu)
        self.window.config(menu = menu)    

        #---Adicionado os botões---
        buttonReturn = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"), text = "Retornar")
        buttonReturn['command'] = self.returnMain
        buttonReturn.pack()
        buttonReturn.place(x=10,y=400)

        buttonInsert = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Inserir")
        buttonInsert['command'] = self.push
        buttonInsert.pack()
        buttonInsert.place(x=10,y=250)

        buttonRemove = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Remover")
        buttonRemove['command'] = self.pop
        buttonRemove.pack()
        buttonRemove.place(x=10,y=300)

        buttonDeleteAll = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Limpar tela")
        buttonDeleteAll['command'] = self.deleteAll
        buttonDeleteAll.pack()
        buttonDeleteAll.place(x=10,y=350)
   
        #Localização no eixo y onde o retângulo deve ser desenhado
        self.locationY = 700

        #Lista para armazenar todos os retângulos 
        self.rectItem = []

        #List para guardar todos os textos
        #Textos vão dentro dos retângulos
        self.textItem = []

        #List para salvar todas as palavras usadas
        #É usada para salvar os dados no arquivo
        self.wordSave = []

        self.numberObjects = 0

    #Método para retornar para a janela principal
    def returnMain(self):
        self.window.destroy()
        dataStructures.FirstWindow()

    #Método que mostra informações sobre a estrutura
    def about(self, master = None):
        windowAbout = tk.Toplevel()
        windowAbout.geometry("1280x720")
        windowAbout['bg'] = COLORBG

        #Abre o texto com os arquivos
        textAbout = open('txt/stackAbout.txt', 'r',encoding = 'utf8')

        #Escreve o título em um label
        title = tk.Label(windowAbout,text = 'PILHA', font = ("Times", "40", "italic", "bold"), bg = COLORBG)
        title.pack()

        #Escreve o parágrafo em um label
        paragraph = tk.Label(windowAbout,text = textAbout.read(), font = ("Times","14"), bg = COLORBG, anchor = 'w')
        paragraph.pack()
        
        #Abre a imagem para a estrutura
        image = Image.open("img/stackImg.png")
        image = image.resize((500, 220), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        labelImage = tk.Label(master = windowAbout,width = 500, height = 220, image = photo, bg = COLORBG)
        labelImage.image = photo
        labelImage.pack()

    #Método para salvar um arquivo
    def saveFile(self):
        new_file = fd.asksaveasfile(title="Salvar arquivo",
        defaultextension=".txt",
        filetypes=(("Text files","*.txt"),))
        if new_file:
            for i in range(len(self.wordSave)):
                new_file.write(self.wordSave[i] + "\n")
            new_file.close()

    #Método para abrir um arquivo
    def openFile(self):
        filename=fd.askopenfilename(title="Abrir arquivo",filetypes=(("Text files","*.txt"),))

        print(filename)
        #Número de Objetos(Nome do livro,autor e ano) a serem construídos
        Objects = sum(1 for line in open(filename))//3

        archive = open(filename,'r')
        while(Objects > 0):
            #Lê as linahs sequencialmente
            name = archive.readline().rstrip("\n")#Lê o nome e remove o \n
            author = archive.readline().rstrip("\n")#Lê o autor e remove o \n
            year = archive.readline().rstrip("\n")#Lê o ano e remove o \n

            #Cria o retângulo
            self.rectItem.append(self.canvasStack.create_rectangle(200,self.locationY-40,1000,self.locationY))

            #Escreve dentro do retângulo
            self.textItem.append(self.canvasStack.create_text(600,self.locationY-20,text = "Nome do livro: " + name
            + ",  Autor do livro: " + author + ",  Ano de lançamento: " + year))

            #Atualiza as variáveis necessárias
            self.locationY = self.locationY - 40#Posição Y para o próximo retêngulo e texto
            Objects = Objects - 1#Decrementa o objeto para depois conseguir sair do loop
            self.numberObjects = self.numberObjects + 1#Incrementa o número de objetos em 1
        
    #Método auxiliar para a inserção através do canvas
    def pushAux(self,event):
        self.push()

    def push(self):
        #Criando a janela de inserção
        self.windowInsert = tk.Tk()
        self.windowInsert.geometry("320x200")
        self.windowInsert['bg'] = COLORBG

        #Criando os Labels e as caixas de entrada
        label1 = tk.Label(self.windowInsert,text = "Entre com o nome do livro",bg = COLORBG)
        label1.pack()
        self.entryName = tk.Entry(self.windowInsert)
        self.entryName.pack()
        label2 = tk.Label(self.windowInsert,text = "Entre com o nome do autor",bg = COLORBG)
        label2.pack()
        self.entryAuthor = tk.Entry(self.windowInsert)
        self.entryAuthor.pack()
        label3 = tk.Label(self.windowInsert,text = "Entre com o ano de publicação",bg = COLORBG)
        label3.pack()
        self.entryYear = tk.Entry(self.windowInsert)
        self.entryYear.pack()

        #Criando o botão
        btn = tk.Button(self.windowInsert,text="Enviar",command=self.addObject,bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"))
        btn.pack()


    def addObject(self):
        #Testando se todas as entradas foram digitadas
        if((self.entryName.get() == '') or (self.entryAuthor.get() == '') or (self.entryYear.get() == '')):
            labelError = tk.Label(self.windowInsert,text = "Preencha corretamente",bg = COLORBG)
            labelError.pack()
            labelError.place(x = 95,y = 160)
        #Testando se a entrada de ano é numérico
        elif(not self.entryYear.get().isnumeric()):
            labelError = tk.Label(self.windowInsert,text = "Ano precisa ser numérico",bg = COLORBG)
            labelError.pack()
            labelError.place(x = 95,y = 160)
        else:        
            #desenha na tela
            self.rectItem.append(self.canvasStack.create_rectangle(200,self.locationY-40,1000,self.locationY))
            self.textItem.append(self.canvasStack.create_text(600,self.locationY-20,text = "Nome do livro: " + self.entryName.get()
            + ",  Autor do livro: " + self.entryAuthor.get() + ",  Ano de lançamento: " + self.entryYear.get()))

            #Salva a palavra
            self.wordSave.append(self.entryName.get())
            self.wordSave.append(self.entryAuthor.get())
            self.wordSave.append(self.entryYear.get())
            self.windowInsert.destroy()
            self.canvasStack.update()
            self.locationY = self.locationY - 40
            self.numberObjects = self.numberObjects + 1

    #Método auxiliar para a remoção pelo canvas
    def popAux(self,event):
        self.pop()

    def pop(self):
        if(self.numberObjects != 0):
            self.canvasStack.delete(self.rectItem[self.numberObjects - 1])
            self.canvasStack.delete(self.textItem[self.numberObjects - 1])
            self.wordSave = self.wordSave[:len(self.wordSave) - 3]
            self.rectItem = self.rectItem[:self.numberObjects-1]
            self.textItem = self.textItem[:self.numberObjects-1]
            self.locationY = self.locationY + 40
            self.numberObjects = self.numberObjects - 1
    
    #Deleta todos os componentes do canvas
    def deleteAll(self):
        self.canvasStack.delete("all")#Deleta todos os componentes

        #Define os valores para as condições iniciais
        self.rectItem = []
        self.textItem = []
        self.wordSave = []
        self.locationY = 700
        self.numberObjects = 0