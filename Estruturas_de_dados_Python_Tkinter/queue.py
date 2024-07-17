import tkinter as tk
import tkinter.filedialog as fd
import dataStructures
from PIL import ImageTk, Image

COLORBG = '#F0FFFF'
COLORBUTTON = '#00BBFF'
COLORBUTTON2 = '#00DDFF'
CANVASBG = '#F8FFFF'

#Classe da fila
class QueueWindow(tk.Tk):
    def __init__(self):
        #Janela principal da Fila
        self.window = tk.Tk()
        self.window.title("Fila")
        self.window.geometry("1280x720")
        self.window["bg"] = COLORBG

        #Canvas para a janela
        self.canvasQueue = tk.Canvas(self.window,width = 1180, height = 720, bg = CANVASBG)  
        self.canvasQueue.bind('<Button-1>',self.enqueueAux)
        self.canvasQueue.bind('<Button-3>',self.dequeueAux) 
        self.canvasQueue.pack()
        self.canvasQueue.place(x=100,y=0)

        #Menu para a janela da fila
        menu = tk.Menu(self.window)
        file_menu = tk.Menu(menu,tearoff = 0,bg = COLORBG)
        file_menu.add_command(label="Abrir",command = self.openFile)
        file_menu.add_separator()
        file_menu.add_command(label = "Salvar",command = self.saveFile)
        menu.add_cascade(label = "Arquivo",menu = file_menu)
        menu.add_command(label = "Sobre", command = self.about)
        operation_menu = tk.Menu(menu,tearoff = 0,bg = COLORBG)
        operation_menu.add_command(label = "Inserir", command = self.enqueue)
        operation_menu.add_command(label = "Remover", command = self.dequeue)
        operation_menu.add_command(label = "Limpar tela", command = self.deleteAll)
        operation_menu.add_command(label = "Retornar", command = self.returnMain)
        menu.add_cascade(label = "Operações", menu = operation_menu)
        self.window.config(menu = menu)    

        #---Adicionado os botões---
        buttonReturn = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Retornar")
        buttonReturn['command'] = self.returnMain
        buttonReturn.pack()
        buttonReturn.place(x=10,y=400)

        buttonInsert = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Inserir")
        buttonInsert['command'] = self.enqueue
        buttonInsert.pack()
        buttonInsert.place(x=10,y=250)

        buttonRemove = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Remover")
        buttonRemove['command'] = self.dequeue
        buttonRemove.pack()
        buttonRemove.place(x=10,y=300)

        buttonDeleteAll = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Limpar tela")
        buttonDeleteAll['command'] = self.deleteAll
        buttonDeleteAll.pack()
        buttonDeleteAll.place(x=10,y=350)

   
        #Localização no eixo y onde o retângulo deve ser desenhado
        self.locationX = 40

        #Lista para armazenar todos os retângulos 
        self.rectItem = []

        #List para guardar todos os textos
        #Textos vão dentro dos retângulos
        self.textItem = []

        #List para salvar todas as palavras usadas
        #É usada para salvar os dados no arquivo
        self.codeSave = []

        self.numberTasks = 0

    #Método para retornar para a janela principal
    def returnMain(self):
        self.window.destroy()
        dataStructures.FirstWindow()

    #Método que mostra informações sobre a estrutura
    def about(self, master = None):
        windowAbout = tk.Toplevel()
        windowAbout.geometry("1280x720")
        windowAbout['bg'] = COLORBG

        textAbout = open('txt/queueAbout.txt', 'r',encoding = 'utf8')

        title = tk.Label(windowAbout,text = 'FILA', font = ("Times", "40", "italic", "bold"), bg = COLORBG)
        title.pack()

        paragraph = tk.Label(windowAbout,text = textAbout.read(), font = ("Times","14"), bg = COLORBG, anchor = 'w')
        paragraph.pack()
        
        image = Image.open("img/queueImg.png")
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
            for i in range(len(self.codeSave)):
                new_file.write(self.codeSave[i] + "\n")
            new_file.close()

    #Método para abrir um arquivo
    def openFile(self):
        filename=fd.askopenfilename(title="Abrir arquivo",filetypes=(("Text files","*.txt"),))

        #Número de Objetos(Nome do livro,autor e ano) a serem construídos
        Tasks = sum(1 for line in open(filename))

        archive = open(filename,'r')
        while(Tasks > 0):
            #Lê as linahs sequencialmente
            Code = archive.readline().rstrip("\n")#Lê o ano e remove o \n

            #Cria o retângulo
            self.rectItem.append(self.canvasQueue.create_rectangle(self.locationX,200,self.locationX+30,400))

            #Escreve dentro do retângulo
            self.textItem.append(self.canvasQueue.create_text(self.locationX+15,300,text = "\n".join(Code)))

            #Atualiza as variáveis necessárias
            self.locationX = self.locationX + 30#Posição X para o próximo retêngulo e texto
            Tasks = Tasks - 1#Decrementa o objeto para depois conseguir sair do loop
            self.numberTasks = self.numberTasks + 1#Incrementa o número de objetos em 1
        
    #Método auxiliar para inserção pelo canvas
    def enqueueAux(self,event):
        self.enqueue()

    def enqueue(self):
        #Criando a janela de inserção
        self.windowInsert = tk.Tk()
        self.windowInsert.geometry("240x120")
        self.windowInsert['bg'] = COLORBG

        #Criando os Labels e as caixas de entrada
        label1 = tk.Label(self.windowInsert,text = "Entre com o código da tarefa",bg = COLORBG)
        label1.pack()
        self.entryCode = tk.Entry(self.windowInsert)
        self.entryCode.pack()

        #Criando o botão
        btn = tk.Button(self.windowInsert,text="Enviar",command=self.addTask,bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"))
        btn.pack()


    def addTask(self):
        #Verifica se preencheu com algum dado
        if(self.entryCode.get() == ''):
            labelError = tk.Label(self.windowInsert,text = "Preencha corretamente",bg = COLORBG)
            labelError.pack()
            labelError.place(x = 55,y = 80)

        else:
            #Desenha na tela
            self.rectItem.append(self.canvasQueue.create_rectangle(self.locationX,200,self.locationX+30,400))
            self.textItem.append(self.canvasQueue.create_text(self.locationX+15,300,text = "\n".join(self.entryCode.get())))

            #Salva a codigo
            self.codeSave.append(self.entryCode.get())
            self.windowInsert.destroy()
            self.canvasQueue.update()
            self.locationX = self.locationX + 30
            self.numberTasks = self.numberTasks + 1
            

    #Método auxiliar para a remoção pelo canvas
    def dequeueAux(self,event):
        self.dequeue()
    
    def dequeue(self):
        if(self.numberTasks != 0):
            self.canvasQueue.delete(self.rectItem[0])
            self.canvasQueue.delete(self.textItem[0])
            self.codeSave = self.codeSave[1:]
            self.rectItem = self.rectItem[1:]
            self.textItem = self.textItem[1:]
            self.locationX = self.locationX - 30
            self.numberTasks = self.numberTasks - 1
            for i in range(self.numberTasks):
                self.canvasQueue.move(self.rectItem[i],-30,0)
                self.canvasQueue.move(self.textItem[i],-30,0)
    
    #Deleta todos os componentes do canvas
    def deleteAll(self):
        self.canvasQueue.delete("all")#Deleta todos os componentes

        #Define os valores para as condições iniciais
        self.rectItem = []
        self.textItem = []
        self.codeSave = []
        self.locationX = 40
        self.numberTasks = 0