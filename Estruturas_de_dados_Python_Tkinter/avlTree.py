#---Observação---
#Todos os métodos são quase iguais com os usados na árvore binária de busca
#A maior diferença está na implementação da inserção e remoção

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

#Classe do nó da árvore avl
class NodeAvl: 
    def __init__(self, val): 
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

#Classe da árvore avl
class AvlTreeWindow(tk.Tk):
    def __init__(self, master = None):
        #---CRIANDO A JANELA---
        #Janela principal da queue
        self.window = tk.Tk()
        self.window.title("Árvore Avl")
        self.window.geometry("1280x720")
        self.window["bg"] = COLORBG

        #Canvas para a janela
        self.canvasAvl = tk.Canvas(self.window,width = 1180, height = 720, bg = CANVASBG)   
        self.canvasAvl.bind('<Button-1>',self.insertWindowAux)
        self.canvasAvl.bind('<Button-3>',self.removeWindowAux) 
        self.canvasAvl.pack()
        self.canvasAvl.place(x=100,y=0)

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

        #Inserindo os botões na janela
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

        #definindo os parâmetros iniciais
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

        rows = sum(1 for line in open(filename))
        archive = open(filename,'r')
        while rows > 0:
            op = archive.readline().rstrip("\n")
            valor = archive.readline().rstrip("\n")
            self.archiveSave.append(op)
            self.archiveSave.append(valor)
            if(op == 'i'):
                self._root = self.insert(self._root,int(valor))
            elif(op == 'r'):
                self._root = self.remove(self._root,int(valor))
            rows = rows - 1
        
        self.printCanvas(self._root,LOCALIZAX[0],40,1,0,"none")
    
    #Método que mostra informações sobre a estrutura
    def about(self, master = None):
        windowAbout = tk.Toplevel()
        windowAbout.geometry("1280x720")
        windowAbout['bg'] = COLORBG

        textAbout = open('txt/avlAbout.txt', 'r',encoding = 'utf8')

        title = tk.Label(windowAbout,text = 'ÁRVORE AVL', font = ("Times", "40", "italic", "bold"), bg = COLORBG)
        title.pack()

        paragraph = tk.Label(windowAbout,text = textAbout.read(), font = ("Times","14"), bg = COLORBG, anchor = 'w')
        paragraph.pack()
        
        image = Image.open("img/AVLTreeImg.gif")
        image = image.resize((500, 220), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        labelImage = tk.Label(master = windowAbout,image = photo, bg = COLORBG)
        labelImage.image = photo
        labelImage.pack()
    
    #Método auxiliar para o canvas
    def insertWindowAux(self,event):
        self.insertWindow()

    #Janela de inserção
    def insertWindow(self):
        self.windowInsert = tk.Tk()
        self.windowInsert.geometry("240x120")
        self.windowInsert['bg'] = COLORBG

        label1 = tk.Label(self.windowInsert,text = "Entre com a chave:",bg = COLORBG)
        label1.pack()
        self.entryval = tk.Entry(self.windowInsert)
        self.entryval.pack()

        #Criando o botão
        btn = tk.Button(self.windowInsert,text="Enviar",command=self.insertAux,bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"))
        btn.pack()

        self.labelError = tk.Label(self.windowInsert,text = "Preencha os dados",bg = COLORBG)
        self.labelError.pack()

    #Verificando o elemento para a inserção
    def insertAux(self):
        self.labelError.destroy()
        if(self.entryval.get() == ''):
            self.labelError = tk.Label(self.windowInsert,text = "É necessário preencher com um valor",bg = COLORBG)
            self.labelError.pack()
        elif(not self.entryval.get().isnumeric()):
            self.labelError = tk.Label(self.windowInsert,text = "É necessário que seja um valor inteiro",bg = COLORBG)
            self.labelError.pack()
        else:
            valor = self.entryval.get()
            self.archiveSave.append('i')
            self.archiveSave.append(valor)
            self._root = self.insert(self._root,int(valor))#Chamando a inserção de um elemento
            self.canvasAvl.delete("all")
            self.printCanvas(self._root,LOCALIZAX[0],40,1,0,"none")
            self.windowInsert.destroy()

#----Deixei os comentários dessa função em inglês, pois aproveitei o código que eu já tinha enviado anteriormente----
    def insert(self,root, val): 
        if root is None:  
            return NodeAvl(val)  
        elif val < root.val: 
            root.left = self.insert(root.left, val) 
        else: 
            root.right = self.insert(root.right, val) 

        #modify the height of ancestor node
        if ((self.getHeight(root.left)) < self.getHeight(root.right)):
            root.height = 1 + self.getHeight(root.right)
        else:
            root.height = 1 + self.getHeight(root.left)

        #get the value of the balance factor
        balance = self.getBalance(root) 

        #---verify the balance factor---

        #case 1 - rotate left
        if balance < -1 and val > root.right.val: 
            return self.leftRotate(root) 

        #case 2 - rotate right
        if balance > 1 and val < root.left.val: 
            return self.rightRotate(root) 
    
        #case 3 - rotate right-left
        if balance < -1 and val < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 

        #case 4 - rotate left-right
        if balance > 1 and val > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
    
        #return the root
        return root 

    
    def leftRotate(self, ancestorNode): 
        newAncestorNode = ancestorNode.right 
        aux = newAncestorNode.left 

        #run the rotation
        newAncestorNode.left = ancestorNode 
        ancestorNode.right = aux 
  
        #update the nodes' height

        #update the previous ancestor node
        if(self.getHeight(ancestorNode.left) > self.getHeight(ancestorNode.right)):
            ancestorNode.height = 1 + self.getHeight(ancestorNode.left)
        else:
            ancestorNode.height = 1 + self.getHeight(ancestorNode.right)

        #update the new ancestor node
        if(self.getHeight(newAncestorNode.left) > self.getHeight(newAncestorNode.right)):
            newAncestorNode.height = 1 + self.getHeight(newAncestorNode.left)
        else:
            newAncestorNode.height = 1 + self.getHeight(newAncestorNode.right)
  
        #return the new ancestor node
        return newAncestorNode 
  
    #Function to rotate right
    def rightRotate(self, ancestorNode):  
        newAncestorNode = ancestorNode.left 
        aux = newAncestorNode.right 

        #run the rotation
        newAncestorNode.right = ancestorNode 
        ancestorNode.left = aux 
  
        #update the nodes' height

        #update the previous ancestor node
        if(self.getHeight(ancestorNode.left) > self.getHeight(ancestorNode.right)):
            ancestorNode.height = 1 + self.getHeight(ancestorNode.left)
        else:
            ancestorNode.height = 1 + self.getHeight(ancestorNode.right)

        #update the new ancestor node
        if(self.getHeight(newAncestorNode.left) > self.getHeight(newAncestorNode.right)):
            newAncestorNode.height = 1 + self.getHeight(newAncestorNode.left)
        else:
            newAncestorNode.height = 1 + self.getHeight(newAncestorNode.right)
    
        #return the new ancestor node
        return newAncestorNode 

    #return the node's height
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height  
    
    #return the balance factor
    #balance factor = left subtree's height  - right subtree's height
    def getBalance(self, root): 
        if not root: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
#----Aqui acabam os cometários em inglês-----

    #Função auxiliar para o canvas
    def removeWindowAux(self, event):
        self.removeWindow()

    #Janela de remoção
    def removeWindow(self):
        self.windowRemove = tk.Tk()
        self.windowRemove.geometry("240x120")
        self.windowRemove['bg'] = COLORBG

        label1 = tk.Label(self.windowRemove,text = "Entre com a chave a ser removida:",bg = COLORBG)
        label1.pack()
        self.entryval = tk.Entry(self.windowRemove)
        self.entryval.pack()

        #Criando o botão
        btn = tk.Button(self.windowRemove,text="Enviar",command=self.removeAux,bg = COLORBUTTON,
        activebackground = COLORBUTTON2,font = ("times","10","bold"))
        btn.pack()

        self.labelError = tk.Label(self.windowRemove,text = "Preencha os dados",bg = COLORBG)
        self.labelError.pack()

    #Verificando o elemento inserido na janela de remoção
    def removeAux(self):
        self.labelError.destroy()
        if(self.entryval.get() == ''):
            self.labelError = tk.Label(self.windowRemove,text = "É necessário preencher com um valor",bg = COLORBG)
            self.labelError.pack()
        elif(not self.entryval.get().isnumeric()):
            self.labelError = tk.Label(self.windowRemove,text = "É necessário que seja um valor inteiro",bg = COLORBG)
            self.labelError.pack()
        else:
            valor = self.entryval.get()
            self.archiveSave.append('r')
            self.archiveSave.append(valor)
            self._root = self.remove(self._root,int(valor))
            self.canvasAvl.delete("all")
            self.printCanvas(self._root,LOCALIZAX[0],40,1,0,"none")
            self.windowRemove.destroy()

    #Método que verifica o nó com o menor valor de chave
    def minValueNode(self,root):
        if root is None or root.left is None: 
            return root 
  
        return self.minValueNode(root.left) 

    #Função para remover da árvore
    def remove(self, root, key): 
        #Removendo como se fosse uma árvore BST
        if not root: 
            return root 
  
        elif key < root.val: 
            root.left = self.remove(root.left, key) 
  
        elif key > root.val: 
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
            root.val = temp.val 
            root.right = self.remove(root.right, 
                                      temp.val) 
  
        # Se tiver apenas um nó, basta retorná-lo
        if root is None: 
            return root 
  
        # Alterando o tamanho do nó pai
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 
  
        # Obtendo o fator de balanceamento
        balance = self.getBalance(root) 
  
        #Verificar se está desbalanceada assim como verificado na inserção

        # Caso 1 - rotação direita
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        # Caso 2 - rotação esquerda
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
  
        # Caso 3 - Rotação esquerda-diraita 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Rotação direita-esquerda 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
    
    #Desenhando no canvas(Igual ao usado na árvore binária de busca)
    def printCanvas(self,root,locationX,locationY,row,posLOCALIZAX,direction): 

        if root: 
            if(direction == "none"):
                self.canvasAvl.create_oval(locationX-25,locationY-25,locationX+25,locationY+25)
                self.canvasAvl.create_text(locationX,locationY,text = root.val)
            if(direction == "esq"):
                self.canvasAvl.create_oval(locationX-25,locationY-25,locationX+25,locationY+25)
                self.canvasAvl.create_text(locationX,locationY,text = root.val)
                self.canvasAvl.create_line(LOCALIZAX[int((posLOCALIZAX- 1)/2)] - 18,locationY - 150+(row-1) + 18 ,locationX,locationY-25)
            if(direction == "dir"):
                self.canvasAvl.create_oval(locationX-25,locationY-25,locationX+25,locationY+25)
                self.canvasAvl.create_text(locationX,locationY,text = root.val)
                self.canvasAvl.create_line(LOCALIZAX[int((posLOCALIZAX-2)/2)]+ 18,locationY - 150+(row-1) + 18 ,locationX,locationY-25)
            if(direction == "invalid"):
                msg="A tela pode não estar apresentando todos os itens, recomenda-se remover o último elemento inserido"
                mb.showwarning("Warning",msg)
            
            if(row <= 4):
                nextEsq = int(2*posLOCALIZAX + 1)
                nextDir = int(2*posLOCALIZAX + 2)
                self.printCanvas(root.left, LOCALIZAX[nextEsq], locationY + 150-row,row+1,nextEsq,"esq") 
                self.printCanvas(root.right,LOCALIZAX[nextDir], locationY + 150-row,row+1,nextDir,"dir") 
            elif(row == 5):
                self.printCanvas(root.left, 0, 0,row+1,0,"invalid") 
                self.printCanvas(root.right,0, 0,row+1,0,"invalid") 

    #Método que limpa a tela
    def deleteAll(self):
        self.canvasAvl.delete('all')
        self._root = None
        self.archiveSave = []
    
    #Método que retorna para a janela principal
    def returnMain(self):
        self.window.destroy()
        dataStructures.FirstWindow()