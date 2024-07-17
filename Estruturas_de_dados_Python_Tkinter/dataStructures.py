import tkinter as tk
import tkinter.filedialog as fd
import stack,queue,listMain,doubList,bsTree,avlTree
from PIL import ImageTk, Image

#Cores que podem ser utilizadas no código
COLORBG = '#F0FFFF'
COLORBUTTON = '#00BBFF'
COLORBUTTON2 = '#00DDFF'
CANVASBG = '#F8FFFF'

#Classe da janela principal do programa sobre estruturas de dados
class FirstWindow:
    def __init__(self, master=None):

        self.root = tk.Tk()
        self.root.geometry("1080x720")
        self.root['bg'] = COLORBG

        self.root.title("Initial Page")

        '''
        image = Image.open("img.jpg")
        photo = ImageTk.PhotoImage(image)
        
        self.label = tk.Label(master,width = 1080, height = 720, bg = COLORBG)   
        #self.label.image = photo
        self.label.pack()
        '''

        title = tk.Label(self.root, text = "Estruturas de Dados",bg = COLORBG)
        title["font"] = ("Times", "50", "italic", "bold")
        title.pack()
        title.place(x = 250, y = 60)

        subject = tk.Label(self.root, text = "Tópicos especiais em programação",bg = COLORBG)
        subject["font"] = ("Times", "20", "bold")
        subject.pack()
        subject.place(x = 325, y = 150)

        name = tk.Label(self.root, text = "Aluno:\nRafael Rocha Maciel",bg = COLORBG)
        name["font"] = ("Times", "20", "bold")
        name.pack()
        name.place(x = 420, y = 220)

        #adicionando botão para a pilha
        self.buttonStack = tk.Button(master = self.root, width = 20, height = 4, text = "Pilha",
        bg = COLORBUTTON,activebackground = COLORBUTTON2)
        self.buttonStack["font"] = ("Times", "18", "bold")
        self.buttonStack['command'] = self.createStack
        self.buttonStack.pack()
        self.buttonStack.place(x = 50, y = 360)

        #adicionando botão para a fila
        self.buttonQueue = tk.Button(master = self.root, width = 20, height = 4, text = "Fila",
        bg = COLORBUTTON,activebackground = COLORBUTTON2)
        self.buttonQueue["font"] = ("Times", "18", "bold")
        self.buttonQueue['command'] = self.createQueue
        self.buttonQueue.pack()
        self.buttonQueue.place(x = 400, y = 360)

        #adicionando botão para a lista encadeada
        self.buttonList = tk.Button(master = self.root, width = 20, height = 4, text = "Lista Encadeada",
        bg = COLORBUTTON,activebackground = COLORBUTTON2)
        self.buttonList["font"] = ("Times", "18", "bold")
        self.buttonList['command'] = self.createList
        self.buttonList.pack()
        self.buttonList.place(x = 750, y = 360)

        #adicionando botão para a lista duplamente encadeada
        self.buttonDoubList = tk.Button(master = self.root, width = 20, height = 4, text = "Lista Duplamente\nEncadeada",
        bg = COLORBUTTON,activebackground = COLORBUTTON2)
        self.buttonDoubList["font"] = ("Times", "18", "bold")
        self.buttonDoubList['command'] = self.createDoubList
        self.buttonDoubList.pack()
        self.buttonDoubList.place(x = 50, y = 540)

        #adicionando botão para a árvore binária de busca
        self.buttonBSTree = tk.Button(master = self.root, width = 20, height = 4, text = "Árvore Binária de Busca",
        bg = COLORBUTTON,activebackground = COLORBUTTON2)
        self.buttonBSTree["font"] = ("Times", "18", "bold")
        self.buttonBSTree['command'] = self.createBSTree
        self.buttonBSTree.pack()
        self.buttonBSTree.place(x = 400, y = 540)

        #adicionando botão para a árvore avl
        self.buttonAvlTree = tk.Button(master = self.root, width = 20, height = 4, text = "Árvore AVL",
        bg = COLORBUTTON,activebackground = COLORBUTTON2)
        self.buttonAvlTree["font"] = ("Times", "18", "bold")
        self.buttonAvlTree['command'] = self.createAvlTree
        self.buttonAvlTree.pack()
        self.buttonAvlTree.place(x = 750, y = 540)

        self.root.mainloop()

    #Método para a criação da pilha
    def createStack(self):
        self.root.destroy()
        stack.StackWindow()

    #Método para a criação da fila
    def createQueue(self):
        self.root.destroy()
        queue.QueueWindow()

    #Método para a criação da lista encadeada
    def createList(self):
        self.root.destroy()
        listMain.ListWindow()

    #Método para a criação da lista duplamente encadeada  
    def createDoubList(self):
        self.root.destroy()
        doubList.DoubListWindow()

    #Método para a criação da árvore binária de busca  
    def createBSTree(self):
        self.root.destroy()
        bsTree.BSTreeWindow()

    #Método para a criação da árvore avl
    def createAvlTree(self):
        self.root.destroy()
        avlTree.AvlTreeWindow()

