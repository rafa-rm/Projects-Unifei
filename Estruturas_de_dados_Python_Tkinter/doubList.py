import tkinter as tk
import tkinter.filedialog as fd
import dataStructures
from PIL import ImageTk, Image

COLORBG = '#F0FFFF'
COLORBUTTON = '#00BBFF'
COLORBUTTON2 = '#00DDFF'
CANVASBG = '#F8FFFF'

#Classe do nó usado na lista duplamente encadeada
class NodeGameList:
    def __init__(self,name,publisher,year,next,prev):
        self.name = name
        self.publisher = publisher
        self.year = year
        self.next = next
        self.prev = prev

#Classe da lista duplamente encadeada
class DoubListWindow(tk.Tk):
    def __init__(self, master = None):
        #---CRIANDO A JANELA---
        #Janela principal da lista duplamente encadeada
        self.window = tk.Tk()
        self.window.title("Lista Duplamente Encadeada")
        self.window.geometry("1280x720")
        self.window["bg"] = COLORBG

        #Canvas para a janela
        self.canvasDoubList = tk.Canvas(self.window,width = 1180, height = 720, bg = CANVASBG)   
        self.canvasDoubList.bind('<Button-1>',self.insertAux)
        self.canvasDoubList.bind('<Button-3>',self.removeAux) 
        self.canvasDoubList.pack()
        self.canvasDoubList.place(x=100,y=0)

        #Menu para a janela
        menu = tk.Menu(self.window)
        file_menu = tk.Menu(menu,tearoff = 0,bg = COLORBG)
        file_menu.add_command(label="Open", command = self.openFile)
        file_menu.add_separator()
        file_menu.add_command(label = "Save", command = self.saveFile)
        menu.add_cascade(label = "File",menu = file_menu)
        menu.add_command(label = "Sobre", command = self.about)
        operation_menu = tk.Menu(menu,tearoff = 0,bg = COLORBG)
        operation_menu.add_command(label = "Inserir", command = self.insert)
        operation_menu.add_command(label = "Remover", command = self.remove)
        operation_menu.add_command(label = "Buscar", command = self.search)
        operation_menu.add_command(label = "Ordem Crescente", command = self.ascendingOrder)
        operation_menu.add_command(label = "Ordem Decrescente", command = self.descendingOrder)
        operation_menu.add_command(label = "Limpar tela", command = self.deleteAll)
        operation_menu.add_command(label = "Retornar", command = self.returnMain)

        menu.add_cascade(label = "Operations", menu = operation_menu)
        self.window.config(menu = menu)

        #Adicionando os botões
        buttonBack = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Retornar")
        buttonBack['command'] = self.returnMain
        buttonBack.pack()
        buttonBack.place(x=10,y=500)
        buttonInsert = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Inserir")
        buttonInsert['command'] = self.insert
        buttonInsert.pack()
        buttonInsert.place(x=10,y=200)
        buttonRemove = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Remover")
        buttonRemove['command'] = self.remove
        buttonRemove.pack()
        buttonRemove.place(x=10,y=250)
        buttonAscending = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Crescente")
        buttonAscending['command'] = self.ascendingOrder
        buttonAscending.pack()
        buttonAscending.place(x=10,y=350)
        buttonDescending = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Decrescente")
        buttonDescending['command'] = self.descendingOrder
        buttonDescending.pack()
        buttonDescending.place(x=10,y=400)
        buttonSearch = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Buscar")
        buttonSearch['command'] = self.search
        buttonSearch.pack()
        buttonSearch.place(x=10,y=300)
        buttonDeleteAll = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Limpar Tela")
        buttonDeleteAll['command'] = self.deleteAll
        buttonDeleteAll.pack()
        buttonDeleteAll.place(x=10,y=450)

        #Definindo os valores iniciais para as variáveis
        self._first = None
        self._last = None
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

        textAbout = open('txt/doubListAbout.txt', 'r',encoding = 'utf8')

        title = tk.Label(windowAbout,text = 'LISTA DUPLAMENTE ENCADEADA', font = ("Times", "40", "italic", "bold"), bg = COLORBG)
        title.pack()

        paragraph = tk.Label(windowAbout,text = textAbout.read(), font = ("Times","14"), bg = COLORBG, anchor = 'w')
        paragraph.pack()
        
        image = Image.open("img/doubListImg.png")
        photo = ImageTk.PhotoImage(image)
        labelImage = tk.Label(master = windowAbout,image = photo, bg = COLORBG)
        labelImage.image = photo
        labelImage.pack()

    #Método para abrir o arquivo
    def openFile(self):
        filename=fd.askopenfilename(title="Abrir arquivo",filetypes=(("Text files","*.txt"),))
        row = sum(1 for line in open(filename))//3#Verifica o número de elementos
        archive = open(filename,'r')
        while (row > 0):
            name = (archive.readline().rstrip("\n"))
            publisher = archive.readline().rstrip("\n")
            year = int(archive.readline().rstrip("\n"))
            self.addGame(name,publisher,year)#Insere na lista o elemento
            row = row - 1
      
    #Método para salvar o arquivo
    def saveFile(self):
        current = self._first
        new_file = fd.asksaveasfile(title="Salvar arquivo",
        defaultextension=".txt",
        filetypes=(("Text files","*.txt"),))
        if new_file:
            i = self._length
            while (i > 0):
                new_file.write(current.name + "\n"
                    + str(current.publisher) + "\n" + str(current.year) +"\n")
                current = current.next
                i = i - 1
            new_file.close()

    #Método auxiliar para o Canvas
    def insertAux(self,event):
        self.insert()
    
    def insert(self):
        #Criando a janela de inserção
        self.windowInsert = tk.Tk()
        self.windowInsert.geometry("320x200")
        self.windowInsert['bg'] = COLORBG

        #Criando os Labels e as caixas de entrada
        label1 = tk.Label(self.windowInsert,text = "Entre com o nome do Jogo",bg = COLORBG)
        label1.pack()
        self.entryName = tk.Entry(self.windowInsert)
        self.entryName.pack()
        label2 = tk.Label(self.windowInsert,text = "Entre com a desenvolvedora",bg = COLORBG)
        label2.pack()
        self.entryPublisher = tk.Entry(self.windowInsert)
        self.entryPublisher.pack()
        label3 = tk.Label(self.windowInsert,text = "Entre com o ano de lançamento",bg = COLORBG)
        label3.pack()
        self.entryYear = tk.Entry(self.windowInsert)
        self.entryYear.pack()

        #Criando o botão
        btn = tk.Button(self.windowInsert,text="Enviar",command=self.addGameAux,bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"))
        btn.pack()

        self.labelError = tk.Label(self.windowInsert,text = "Preencha os dados",bg = COLORBG)
        self.labelError.pack()
        self.labelError.place(x=105,y = 160)

    #Auxiliar para a inserção na lista
    def addGameAux(self):
        self.labelError.destroy()
        #Verifica se está tudo preenchido
        if((self.entryName.get() == '') or (self.entryPublisher.get() == '') or (self.entryYear.get() == '')):
            self.labelError = tk.Label(self.windowInsert,text = 'É necessário preencher todos os campos',bg = COLORBG)
            self.labelError.pack()
            self.labelError.place(x=60,y = 160)
        #Verifica se o ano é numérico
        elif(not self.entryYear.get().isnumeric()):
            self.labelError = tk.Label(self.windowInsert,text = 'Ano de lançamento precisa ser numérico',bg = COLORBG)
            self.labelError.pack()
            self.labelError.place(x=65,y = 160)
        #Pegando os elementos para inserir na lista
        else:
            name = self.entryName.get()
            publisher = self.entryPublisher.get()
            year = int(self.entryYear.get())
            self.windowInsert.destroy()
            self.addGame(name,publisher,year)#Chamando a inserção da lista
       
    #Método que insere na lista
    def addGame(self,name,publisher,year):
        current = self._first
        previous = None
        while (current != None and current.name < name):
            previous = current
            current = current.next
        if(self._length == 0):
            current = NodeGameList(name,publisher,year,None,None)
            self._first = current
            self._last = current
        elif previous == None:
            current = NodeGameList(name,publisher,year,self._first,None)
            self._first.prev = current
            self._first = current
        elif current == None:
            current = NodeGameList(name,publisher,year,None,self._last)
            previous.next = current
            self._last = current
        else:
            current = NodeGameList(name,publisher,year,previous.next,previous)
            previous.next.prev = current
            previous.next = current
        self._length = self._length + 1
        self.printCanvas()

    #Método auxiliar para o canvas
    def removeAux(self,event):
        self.remove()

    def remove(self):
        #Criação da janela de remoção
        self.windowRemove = tk.Tk()
        self.windowRemove.geometry("200x100")
        self.windowRemove['bg'] = COLORBG

        #Criando os Labels e as caixas de entrada
        label = tk.Label(self.windowRemove,text = "Entre com o nome do Jogo",bg = COLORBG)
        label.pack()
        self.removeName = tk.Entry(self.windowRemove)
        self.removeName.pack()

        btnRemove = tk.Button(self.windowRemove,text="Remover da Lista",bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"),command=self.removeGame)
        btnRemove.pack()

    #Método para a remoção do jogo da lista
    def removeGame(self):
        #Não precisa verificar se não foi preenchido
        #Caso o entry não tenha sido preenchido o jogo não será encontrado
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
        if current == self._last:
            self._last = current.prev
        else:
            current.next.prev = previous
        self._length = self._length - 1
        self.windowRemove.destroy()
        self.printCanvas()
        return True

    #Método para buscar um jogo na lista
    def search(self):
        #Criando a janela de busca
        self.windowsearch = tk.Tk()
        self.windowsearch.geometry("200x100")
        self.windowsearch['bg'] = COLORBG

        #Criando os Labels e as caixas de entrada
        label = tk.Label(self.windowsearch,text = "Entre com o nomo do jogo",bg = COLORBG)
        label.pack()
        self.searchName = tk.Entry(self.windowsearch)
        self.searchName.pack()

        btnsearch = tk.Button(self.windowsearch,text="Buscar na lista",command=self.searchGame,bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"))
        btnsearch.pack()

        self.labelError = tk.Label(self.windowsearch, text = '')
        self.labelError.pack()
    
    #Buscando o jogo na lista
    def searchGame(self):
        self.labelError.destroy()
        #Verificando se foi preenchido
        if(self.searchName.get() == ''):
            self.labelError = tk.Label(self.windowsearch,text = 'É necessário preencher corretamente',bg = COLORBG)
            self.labelError.pack()
        else:
            current = self._first
            name = self.searchName.get()
            #Procurando o jogo na lista
            while (current != None and current.name != name):
                current = current.next
            #O jogo não foi encontrado
            if current == None:
                self.windowsearch.destroy()
                windowPrint = tk.Tk()
                labelPrint = tk.Label(windowPrint,text = "O jogo não está presente na lista",bg = COLORBG,font = ("Times","10","bold"))
                labelPrint.pack()
                return False
            self.windowsearch.destroy()
            #O jogo foi encontrado
            windowPrint = tk.Tk()
            labelPrint = tk.Label(windowPrint,text = "O Jogo está presente na lista\n"
                + "Nome:\n" + current.name + "\nDesenvolvedora\n" + str(current.publisher) + 
                "\nAno:\n" + str(current.year),bg = COLORBG,font = ("Times","10","bold"))
            labelPrint.pack()
            return True

    #Mostrando os jogos em ordem crescente pelo nome
    def ascendingOrder(self):
        #Cria a janela
        windowAscending = tk.Tk()
        windowAscending['bg'] = COLORBG
        current = self._first
        i = 1
        text = ""#Texto que será inserido

        #Insere um jogo por linha
        while current != None:
            text = text +  str(i) + "º Jogo - " + "Nome: " + current.name + " Desenvolvedora: " + current.publisher + " Ano de lançamento: " + str(current.year) + "\n"
            i = i + 1
            current = current.next 
        
        #Criando um label com os jogos em ordem crescente
        labelAscending = tk.Label(windowAscending, text = text, font = ("Times", "14"),bg = COLORBG)
        labelAscending.pack()
    
    #Mostrando os jogos em ordem decrescente pelo nome
    def descendingOrder(self):
        #Cria a janela
        windowDescending = tk.Tk()
        windowDescending['bg'] = COLORBG
        current = self._last
        i = 1
        text = ""
        #Insere um jogo por linha
        while current != None:
            text = text +  str(i) + "º Jogo - " + "Nome: " + current.name + " Desenvolvedora: " + current.publisher + " Ano de lançamento: " + str(current.year) + "\n"
            i = i + 1
            current = current.prev
        
        #Criando um label com os jogos em ordem crescente
        labelDescending = tk.Label(windowDescending, text = text, font = ("Times", "14"),bg = COLORBG)
        labelDescending.pack()

    #Método para desenhar no canvas
    def printCanvas(self):
        i = self._length 
        current = self._first
        self.canvasDoubList.delete('all')
        locationX = 40
        while i > 0:
            self.canvasDoubList.create_text(locationX+40,350,text = "Nome:\n" + current.name[:13]
                + "\n\nAno:\n" + str(current.year))
            self.canvasDoubList.create_rectangle(locationX,300,locationX+80,400)

            #Desenha a seta para a direita
            self.canvasDoubList.create_line(locationX+80,330,locationX+95,330)   
            self.canvasDoubList.create_line(locationX+95,320,locationX+95,340)  
            self.canvasDoubList.create_line(locationX+95,320,locationX+100,330)
            self.canvasDoubList.create_line(locationX+95,340,locationX+100,330)   

            #Desenha a seta para a esquerda
            self.canvasDoubList.create_line(locationX,370,locationX-15,370)   
            self.canvasDoubList.create_line(locationX-15,360,locationX-15,380)  
            self.canvasDoubList.create_line(locationX-15,360,locationX-20,370)
            self.canvasDoubList.create_line(locationX-15,380,locationX-20,370)  
            self.canvasDoubList.update()
            locationX = locationX + 100
            current = current.next
            i = i - 1

    #Método para remover todos os elementos da lista
    def deleteAll(self):
        self.canvasDoubList.delete('all')
        self._first = None
        self._last = None
        self._length = 0