import json
import requests, time
import traceback
import logging

def test(url, method, id='', body ={}): 
    start = time.time()
    if id == '':
        try:
            if method == 'GET':
                res = requests.get(url)
            if method == 'POST':
                res = requests.post(url, json=body)
        except Exception as e:
            logging.error(traceback.format_exc())
    else:
        try: 
            if method == 'GET':
                res = requests.get(url+f'/{id}/id')
            if method == 'DELETE':
                res = requests.delete(url+f'/{id}')
        except Exception as e:
            logging.error(traceback.format_exc())
    end = time.time()
    delta = (end-start)*100
    print(f'{method} {url} with status {res.status_code} ------ time: {delta}ms')

if __name__ == "__main__":
    port = "5000"
    url = f'http://127.0.0.1:{port}'
    # test(f'{url}/publications', "POST", body={"title": "Test Title", "content": "Test Content"})
    # test("{url}/publications", "DELETE", id="1")
    # test("{url}/publications", "GET", id="1")
    print("---------------SUTE FOR PUBLICATIONS--------------")
    test(f'{url}/publications', "GET")
    test(f'{url}/publications/hashtags', "GET")


