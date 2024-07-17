import tkinter as tk
import tkinter.filedialog as fd
import dataStructures
from PIL import ImageTk, Image

COLORBG = '#F0FFFF'
COLORBUTTON = '#00BBFF'
COLORBUTTON2 = '#00DDFF'
CANVASBG = '#F8FFFF'

#Classe do nó usado na lista encadeada
class nodeList:
    def __init__(self,name,number,age,next):
        self.name = name
        self.number = number
        self.age = age
        self.next = next

#Classe da lista encadeada
class ListWindow(tk.Tk):
    def __init__(self):

        #---CRIANDO A JANELA---
        #Janela principal da lista encadeada
        self.window = tk.Tk()
        self.window.title("List")
        self.window.geometry("1280x720")
        self.window["bg"] = COLORBG

        #Canvas para a janela
        self.canvasList = tk.Canvas(self.window,width = 1180, height = 720, bg = CANVASBG) 
        self.canvasList.bind('<Button-1>',self.insertAux)
        self.canvasList.bind('<Button-3>',self.removeAux) 
        self.canvasList.pack()
        self.canvasList.place(x=100,y=0)

        #Menu para a janela
        menu = tk.Menu(self.window)
        file_menu = tk.Menu(menu,tearoff = 0,bg = COLORBG)
        file_menu.add_command(label="Abrir",command = self.openFile)
        file_menu.add_separator()
        file_menu.add_command(label = "Salvar", command = self.saveFile)
        menu.add_cascade(label = "Arquivo",menu = file_menu)
        menu.add_command(label = "Sobre", command = self.about)
        operation_menu = tk.Menu(menu,tearoff = 0,bg = COLORBG)
        operation_menu.add_command(label = "Inserir",command = self.insert)
        operation_menu.add_command(label = "Remover",command = self.remove)
        operation_menu.add_command(label = "Buscar",command = self.search)
        operation_menu.add_command(label = "Primeiro",command = self.firstStudent)
        operation_menu.add_command(label = "Limpar tela",command = self.deleteAll)
        operation_menu.add_command(label = "Retornar", command = self.returnMain)

        menu.add_cascade(label = "Operações", menu = operation_menu)
        self.window.config(menu = menu)

        #Adicionando os botões
        buttonBack = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Retornar")
        buttonBack['command'] = self.returnMain
        buttonBack.pack()
        buttonBack.place(x=10,y=450)
        buttonInsert = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Inserir")
        buttonInsert['command'] = self.insert
        buttonInsert.pack()
        buttonInsert.place(x=10,y=200)
        buttonRemove = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Remover")
        buttonRemove['command'] = self.remove
        buttonRemove.pack()
        buttonRemove.place(x=10,y=250)
        buttonFirst = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Primeiro")
        buttonFirst['command'] = self.firstStudent
        buttonFirst.pack()
        buttonFirst.place(x=10,y=350)
        buttonSearch = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Buscar")
        buttonSearch['command'] = self.search
        buttonSearch.pack()
        buttonSearch.place(x=10,y=300)
        buttonDeleteAll = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Limpar Tela")
        buttonDeleteAll['command'] = self.deleteAll
        buttonDeleteAll.pack()
        buttonDeleteAll.place(x=10,y=400)

        #definindo as condições iniciais
        self._first = None
        self._length = 0

    #Método para retornar para a janela principal
    def returnMain(self):
        self.window.destroy()
        dataStructures.FirstWindow()

    #Método que mostra informações sobre a estrutura
    def about(self, master = None):
        windowAbout = tk.Toplevel()
        windowAbout.geometry("1280x720")
        windowAbout['bg'] = COLORBG

        textAbout = open('txt/listAbout.txt', 'r',encoding = 'utf8')

        title = tk.Label(windowAbout,text = 'LISTA ENCADEADA', font = ("Times", "40", "italic", "bold"), bg = COLORBG)
        title.pack()

        paragraph = tk.Label(windowAbout,text = textAbout.read(), font = ("Times","14"), bg = COLORBG, anchor = 'w')
        paragraph.pack()
        
        image = Image.open("img/listImg.jpg")
        photo = ImageTk.PhotoImage(image)
        labelImage = tk.Label(master = windowAbout,image = photo, bg = COLORBG)
        labelImage.image = photo
        labelImage.pack()

    def openFile(self):
        filename=fd.askopenfilename(title="Abrir arquivo",filetypes=(("Text files","*.txt"),))
        elements = sum(1 for line in open(filename))//3 # Número de elementos que serão inseridos
        archive = open(filename,'r')
        name = []
        number = []
        age = []

        #Coloca todos os elementos em uma lista
        while (elements > 0):
            name.append(archive.readline().rstrip("\n"))
            number.append(int(archive.readline().rstrip("\n")))
            age.append(int(archive.readline().rstrip("\n")))
            elements = elements - 1
        

        self._length = len(name)#Define o tamanho da lista como o número de elementos na lista de nomes
        sizeList = len(name) - 1

        #Insere o último elemento da lista
        current = nodeList(name.pop(sizeList),number.pop(sizeList),age.pop(sizeList),None)
        sizeList = sizeList - 1
        
        #Vai inserindo na ordem decrescente
        for i in range(sizeList,-1,-1):
            previous = nodeList(name.pop(i),number.pop(i),age.pop(i),
                current)
            current = previous
        self._first = current
        self.printCanvas()#Chama o método que mostra no canvas
      
    #Método para salvar os arquivos
    def saveFile(self):
        current = self._first
        new_file = fd.asksaveasfile(title="Salvar arquivo",
        defaultextension=".txt",
        filetypes=(("Text files","*.txt"),))
        if new_file:
            i = self._length
            while (i > 0):
                new_file.write(current.name + "\n"
                    + str(current.number) + "\n" + str(current.age) +"\n")
                current = current.next
                i = i - 1
            new_file.close()

    #Método que mostra uma janela com o primeiro estudante
    def firstStudent(self):
        if(self._first != None):
            windowFirst = tk.Tk()
            windowFirst['bg'] = COLORBG
            windowFirst.title("1º Aluno")
            windowFirst.geometry("220x120")
            labelFirst = tk.Label(windowFirst,text = "Nome:\n" + self._first.name
            +  "\nNúmero:\n" + str(self._first.number) + "\nIdade:\n" + str(self._first.age), bg = COLORBG)
            labelFirst.pack()

    #Método para a busca de um aluno pelo seu número
    def search(self):
        self.windowsearch = tk.Tk()
        self.windowsearch.geometry("200x100")
        self.windowsearch['bg'] = COLORBG

        #Criando os Labels e as caixas de entrada
        label = tk.Label(self.windowsearch,text = "Entre com o número do aluno",bg = COLORBG)
        label.pack()
        self.searchNumber = tk.Entry(self.windowsearch)
        self.searchNumber.pack()

        btnsearch = tk.Button(self.windowsearch,text="Buscar na turma",command=self.searchStudent,bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"))
        btnsearch.pack()

        self.labelError = tk.Label(self.windowsearch, text = '')
        self.labelError.pack()
    
    #Método que mostra a janela com o aluno que foi procurado
    def searchStudent(self):
        self.labelError.destroy()
        #Verifica se foi digitado um número
        if(not self.searchNumber.get().isnumeric()):
            self.labelError = tk.Label(self.windowsearch,text = 'É necessário digitar um número',bg = COLORBG)
            self.labelError.pack()
        else:
            current = self._first
            number = int(self.searchNumber.get())
            #Busca na lista
            while (current != None and current.number != number):
                current = current.next
            #O aluno não está presente na lista
            if current == None:
                self.windowsearch.destroy()
                windowPrint = tk.Tk()
                labelPrint = tk.Label(windowPrint,text = "O aluno não está presente na turma",bg = COLORBG)
                labelPrint.pack()
                return False
            self.windowsearch.destroy()
            # O aluno está presente na lista
            windowPrint = tk.Tk()
            labelPrint = tk.Label(windowPrint,text = "O aluno está presente na turma\n"
                + "Nome:\n" + current.name + "\nNúmero:\n" + str(current.number) + 
                "\nIdade:\n" + str(current.age),bg = COLORBG)
            labelPrint.pack()
            return True

    #Método auxiliar para o canvas
    def insertAux(self,event):
        self.insert()

    def insert(self):
        #Criando a janela de inserção
        self.windowInsert = tk.Tk()
        self.windowInsert.geometry("320x200")
        self.windowInsert['bg'] = COLORBG

        #Criando os Labels e as caixas de entrada
        label1 = tk.Label(self.windowInsert,text = "Entre com o nome do aluno",bg = COLORBG)
        label1.pack()
        self.entryName = tk.Entry(self.windowInsert)
        self.entryName.pack()
        label2 = tk.Label(self.windowInsert,text = "Entre com o numero do aluno",bg = COLORBG)
        label2.pack()
        self.entryNumber = tk.Entry(self.windowInsert)
        self.entryNumber.pack()
        label3 = tk.Label(self.windowInsert,text = "Entre com a idade do aluno",bg = COLORBG)
        label3.pack()
        self.entryAge = tk.Entry(self.windowInsert)
        self.entryAge.pack()

        #Criando o botão
        btn = tk.Button(self.windowInsert,text="Enviar",command=self.addStudent,bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"))
        btn.pack()

        self.labelError = tk.Label(self.windowInsert,text = "Preencha os dados",bg = COLORBG)
        self.labelError.pack()
        self.labelError.place(x=105,y = 160)
    
    #Inserção do elemento na lista
    def addStudent(self):
        self.labelError.destroy()
        #Verifica se todos os itens foram preenchidos
        if((self.entryName.get() == '') or (self.entryNumber.get() == '') or (self.entryAge.get() == '')):
            self.labelError = tk.Label(self.windowInsert,text = 'É necessário preencher todos os campos',bg = COLORBG)
            self.labelError.pack()
            self.labelError.place(x=60,y = 160)
        #Verifica se número e idade são numéricos
        elif((not self.entryNumber.get().isnumeric() or (not self.entryAge.get().isnumeric()))):
            self.labelError = tk.Label(self.windowInsert,text = 'Número e idade precisam ser números',bg = COLORBG)
            self.labelError.pack()
            self.labelError.place(x=65,y = 160)
        #inserir na lista
        else:
            current = self._first
            previous = None
            name = self.entryName.get()
            number = int(self.entryNumber.get())
            age = int(self.entryAge.get())

            while (current != None and current.name < name):
                previous = current
                current = current.next
            if previous == None:
                current = nodeList(name,number,age,self._first)
                self._first = current
            else:
                current = nodeList(name,number,age,previous.next)
                previous.next = current
            self._length = self._length + 1
            self.windowInsert.destroy()
            self.printCanvas()
    
    #Método auxiliar para o canvas
    def removeAux(self,event):
        self.remove()


    def remove(self):
        #Criando a janela de remoção
        self.windowRemove = tk.Tk()
        self.windowRemove.geometry("200x100")
        self.windowRemove['bg'] = COLORBG

        #Criando os Labels e as caixas de entrada
        label = tk.Label(self.windowRemove,text = "Entre com o nome do aluno",bg = COLORBG)
        label.pack()
        self.removeName = tk.Entry(self.windowRemove)
        self.removeName.pack()

        btnRemove = tk.Button(self.windowRemove,text="Remover na turma",bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"),command=self.removeStudent)
        btnRemove.pack()
    
    #Removendo o estudante
    def removeStudent(self):
        current = self._first
        previous = None
        name = self.removeName.get()
        while (current != None and current.name != name):
            previous = current
            current = current.next
        if current == None:
            self.windowRemove.destroy()
            return False
        if current == self._first:
            self._first = current.next
        else:
            previous.next = current.next
        self._length = self._length - 1
        self.windowRemove.destroy()
        self.printCanvas()
        return True
  
    #Método para desenhar no canvas
    def printCanvas(self):
        i = self._length 
        current = self._first
        self.canvasList.delete('all')
        locationX = 40#Define a localização no eixo x para o primeiro elemento
        while i > 0:
            #Escrevendo os itens
            self.canvasList.create_text(locationX+40,350,text = "Nome:\n" + current.name[:13]
                + "\n\nIdade:\n" + str(current.age))
            #Desenhando o retângulo
            self.canvasList.create_rectangle(locationX,300,locationX+80,400)

            #Desenha a seta
            self.canvasList.create_line(locationX+80,350,locationX+95,350)   
            self.canvasList.create_line(locationX+95,340,locationX+95,360)  
            self.canvasList.create_line(locationX+95,340,locationX+100,350)
            self.canvasList.create_line(locationX+95,360,locationX+100,350)   
            self.canvasList.update()
            locationX = locationX + 100#Define a localização para o próximo elemento
            current = current.next
            i = i - 1

    #Método para limpar a tela
    def deleteAll(self):
        self.canvasList.delete('all')
        self._first = None
        self._length = 0