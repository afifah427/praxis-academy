import psycopg2
from flask import request, render_template, redirect

def index():
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="I270302A"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        detail = request.form.get("detail")
        query = f"insert into buah(nama, detail) values('{nama}', '{detail}')"
        curs.execute(query)
        conn.commit()
        

    
    print(request.method)
    query = f"select * from buah order by id desc"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    # data = ["anggur", "jeruk", "apel"]
    return render_template("index.html", context=data)

def detail(buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="I270302A"
    )
    curs = conn.cursor()
    query = f"select * from buah where id = {buah_id}"
    curs.execute(query)
    data = curs.fetchone()
    conn.commit()
    curs.close()
    conn.close()
    return render_template("detail.html", context=data)

def delete(buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="I270302A"
    )
    curs = conn.cursor()
    query = f"delete from buah where id = {buah_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect("/")

def update(buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="I270302A"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama =request.form.get("nama")
        detail =request.form.get("detail")
        query = f"update buah set nama = '{nama}', detail = '{detail}' where id = {buah_id}"
        curs.execute(query)
        conn.commit()
        return redirect("/")
        
    query = f"select * from buah where id = {buah_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    return render_template("update.html", context=data)

