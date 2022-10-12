from unicodedata import name
import requests
from tinydb import TinyDB

def add():
    db = TinyDB('db.json')
    url = 'http://127.0.0.1:8000/add/'
    db.default_table_name = 'Vivo'
    for i in db.all():
        dict_p = {}
        dict_p['name'] = i.get('name')
        dict_p["company"] = i.get("company"),
        dict_p["color"] =  i.get("color"),
        dict_p["RAM"] =i.get("RAM"),
        dict_p["memory"] = i.get("memory"),
        dict_p["price"] =i.get("price"),
        dict_p["img_url"] =i.get("img_url")
        r = requests.post(url, data=dict_p)
    return db.all()
add()