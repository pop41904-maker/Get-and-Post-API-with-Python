from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from data.data import *
import uuid, hashlib

def create_salt() -> str:
    return str(uuid.uuid4())
def hashing_data(Password : str, Salt : str) -> str:
    return hashlib.sha512((Password + Salt).encode()).hexdigest()

app = FastAPI()

class UserSchema(BaseModel) :
    Name : str = Field(min_length=2, max_length=18)
    Password : str = Field(min_length=6)
    Email : EmailStr

try :
    con = connect_DB()
    cur = cursor_connect(con)

    cur.execute("""CREATE TABLE IF NOT EXISTS Users(
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Password TEXT NOT NULL,
        Salt TEXT NOT NULL,
        Email TEXT NOT NULL
    )
    """)
finally :
    con.close()

@app.post('/user', tags=['Create User'])
def registrate_account(User : UserSchema) :
    try :
        con = connect_DB()
        cur = cursor_connect(con)

        Salt = create_salt()
        Password = hashing_data(User.Password, Salt)

        cur.execute("INSERT INTO Users(Name, Password, Salt, Email) VALUES(?,?,?,?)", (User.Name, Password, Salt, User.Email))
        con.commit()
        return {"massage": True, "User status was create" : True}
    finally :
        con.close()