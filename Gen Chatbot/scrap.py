//this codes works everyday.so anyone run the script now it will take one day to execute

import requests
import sys
import bs4
from bs4 import BeautifulSoup
from lxml import html
import re
import csv
import numpy
import json

import schedule 
import time
def scrap():
    an=[]
    page = requests.get('https://www.concordia.ca/ginacody/info-systems-eng/students/faq.html')

    '''
    faq_1=bs4.BeautifulSoup(page.text,"html.parser")

    for i in faq_1.select('p'):
    answers=(i.getText())
    answers=json.dumps(answers)

    print(answers)
    for j in faq_1.select('h6'):
    questions=(j.getText())
    questions=json.dumps(questions)

    print(questions)

   # print(type(i.getText()))'''

    tree=html.fromstring(page.content)
    topics=tree.xpath("//h3[@class='title']/a/text()")
    questions=tree.xpath("//div[@class='rte']/h6/span/text()")
    answers=tree.xpath("//div[@class='rte']/p/span/text()") 
    #answers=json.loads(str(answers))
    #answers=answers.replace("\xa0", "")
    print(answers)
    #for i in answers:
    #   answers[i]=answers.replace('\xa0','')
    #answers=re.sub(r'(\s+\n)', ' ', answers)
    #print(answers)
    '''from itertools import zip_longest
    d = [questions,answers]
    export_data = zip_longest(*d, fillvalue = '')
    with open('numbers_1.csv', 'w', newline='') as json_file:
        wr = csv.writer(myfile)
        wr.writerow(( "questions","answers"))
        wr.writerows(export_data)
    myfile.close()'''
    #from itertools import zip_longest
    d=[questions,answers]
    #export_data=zip_longest(*d,fillvalue='')
    with open ('data.json','w') as json_file:
        json.dump(d,json_file)

schedule.every(86400).seconds.do(scrap)
while 1:
    schedule.run_pending()
    time.sleep(1)