import requests
import csv
from json import dumps

def scrapping_data(file):
    with open ("관서별_5대범죄_발생_및_검거_현황_2000_2016_/" + file, newline='', encoding='euc-kr') as csvfile:

        data = csv.reader(csvfile)
        temp_dict = {}
        year = file.split("│")[0]
        for row in data:
            temp_dict["year"] = year
            temp_dict["area"] = "서울"
            temp_dict["location"] = row[0]
            temp_dict["type"] = row[1]
            if(row[2] == "발생"):
                temp_dict["occur"] = row[3]
            else:
                temp_dict["arrest"] = row[3]
                requests.post("http://localhost/api/crime/", data=temp_dict)
            

if __name__ == "__main__":

    scrapping_data("2000│т.csv")