
# for excel 2010 up 
import openpyxl , os , shutil , glob

class ie_excel:
    def __init__(self):
        self.path = os.path.abspath(".")
        self.pop_path = os.path.dirname(self.path)

    def __str__(self):
        print("hi")
    def create_folder(self):
        isfolder_exist = os.path.isdir("/as")
        print(isfolder_exist)
        print(os.listdir(self.path))
        #if not os.path.exists('hi.txt'):
            #shutil.copyfile('hi.txt','hi2.txt')
            #print(islink)
    

a = ie_excel().create_folder()
