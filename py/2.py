HOST = get_host()
PORT = get_port()
USER = get_id()
PASSWORD = get_password()
DB = get_db()


def connect():
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=DB)
    except pymysql.Error as e:
        print('connection error')

    return conn


def close(conn):
    if not conn is None:
        try:
            conn.close
        except pymysql.Error as e:
            print('close error')


def sql(email, password):
    conn = connect()
    cursor: pymysql.cursors.Cursor = conn.cursor()

    sql = "SELECT * FROM company WHERE email= '" + "%s" + "' AND password='" + "%s" + "'";
    sql_data = (email, password)
    cursor.execute(sql, sql_data)

    if isinstance(cursor, pymysql.cursors.Cursor):
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))

    conn.commit()
    close(conn)
    return json_data