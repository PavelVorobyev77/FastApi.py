import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends
from sqlalchemy import *
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from urllib import parse


db_username = 'DESKTOP-BK1T0PD\pasch'
db_password = ''
server_name = 'DESKTOP-BK1T0PD\SQLEXPRESS'
db_name = '21.102-08-VP_PM'
db_url = (f"mssql+pyodbc://{db_username}:{db_password}@{server_name}/{db_name}?"
          f"driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes")
engine = create_engine(db_url)

app = FastAPI()

class Base(DeclarativeBase): pass
class Clients(Base):
    __tablename__ = "Clients"

    ID_Client = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ClientName = Column(String)
    ClientSurname = Column(String)
    ClientPatronymic = Column(String)
    phoneNumber = Column(String)
    Client_login = Column(String)
    Client_pswd = Column(String)


class ConstructionMaterials(Base):
    __tablename__ = "ConstructionMaterials"

    ID_ConstMaterial = Column(Integer, primary_key=True, index=True, autoincrement=True)
    MaterialName = Column(String)
    Quantity = Column(Integer)

class FinishingMaterials(Base):
    __tablename__ = "FinishingMaterials"

    ID_FinMaterial = Column(Integer, primary_key=True, index=True, autoincrement=True)
    MaterialName = Column(String)
    Quantity = Column(Integer)

class ClientsMod(BaseModel):
    ClientName : str
    ClientSurname : str
    ClientPatronymic : str
    phoneNumber : str
    Client_login : str
    Client_pswd : str


class FinishingMaterialsModels(BaseModel):
    MaterialName : str
    Quantity : int

class ConstructionMaterialsModels(BaseModel):
    MaterialName : str
    Quantity : int


Base.metadata.create_all(bind=engine)


@app.get("/getClient/{id}")
async def root1(id):
    with Session(autoflush=False, bind=engine) as db:
        clients = db.query(Clients).all()
        for p in clients:
            if p.ID_Client == int(id):
                return p

@app.post("/postClient")
async def root4(item: ClientsMod=Depends()):
    with Session(autoflush=False, bind=engine) as db:
        a = Clients()
        a.ClientName = item.ClientName
        a.ClientSurname = item.ClientSurname
        a.ClientPatronymic = item.ClientPatronymic
        a.phoneNumber = item.phoneNumber
        a.Client_login = item.Client_login
        a.Client_pswd = item.Client_pswd
        db.add(a)
        db.commit()

@app.put("/putClient/{id}")
async def root3(id: str, item: ClientsMod=Depends()):
    with Session(autoflush=False, bind=engine) as db:
        a:Clients = db.query(Clients).filter(Clients.ID_Client == id).first()
        a.ClientName = item.ClientName
        a.ClientSurname = item.ClientSurname
        a.ClientPatronymic = item.ClientPatronymic
        a.phoneNumber = item.phoneNumber
        a.Client_login = item.Client_login
        a.Client_pswd = item.Client_pswd
        db.commit()

@app.delete("/delClient")
async def root5(id : str):
    with Session(autoflush=False, bind=engine) as db:
        a =db.query(Clients).filter(Clients.ID_Client == id).first()
        db.delete(a)
        db.commit()

@app.get("/getCM/{id}")
async def root1(id):
    with Session(autoflush=False, bind=engine) as db:
        cm = db.query(ConstructionMaterials).all()
        for p in cm:
            if p.ID_ConstMaterial == int(id):
                return p

@app.post("/postCM")
async def root4(item: ConstructionMaterialsModels=Depends()):
    with Session(autoflush=False, bind=engine) as db:
        a = ConstructionMaterials()
        a.MaterialName = item.MaterialName
        a.Quantity = item.Quantity
        db.add(a)
        db.commit()

@app.put("/putCM/{id}")
async def root3(id: str, item: ConstructionMaterialsModels=Depends()):
    with Session(autoflush=False, bind=engine) as db:
        a:ConstructionMaterials = db.query(ConstructionMaterials).filter(ConstructionMaterials.ID_ConstMaterial == id).first()
        a.MaterialName = item.MaterialName
        a.Quantity = item.Quantity
        db.commit()

@app.delete("/delCM")
async def root5(id : str):
    with Session(autoflush=False, bind=engine) as db:
        a =db.query(ConstructionMaterials).filter(ConstructionMaterials.ID_ConstMaterial == id).first()
        db.delete(a)
        db.commit()

@app.get("/getFM/{id}")
async def root1(id):
    with Session(autoflush=False, bind=engine) as db:
        fm = db.query(FinishingMaterials).all()
        for p in fm:
            if p.ID_FinMaterial == int(id):
                return p

@app.post("/postFM")
async def root4(item: FinishingMaterialsModels=Depends()):
    with Session(autoflush=False, bind=engine) as db:
        a = FinishingMaterials()
        a.MaterialName = item.MaterialName
        a.Quantity = item.Quantity
        db.add(a)
        db.commit()

@app.put("/putFM/{id}")
async def root3(id: str, item: FinishingMaterialsModels=Depends()):
    with Session(autoflush=False, bind=engine) as db:
        a:FinishingMaterials = db.query(FinishingMaterials).filter(FinishingMaterials.ID_FinMaterial == id).first()
        a.MaterialName = item.MaterialName
        a.Quantity = item.Quantity
        db.commit()

@app.delete("/delFM")
async def root5(id : str):
    with Session(autoflush=False, bind=engine) as db:
        a =db.query(FinishingMaterials).filter(FinishingMaterials.ID_FinMaterial == id).first()
        db.delete(a)
        db.commit()

#uvicorn.run(app, host="localhost", port=8000)
#python -m uvicorn main:app --reload