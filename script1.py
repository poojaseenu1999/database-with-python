import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXIST store (item TEXT ,quantity INTEGER, prize REAL )")
    conn.commit()
    conn.close()

def insert(item,quantity,prize):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,prize))
    conn.commit()
    conn.close()
#insert("cofee cups",4,40.50)

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()


def update(quantity,prize,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?,prize=? WHERE item=?",(quantity,prize,item))
    conn.commit()
    conn.close()

update(10,70.90,"water bottle")
#delete("cofee cups")
print(view())
