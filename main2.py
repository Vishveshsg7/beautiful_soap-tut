from bs4 import BeautifulSoup
import requests

html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35").text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('li', class_= 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_='joblist-comp-name')
print(company_name)
