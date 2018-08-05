import pyodbc
import wikipedia as wiki
from BeautifulSoup import BeautifulSoup
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


# SCRAPE 1000 RANDOM PAGES FROM WIKIPEDIA
pages = wiki.random(pages=10)
count1 = 0
while count1 < 100:
    for i in pages:
        try:
            curs.execute("INSERT INTO Page (Title, Summary) VALUES (?, ?)",
            (wiki.WikipediaPage(title=i).title, wiki.WikipediaPage(title=i).summary))
            html_page = wiki.WikipediaPage(title=i).html()
            soup = BeautifulSoup(html_page)
            links = soup.findAll('a', {'class': None})
            curs.execute("UPDATE Page SET Link1Name = ? WHERE Title = ?",
            (links[0].get('title'), wiki.WikipediaPage(title=i).title))
            curs.execute("UPDATE Page SET Link1URL = ? WHERE Title = ?",
            ('https://en.wikipedia.org' + links[0].get('href'), wiki.WikipediaPage(title=i).title))
            curs.execute("UPDATE Page SET Link2Name = ? WHERE Title = ?",
            (links[1].get('title'), wiki.WikipediaPage(title=i).title))
            curs.execute("UPDATE Page SET Link2URL = ? WHERE Title = ?",
            ('https://en.wikipedia.org' + links[1].get('href'), wiki.WikipediaPage(title=i).title))
            curs.execute("UPDATE Page SET Link3Name = ? WHERE Title = ?",
            (links[2].get('title'), wiki.WikipediaPage(title=i).title))
            curs.execute("UPDATE Page SET Link3URL = ? WHERE Title = ?",
            ('https://en.wikipedia.org' + links[2].get('href'), wiki.WikipediaPage(title=i).title))
            curs.execute("UPDATE Page SET Link4Name = ? WHERE Title = ?",
            (links[3].get('title'), wiki.WikipediaPage(title=i).title))
            curs.execute("UPDATE Page SET Link4URL = ? WHERE Title = ?",
            ('https://en.wikipedia.org' + links[3].get('href'), wiki.WikipediaPage(title=i).title))
            curs.execute("UPDATE Page SET Link5Name = ? WHERE Title = ?",
            (links[4].get('title'), wiki.WikipediaPage(title=i).title))
            curs.execute("UPDATE Page SET Link5URL = ? WHERE Title = ?",
            ('https://en.wikipedia.org' + links[4].get('href'), wiki.WikipediaPage(title=i).title))
            cnxn.commit()
        except:
            pass
    count1 += 1
    pages = wiki.random(pages=10)


# READ DATA FROM DB
curs.execute("SELECT * FROM Page")
for row in curs.fetchall():
    print(row)