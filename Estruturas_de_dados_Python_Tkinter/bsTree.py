import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import dataStructures
from PIL import ImageTk, Image

COLORBG = '#F0FFFF'
COLORBUTTON = '#00BBFF'
COLORBUTTON2 = '#00DDFF'
CANVASBG = '#F8FFFF'

#Valores usados para a localização dos elementos no eixo X do canvas
LOCALIZAX = [592,292, 892,142, 442, 742, 1042,67, 217, 367, 517, 667, 817, 967, 1117,30, 105, 180, 255, 330, 405, 480, 555, 630, 705, 780, 855, 930, 1005, 1080, 1155]

#Classe do nó da árvore binária de busca
class NodeBST: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.key = key

#Classe da árvore binária de busca
class BSTreeWindow(tk.Tk):
    def __init__(self, master = None):
        #---CRIANDO A JANELA---
        #Janela principal da queue
        self.window = tk.Tk()
        self.window.title("Árvore Binária de Busca")
        self.window.geometry("1300x720")
        self.window["bg"] = COLORBG

        #Canvas para a janela
        self.canvasBST = tk.Canvas(self.window,width = 1180, height = 720, bg = CANVASBG)   
        self.canvasBST.bind('<Button-1>',self.insertWindowAux)
        self.canvasBST.bind('<Button-3>',self.removeWindowAux) 
        self.canvasBST.pack()
        self.canvasBST.place(x=100,y=0)

        #Menu para a janela
        menu = tk.Menu(self.window)
        file_menu = tk.Menu(menu,tearoff = 0,bg = COLORBG)
        file_menu.add_command(label="Abrir", command = self.openFile)
        file_menu.add_separator()
        file_menu.add_command(label = "Salvar",command = self.saveFile)
        menu.add_cascade(label = "Arquivo",menu = file_menu)
        menu.add_command(label = "Sobre", command = self.about)
        operation_menu = tk.Menu(menu,tearoff = 0,bg = COLORBG)
        operation_menu.add_command(label = "Inserir",command = self.insertWindow)
        operation_menu.add_command(label = "Remover",command = self.removeWindow)
        operation_menu.add_command(label = "Limpar tela",command = self.deleteAll)
        operation_menu.add_command(label = "Retornar", command = self.returnMain)
 
        menu.add_cascade(label = "Operações", menu = operation_menu)
        self.window.config(menu = menu)

        #Inserindo os butões na janela
        buttonBack = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Voltar")
        buttonBack['command'] = self.returnMain
        buttonBack.pack()
        buttonBack.place(x=10,y=400)
        buttonInsert = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Inserir")
        buttonInsert['command'] = self.insertWindow
        buttonInsert.pack()
        buttonInsert.place(x=10,y=250)
        buttonRemove = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Remover")
        buttonRemove['command'] = self.removeWindow
        buttonRemove.pack()
        buttonRemove.place(x=10,y=300)
        buttonDeleteAll = tk.Button(width = 10,height = 1,bg = COLORBUTTON,activebackground = COLORBUTTON2,font = ("times","10","bold"),text = "Limpar Tela")
        buttonDeleteAll['command'] = self.deleteAll
        buttonDeleteAll.pack()
        buttonDeleteAll.place(x=10,y=350)

        #Definindo as condições iniciais
        self._root = None
        self.archiveSave = []

    #Método para salvar um arquivo
    def saveFile(self):
        new_file = fd.asksaveasfile(title="Salvar arquivo",
        defaultextension=".txt",
        filetypes=(("Text files","*.txt"),))
        if new_file:
            for i in range(len(self.archiveSave)):
                new_file.write(self.archiveSave[i] + "\n")
            new_file.close()
    
    #Método para abrir um arquivo
    def openFile(self):
        filename=fd.askopenfilename(title="Abrir arquivo",filetypes=(("Text files","*.txt"),))

        rows = sum(1 for line in open(filename))#Verifica o número de linhas
        archive = open(filename,'r')
        while rows > 0:
            op = archive.readline().rstrip("\n")#Linha que representa a operação
            valor = archive.readline().rstrip("\n")#Linha com o valor
            self.archiveSave.append(op)
            self.archiveSave.append(valor)
            #Insere na árovre
            if(op == 'i'):
                self._root = self.insert(self._root,int(valor))
            #Remove da árvore
            elif(op == 'r'):
                self._root = self.remove(self._root,int(valor))
            rows = rows - 1
        
        self.printCanvas(self._root,LOCALIZAX[0],40,1,0,"none")#Chama o método para desenhar na tela
    
    #Método que mostra informações sobre a estrutura
    def about(self, master = None):
        windowAbout = tk.Toplevel()
        windowAbout.geometry("1280x720")
        windowAbout['bg'] = COLORBG

        textAbout = open('txt/bstAbout.txt', 'r',encoding = 'utf8')

        title = tk.Label(windowAbout,text = 'ÁRVORE BINÁRIA DE BUSCA', font = ("Times", "40", "italic", "bold"), bg = COLORBG)
        title.pack()

        paragraph = tk.Label(windowAbout,text = textAbout.read(), font = ("Times","14"), bg = COLORBG, anchor = 'w')
        paragraph.pack()
        
        image = Image.open("img/bstTreeImg.png")
        image = image.resize((500, 220), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        labelImage = tk.Label(master = windowAbout,image = photo, bg = COLORBG)
        labelImage.image = photo
        labelImage.pack()
    
    #Método auxiliar para a inserção pelo canvas
    def insertWindowAux(self,event):
        self.insertWindow()

    def insertWindow(self):
        #Cria a janela de inserção
        self.windowInsert = tk.Tk()
        self.windowInsert.geometry("240x120")
        self.windowInsert['bg'] = COLORBG

        #Criando o label e o entry
        label1 = tk.Label(self.windowInsert,text = "Entre com a chave:",bg = COLORBG)
        label1.pack()
        self.entryKey = tk.Entry(self.windowInsert)
        self.entryKey.pack()

        #Criando o botão
        btn = tk.Button(self.windowInsert,text="Enviar",command=self.insertAux,bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"))
        btn.pack()

        #Criando o label de erro
        self.labelError = tk.Label(self.windowInsert,text = "Preencha os dados",bg = COLORBG)
        self.labelError.pack()

    def insertAux(self):
        self.labelError.destroy()
        #Verificando se foi inserido
        if(self.entryKey.get() == ''):
            self.labelError = tk.Label(self.windowInsert,text = "Preencha com um valor",bg = COLORBG)
            self.labelError.pack()
        #Verificando se foi inserido um número
        elif(not self.entryKey.get().isnumeric()):
            self.labelError = tk.Label(self.windowInsert,text = "Preencha com um valor inteiro",bg = COLORBG)
            self.labelError.pack()
        #Preparando a inserção
        else:
            valor = self.entryKey.get()
            self.archiveSave.append('i')#Inserir um 'i' na lista para mostrar que é uma inserção
            self.archiveSave.append(valor)#Inserir o valor na lista usada para salvar os arquivos
            self._root = self.insert(self._root,int(valor))#Chamando o método de inserção 
            self.canvasBST.delete("all")#Limpa a tela
            self.printCanvas(self._root,LOCALIZAX[0],40,1,0,"none")#Desenha a tela com o novo nó
            self.windowInsert.destroy()

    #Método para inserção na árvore
    def insert(self,root, key): 
        if root is None: 
            return NodeBST(key) 
        else: 
            if root.key == key: 
                return root 
            elif root.key < key: 
                root.right = self.insert(root.right, key) 
            else: 
                root.left = self.insert(root.left, key) 
        return root 

    #Método auxiliar para a remoção pelo canvas
    def removeWindowAux(self, event):
        self.removeWindow()

    #Janale de remoção
    def removeWindow(self):
        #Criando a janela de remoção
        self.windowRemove = tk.Tk()
        self.windowRemove.geometry("240x120")
        self.windowRemove['bg'] = COLORBG

        label1 = tk.Label(self.windowRemove,text = "Entre com a chave a ser removida:",bg = COLORBG)
        label1.pack()
        self.entryKey = tk.Entry(self.windowRemove)
        self.entryKey.pack()

        #Criando o botão
        btn = tk.Button(self.windowRemove,text="Enviar",command=self.removeAux,bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"))
        btn.pack()

        self.labelError = tk.Label(self.windowRemove,text = "Preencha os dados",bg = COLORBG)
        self.labelError.pack()

    def removeAux(self):
        self.labelError.destroy()
        #Verificando se foi inserido
        if(self.entryKey.get() == ''):
            self.labelError = tk.Label(self.windowRemove,text = "Preencha com um valor",bg = COLORBG)
            self.labelError.pack()
        #Verificando se foi inserido um número
        elif(not self.entryKey.get().isnumeric()):
            self.labelError = tk.Label(self.windowRemove,text = "Preencha com um valor inteiro",bg = COLORBG)
            self.labelError.pack()
        #Preparando a remoção
        else:
            valor = self.entryKey.get()
            self.archiveSave.append('r')#usa 'r' para mostrar que é uma remoção para a inserção de arquivos(caso seja usada)
            self.archiveSave.append(valor)
            self._root = self.remove(self._root,int(valor))#Chama a função de remoção
            self.canvasBST.delete("all")
            self.printCanvas(self._root,LOCALIZAX[0],40,1,0,"none")
            self.windowRemove.destroy()

    #Método auxiliar para a remoção em uma árvore
    #Retorna o nó com o menor valor da árvore(o nó mais a esquerda)
    def minValueNode(self,node):
        current = node
        while(current.left is not None):
            current = current.left
 
        return current

    #Função para a remoção na árvore
    def remove(self,root, key): 
        if root is None:
            return root
        if key < root.key:
            root.left = self.remove(root.left, key)
        elif(key > root.key):
            root.right = self.remove(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.remove(root.right, temp.key)
        return root
    
    #Método para desenhar no canvas
    def printCanvas(self,root,locationX,locationY,row,posLOCALIZAX,direction): 
        if root: 
            #Verifica se é o primeiro nó
            if(direction == "none"):
                self.canvasBST.create_oval(locationX-25,locationY-25,locationX+25,locationY+25)#Desenha a oval
                self.canvasBST.create_text(locationX,locationY,text = root.key)#Desenha o número dentro da oval
            #Verifica se esse nó é inserido a esquerda
            if(direction == "esq"):
                self.canvasBST.create_oval(locationX-25,locationY-25,locationX+25,locationY+25)#Desenha a oval
                self.canvasBST.create_text(locationX,locationY,text = root.key)#Desenha o número dentro da oval
                self.canvasBST.create_line(LOCALIZAX[int((posLOCALIZAX- 1)/2)] - 18,locationY - 150+(row-1) + 18 ,locationX,locationY-25)#Desenha a ligação
            #Verifica se esse nó é inserido a direita
            if(direction == "dir"):
                self.canvasBST.create_oval(locationX-25,locationY-25,locationX+25,locationY+25)#Desenha a oval
                self.canvasBST.create_text(locationX,locationY,text = root.key)#Desenha o número dentro da oval
                self.canvasBST.create_line(LOCALIZAX[int((posLOCALIZAX-2)/2)]+ 18,locationY - 150+(row-1) + 18 ,locationX,locationY-25)#Desenha a ligação
            #Verifica se o nó não pode ser exibido na tela
            if(direction == "invalid"):
                #Mostra na tela um warning
                msg="A tela pode não estar apresentando todos os itens, recomenda-se remover o último elemento inserido"
                mb.showwarning("Warning",msg)
            
            #Verifica o número de linhas, para o máximo de inserção
            #Valores maiores não cabem na tela
            if(row <= 4):
                nextEsq = int(2*posLOCALIZAX + 1)#Verifica qual o próximo valor no eixo x para o elemento da esquerda
                nextDir = int(2*posLOCALIZAX + 2)#Verifica qual o próximo valor no eixo x para o elemento da esquerda
                self.printCanvas(root.left, LOCALIZAX[nextEsq], locationY + 150-row,row+1,nextEsq,"esq") #Chama a função para a esquerda da árvore
                self.printCanvas(root.right,LOCALIZAX[nextDir], locationY + 150-row,row+1,nextDir,"dir") #Chama a função para a direita da árvore
            #Manda os elementos com a direção inválida
            elif(row == 5):
                self.printCanvas(root.left, 0, 0,row+1,0,"invalid") 
                self.printCanvas(root.right,0, 0,row+1,0,"invalid") 

    #Método que limpa a tela
    def deleteAll(self):
        self.canvasBST.delete('all')
        self._root = None
        self.archiveSave = []
    
    #Método que retorna a janela principal
    def returnMain(self):
        self.window.destroy()
        dataStructures.FirstWindow()

