from tranformer import Transformation
from reader import Reader


class Load:

    def loader_T1(self,transformed_data,file):
        """ It loads on Transformation_1 data to file """
        if transformed_data.isupper() :
            file.write(transformed_data)
        else:
            print("data is not transformed properly!")    
        

    def loader_T2(self,transformed_data,file):
        """ It loads on Transformation_2 data to file """
        for i in range(len(transformed_data)):
            key = transformed_data[i][0]
            value = transformed_data[i][1]
            file.write(f"{key} -> {value}\n")





