import requests 
r = requests.get('https://dogapi.dog/api/v2/facts')
def decorator():
    def wrapper():
        print(r.json()["data"][0]["attributes"]["body"])
    return wrapper
a = decorator()
a()
