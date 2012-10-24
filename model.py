import sqlite3

def connect_db():
    return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):
    c = db.cursor()
    query = """INSERT INTO Users VALUES (Null, ?, ?, ?)"""
    result = c.execute(query,(email, password, name))
    db.commit()
    return result.lastrowid

def authenticate(db, email, password):
    c = db.cursor()
    query = """ SELECT * from Users WHERE email = ? and password =?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields=["id", 'email', 'password', 'name']
        return dict(zip(fields, result))
    return None

def new_task(db, title, user_id):
    c = db.cursor()
    query = """INSERT INTO Tasks Values (Null, ?, current_time, Null, ?)"""
    result = c.execute(query,(title, user_id))
    db.commit()
    return result.lastrowid

def get_user(db, user_id = None):
    if user_id:
        c = db.cursor()
        query = """ SELECT * from Users WHERE id = ?"""
        c.execute(query, (user_id,))
        result = c.fetchone()
        if result:
            fields=["id", "email", "password", "name"]
            return dict(zip(fields, result))
    else:
        user_list = []
        c = db.cursor()
        query = """ SELECT * from Users"""
        c.execute(query)
        result = c.fetchall()
        for row in result:
            fields=["id", "email", "password", "name"]
            user_list.append(dict(zip(fields, row)))
        return user_list

def complete_task(db, task_id):
    c = db.cursor()
    query = """UPDATE tasks SET completed_at = current_time WHERE id =?"""
    result = c.execute(query,(task_id,))
    db.commit()
    return result.lastrowid

def get_tasks(db, user_id = None):
    if user_id:
        c = db.cursor()
        query = """SELECT * from Tasks WHERE user_id = ?"""
        c.execute(query, (user_id,))
        result = c.fetchone()
        if result:
            fields=["id", "title", 'created_at', 'completed_at', 'user_id']
            return dict(zip(fields, result))
    else:
        task_list = []
        c = db.cursor()
        query = """SELECT * from Tasks"""
        c.execute(query)
        db.commit()
        result = c.fetchall()
        for row in result:   
            fields=["id", "title", 'created_at', 'completed_at', 'user_id']
            task_list.append(dict(zip(fields,row)))
        return task_list


def get_task(db, task_id):
    c = db.cursor()
    query = """SELECT * from Tasks Where id = ?"""
    c.execute(query, (task_id, ))
    db.commit()
    result = c.fetchone()
    if result:
        fields=["id", "title", 'created_at', 'completed_at', 'user_id']
        return dict(zip(fields, result))
    return None
