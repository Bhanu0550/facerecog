from bs4 import BeautifulSoup
import requests

url='http://www.studyguideindia.com/Colleges/Engineering/chandigarh-college-of-engineering-technology.html'
res = requests.get(url).content
soup = BeautifulSoup(res, 'lxml')
t1=soup.find("div",{"id":"college_details-new"})
data=t1.find("div",{"id":"clg_dtl"})
data2=data.find('table',{"class":"altcolor1"})
tds=data2.findAll('td')
stngs=tds[1].find('strong')
print(stngs.text)
print(tds[15].text)
