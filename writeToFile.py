
import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser")

open_file = open('myFileTest03.txt', 'w')
open_file.write('test of text')   
open_file.close()  
