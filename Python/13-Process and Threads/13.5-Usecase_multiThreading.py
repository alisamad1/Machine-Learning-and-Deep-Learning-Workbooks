'''
Real-World Example: MultiThreading for I/O bounds tasks
Web Scraping often involves making numerous network requests to fetch web pages.
These tasks are I/O bound because they spend a lot of time waiting for these responses from servers. Multithreading can significantly improve the performance
by allowing multiple webpages to be fetched concurrently.
'''
'''
https://www.langchain.com/langgraph

https://www.langchain.com/langsmith

https://www.langchain.com/langchain
'''
import threading
import requests
import bs4
urls=[
    'https://www.langchain.com/langgraph',
    'https://www.langchain.com/langsmith',
    'https://www.langchain.com/langchain',
]
def fetch_contents(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched{len(soup.text)} characters from {url}')

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print("all Webpages are fetched")