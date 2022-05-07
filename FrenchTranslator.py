#French Translator
#Hayden Decker
#10/1/2021
#This program will accept user input and search through a 2D list to find its corresponding french word.
#This program also allows you to add or remove translations to the english_to_french file.


from tkinter import *
from tkinter import filedialog

def main(): #Creation of main function. This function creates the myGUI object translatorGUI and starts tkinter mainloop.
    translatorGUI = MyGUI()
    mainloop()

def readFile(filename): #This function opens the english_to_french.txt file and strips all whitespace and split at the tab from the text. The strings will then be appended to the languageList list and returned.
    with open(filename, 'r') as languageFile:
        languageList = []
        for line in languageFile:
            english, french = line.split("\t", 1)
            french = french.strip()
            languageList.append([english, french])
        return languageList

class MyGUI:
    languageList = readFile("english_to_french.txt") #MyGUI attribute languageList is for other methods and constructor to access the list.

    def __init__(self):
        self.window = Tk() #This statements create a tkinter window, names it, and gives it an appropriate size.
        self.window.title("Translator")
        self.window.geometry('200x100')

        menuBar = Menu(self.window) #These statements create the menu bar and add it to the window.
        self.window.config(menu = menuBar)

        fileMenu = Menu(menuBar,tearoff=0) #The below statements create a cascading menu called fileMenu. Then open, save, and exit commands are added to the menu.
        menuBar.add_cascade(label = "File", menu = fileMenu)
        fileMenu.add_command(label = "Open", command = self.processOpen)
        fileMenu.add_command(label = "Save", command = self.update)
        fileMenu.add_command(label = "Exit", command = self.exit)

        editMenu = Menu(menuBar,tearoff=0) #editMenu is another cascading menu added to the menu bar. It's commands are list dictionary, add word, and delete word.
        menuBar.add_cascade(label = "Edit", menu = editMenu)
        editMenu.add_command(label = "List dictionary", command = self.displayAll)
        editMenu.add_command(label = "Add word", command = self.addWord)
        editMenu.add_command(label = "Delete word", command = self.deleteWord)

        self.topFrame = Frame(self.window) #Creation and positioning of topFrame.
        self.topFrame.grid(row = 0, column = 0)

        self.bottomFrame = Frame(self.window)#Creation and postioning of bottomFrame
        self.bottomFrame.grid(row = 1, column = 0)

        self.topFrame.grid_rowconfigure(0, weight = 1) #Below are statements used to make the top frame and bottom frame span the entire window so widgets can be centered.
        self.topFrame.grid_columnconfigure(0, weight = 1) 

        self.bottomFrame.grid_rowconfigure(0, weight = 1)
        self.bottomFrame.grid_columnconfigure(0, weight = 1) 

        self.window.grid_rowconfigure(0, weight = 1)
        self.window.grid_columnconfigure(0, weight = 1)

        self.output = StringVar()

        self.labelOutput = Label(self.bottomFrame, textvariable=self.output) #These lines create the label output widget.
        self.labelOutput.grid(row = 0, column = 0, columnspan = 2)

        self.englishEntry = Entry(self.topFrame, width=10) #These lines are for the english entry field widget.
        self.englishEntry.grid(row = 0, column = 0)

        self.frenchEntry = Entry(self.topFrame, width=10)#These lines are for the french entry field widget.
        self.frenchEntry.grid(row = 0, column = 1)

        self.translateButton = Button(self.topFrame, text = "TRANSLATE", command = self.translateToFrench) #These statements are used to create the translate button with it's method command translateToFrench.
        self.translateButton.grid(row = 1, column = 0, columnspan= 2)
        
    def processOpen(self): #This method is used to open file explorer and return the file name to the readFile function. 
        filename = filedialog.askopenfilename() 
        readFile(filename)

    def displayAll(self): #This method iterates through the 2D list and appends each element to the labelOutput text field.
        self.window.geometry('250x1000')
        self.output.set("")
        for i in range(len(self.languageList)):
            for j in range(len(self.languageList[i])):
                self.output.set(self.output.get() + self.languageList[i][j] + " ")
            self.output.set(self.output.get() + "\n")
    
    def translateToFrench(self): #This method iterates through the 2D list and compares the englishEntry field contents to the last element in each sublist and sets labelOutput to it if they match.
        self.window.geometry('200x100')
        for i in range(len(self.languageList)):
            for j in range(len(self.languageList[i])):
                if self.englishEntry.get() == self.languageList[i][j]:
                    self.output.set(self.languageList[i][-1])
    
    def addWord(self): #This method checks if both entry fields are not null and then appends both fields contents to the languageList list.
        if len(self.englishEntry.get()) != 0 and len(self.frenchEntry.get()) != 0:
            self.languageList.append([self.englishEntry.get(),self.frenchEntry.get()])

    def deleteWord(self): #This method iterates through each sublist in the 2D list and removes the sublist if it contains the english text field input.
        for i in self.languageList:
            if self.englishEntry.get() in i:
                self.languageList.remove(i)

    def update(self): #This method iterates through the 2D list and copies it's contents over to the languageFile with the writelines function.
        with open("english_to_french.txt", 'w') as languageFile:
            for i in range(len(self.languageList)):
                for j in range(len(self.languageList[i])):
                    languageFile.writelines(self.languageList[i][j] + "\t")
                languageFile.writelines("\n")
    def exit(self): #This method calls the update method to save the file and then calls the exit function to close the program.
        self.update()
        exit()

main()