from fastapi import FastAPI
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "CV_Aksels.db"

def query_db(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    return [dict(zip(columns, row)) for row in results]

@app.get("/")
def root():
    return {"message": "CV API is live!"}

@app.get("/experience")
def get_experience():
    return query_db("SELECT * FROM experience")

@app.get("/education")
def get_education():
    return query_db("SELECT * FROM education")

@app.get("/skills")
def get_skills():
    return query_db("SELECT * FROM skills")

@app.get("/contact")
def get_contact():
    return query_db("SELECT * FROM contact")

@app.get("/other_experience")
def get_other_experience():
    return query_db("SELECT * FROM other_experience")

@app.get("/personal_info")
def get_personal_info():
    return query_db("SELECT * FROM personal_info")