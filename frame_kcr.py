
from tkinter import Tk, Frame, Menu

class Example(Frame):
  
    def __init__(self,*menu):
        super().__init__() 
         
        self.initUI(*menu)
        self.menu_bar_index=[1,2,3]
        
        
    def initUI(self,*menu):
      
        self.master.title("ElanHome[520489]")
        self.muna_bar()
       

    def onExit(self):
        
        self.quit()

    def muna_bar(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)        
        fileMenu = Menu(menubar)           
        submenu = Menu(fileMenu)      
        submenu.add_command(label="New feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")
        fileMenu.add_cascade(label='Import', menu=submenu, underline=0)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)        
                
def main():
  
    root = Tk()
    root.geometry("480x320+150+150")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()   