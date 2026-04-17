
from typing import Optional

from flask import app

import fastapi
from enum import Enum
app = fastapi.FastAPI()

@app.get("/root")
#def read_root(param1: Optional[str] = None, param2: Optional[str] = None):

def reading_roots(param1:Optional[str]=None, param2:Optional[str]=None):
     url=f"http://domainname.com/context-path/{param1}/{param2}"
     #url = f'http://some.other.api/{param1}/{param2}'
     return {'url': str(url)}

#http://127.0.0.1:8000/root?param1=value1&param2=value2
import sqlite3

conn = sqlite3.connect('example.db',check_same_thread=True)
curs = conn.cursor()

# curs.execute('''CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY,title TEXT,completed TEXT)''')

# conn.commit()

# @app.get("/sqlite3")

# def read():
#     return {"Message": "sqlite3 is working!"}


conn1 = sqlite3.connect('genes.db',check_same_thread=False)
curs = conn1.cursor()

curs.execute('''CREATE TABLE IF NOT EXISTS transcript_SNP (NMid varchar(25) PRIMARY KEY, RSid TEXT)''')
conn1.commit()


@app.get("/sqlite3_genes")
def read_genes(param1: str, param2: Optional[str] = None):
    
     curs1 = conn1.cursor()
     print (param1, param2)
     value= curs1.execute('''select * from transcript_SNP where NMid = ?''', (param1,)).fetchone()
     conn1.commit()
     return {"Message": f"selected" + str(value) + " from the database., param2 is " + str(param2), "param1": param1}



#http://127.0.0.1:8000/sqlite3_genes?param1=NM_000261&param2=rs2
