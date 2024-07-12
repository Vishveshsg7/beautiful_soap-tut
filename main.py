from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    tags = soup.find_all('h2')
    #print(tags)
    for course in tags:
        print(course.text) #to extract the text from the selected tags