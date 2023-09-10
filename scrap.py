import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
# first step 
result=requests.get("https://wuzzuf.net/search/jobs/?q=ui+ux&a=hpb")
# we need from this link the content so we have to use this function 
src=result.content

#to manipulate this content and scrap frome website we have tu use beautiful soup 
soup= BeautifulSoup(src,"lxml")
# here we manipulate the html code 
titles_job=soup.find_all("h2",{"class":"css-m604qf"})
names_company=soup.find_all("a",{"class":"css-17s97q8"})
names_locations=soup.find_all("span",{"class":"css-5wys0k"})
skills_job=soup.find_all("div",{"class":"css-y4udm8"})
link=soup.find_all("a",{"class":})

links=[]
title_job=[]
name_company=[]
name_locations=[]
skill_job=[]
salary=[]
# here we have to enter to the list and gets only the textcontent
for i in range(len(titles_job)):
  title_job.append(titles_job[i].text)
  name_company.append(names_company[i].text)
  name_locations.append(names_locations[i].text)
  skill_job.append(skills_job[i].text)

  

    

file_list=[title_job,name_company,name_locations,skill_job,links,salary]
exported=zip_longest(*file_list)
with open("/Users/pc/Desktop/Py projects/Web scraping/classeur.csv","w")as myfile:
 wr=csv.writer(myfile)
 wr.writerow(["title_job","name_company"," name_locations","skill_job","salaries"])
 wr.writerows(exported)

 
 for link in links:
    print(f"---------------------------------------------------------------------------- ", link)
    result2=requests.get(link)
    src2=result2.content
    soup2= BeautifulSoup(src2,"lxml")
    
   
    