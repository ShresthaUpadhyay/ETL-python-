from csv import reader
from reader import Reader
from collections import Counter


class Transformation:

    def transformation_1(self,data):
        """ Transforms data to upper case."""
        return data.upper()

    def transformation_2(self,data):
        """ Transforms data list of tuple(word , no. of occurrence """
        data = data.replace(",","")
        data = data.replace("\n","")
        data = data.lower()
        data_list = data.split(" ")
        counter = Counter(data_list)
        most_common = counter.most_common() # makes list of tuple(word,number of occurrence)
        return most_common


  

