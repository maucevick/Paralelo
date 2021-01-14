

from multiprocessing.dummy import Pool as ThreadPool
import urllib3

pool = ThreadPool(4) 

urls = [
'https://www.python.org', 'https://www.yahoo.com',
'https://www.google.com', 'http://pythondiario.com'
]

results = pool.map(urllib3.connection_from_url, urls)

for re in results:
    print(re)

pool.close() 
pool.join()


