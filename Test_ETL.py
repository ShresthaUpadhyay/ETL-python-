import unittest
from reader import Reader
from tranformer import Transformation
from loader import Load

class TestETL(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        self.reading_file = Reader(r'C:\Users\Shrestha\Desktop\testing file.txt')
        self.tranformation = Transformation()

    @classmethod
    def tearDown(self) -> None:
        self.reading_file.closefile()

    def test_reader(self):
        """ Testing the getData() of reader class"""
        self.assertEqual(self.reading_file.getData(),"Hello World!")
    
    def test_transformer(self):
        # Testing tranformation_1() and transformation_2() of Transformation class
        read_data_1 = "hello world!"

        self.assertEqual(self.tranformation.transformation_1(read_data_1),"HELLO WORLD!")

        read_data_2 =  "Hello world, hello"

        self.assertEqual(self.tranformation.transformation_2(read_data_2),[('hello',2),('world',1)])
    
    def test_loader(self):
        # Testing loader_t1 and loader_t2 function of Loader class
        tranformed_data_1 = "HELLO WORLD!"
        transformed_data_2 = [('hello',1),('world',1)]

        loadingfile = open(r"C:\Users\Shrestha\Desktop\test loader.txt","w")

        l = Load()

        l.loader_T1(tranformed_data_1,loadingfile)
        loadingfile.close()

        test_read = Reader(r"C:\Users\Shrestha\Desktop\test loader.txt")    
        self.assertEqual(test_read.getData(),"HELLO WORLD!")
        test_read.closefile()

        loadingfile2 = open(r"C:\Users\Shrestha\Desktop\test loader2.txt","w")
        
        l.loader_T2(transformed_data_2,loadingfile2)
        loadingfile2.close()

        test_read2 = Reader(r"C:\Users\Shrestha\Desktop\test loader2.txt")
        self.assertEqual(test_read2.getData(),'hello -> 1\nworld -> 1\n')
        test_read2.closefile()


    

if __name__ == "__main__":
    unittest.main()