
class Reader():
    def __init__(self,location):
        try:
            self.file = open(location,encoding="utf8")
        except FileNotFoundError:
            print("file doesnt exist!!!")      
    
    def getData(self):  
        """ This returns file data in str """ 
        file_data = ""
        for line in self.file.readlines():
            file_data += line     
        self.file.close()
        return file_data

    def closefile(self):
        return self.file.close()


