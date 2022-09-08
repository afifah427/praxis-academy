from flask import Flask, render_template, request, redirect
import psycopg2
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="santri",
        user="postgres",
        password="I270302A")
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        angkatan = request.form.get("angkatan")
        query = f"insert into daftar_santri(nama, angkatan) values('{nama}', '{angkatan}')"
        curs.execute(query)
        conn.commit()
        curs.close()
        conn.close()
 
    
    print(request.method)
    query = f"select * from daftar_santri order by nama asc"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    # data = ["anggur", "jeruk", "apel"]
    return render_template("index.html", context=data)

@app.route("/2022/<angkatan_2022_id>")
def detail(angkatan_2022_id):
    conn = psycopg2.connect(
        host="localhost",
        database="angkatan",
        user="postgres",
        password="I270302A"
    )
    curs = conn.cursor()
    query = f"select * from angkatan_2022 where id = {angkatan_2022_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    return render_template("2022.html", context=data)


if __name__ == "__main__":
    app.run()