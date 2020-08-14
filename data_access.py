import _sqlite3

def get_db():
    db = getattr(g, '_databasee', None)



def createTable():
    conn = _sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE purchases
                (date text,
                item text,
                qty integer,
                price real)''')
    c.execute("INSERT INTO purchases VALUES ('2-8-2020', 'Yankee burger', '1', 7.95)")
    conn.commit()
    conn.close()

def addUser(fname, sname):
    conn = _sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (fName, sName) VALUES (?, ?)", (fname, sname))
    conn.commit()
    conn.close()

def findSurname(sname):
    conn = _sqlite3.connect("example.db")
    c = conn.cursor()
    for row in c.execute('SELECT * FROM users WHERE sName=?', (sname,)):
        print(row)
    conn.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

#def addUser(fname, sname):
 #   conn = sqlite3.connect('example.db')
  #  c = conn.cursor()
