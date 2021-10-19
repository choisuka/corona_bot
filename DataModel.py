from urllib import request
from bs4 import BeautifulSoup
 

class DataModel():
    def __init__(self):
        self.target = request.urlopen("http://ncov.mohw.go.kr/")
        self.soup = BeautifulSoup(self.target, "html.parser")      
        self.nums = []

    def gen_message(self):
        for item in self.soup.select("div.datalist"):
            for data in item.select("span.data"):
                self.nums.append(int(data.string.replace(",","")))

                

        message = "오늘 코로나 확진자수: " + str(sum(self.nums)) + "명"
        return message

 
