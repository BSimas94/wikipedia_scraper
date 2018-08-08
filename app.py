import pyodbc
import wikipedia as wiki
from bs4 import BeautifulSoup
import re

# CREATE THE CONNECTION
cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};"
                        "Server=172.17.0.2;"
                        "Port=1433;"
                        "Database=wikipedia;"
                        "uid=sa;pwd=reallyStrongPwd123")


# CREATE CURSOR AND SELECT THE DATABASE
curs = cnxn.cursor()
curs.execute("USE wikipedia")


# SCRAPE DATA FROM A SPECIFIED PAGE
i = "Ex Machina (film)"
html_page = wiki.WikipediaPage(title=i).html()
soup = BeautifulSoup(html_page,features="html.parser")
links = soup.findAll('a', {'class': None})
curs.execute("INSERT INTO Page (Title, Summary, Link1Name, Link1URL, Link2Name, Link2URL, Link3Name, Link3URL, Link4Name, Link4URL, Link5Name, Link5URL) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
wiki.WikipediaPage(title=i).title, wiki.WikipediaPage(title=i).summary,
links[0].get('title'),'https://en.wikipedia.org' + links[0].get('href'),
links[1].get('title'),'https://en.wikipedia.org' + links[1].get('href'),
links[2].get('title'),'https://en.wikipedia.org' + links[2].get('href'),
links[3].get('title'),'https://en.wikipedia.org' + links[3].get('href'),
links[4].get('title'),'https://en.wikipedia.org' + links[4].get('href'))
cnxn.commit()


# READ DATA FROM DB
curs.execute("SELECT * FROM Page")
for row in curs.fetchall():
    print(row)