# Here we are going to fetch the number of characters from three different urls
# https://www.linkedin.com/feed/
# https://courses.wscubetech.com/t/u/activeCourses
# https://www.hackerrank.com/dashboard
import threading
import requests
import time
from datetime import datetime 
from bs4 import BeautifulSoup
# Now we are going to define some list of urls through which we are going to perform the web scrapping
urls = [
    'https://docs.langchain.com/oss/python/langchain/overview',

    'https://docs.langchain.com/oss/python/langchain/quickstart',

    'https://docs.langchain.com/oss/python/langchain/install'
]

def fetch_contents(url):
    def Length(a):
        count = 0
        for x in a :
            count = count + 1
        return count
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'html.parser')
        time.sleep(1)
        print(f"fetched {Length(soup.text)} characters from {url}")
    except Exception as e:
        print(f'Not able to fetch contents from the url due to\n {e}')
        
# Now we are going to create a thread
threads = []
start_time = datetime.now().strftime("%H:%M:%S")
t1 = time.time()
print(f'The process started at\n {start_time}')

for url in urls:
    thread = threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    
end_time = datetime.now().strftime("%H:%M:%S")
t2 = time.time() - t1
print(f'The process ended at\n {end_time}')
print(f'All the contents got successfully fetched within\n {t2} seconds.')
    
