try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="hda182526")


    curs = conn.cursor()

    nama = 'mark'

    query = f"delete from siswa where nama='{nama}'"
    curs.execute(query)
    conn.commit()
    print("data dihpus")
except Exception as e:
    print(e)