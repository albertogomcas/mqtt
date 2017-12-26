import sqlite3

DB_NAME = "mqttdata.db"


def init_db():
    db = get_db()
    with open('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    db = sqlite3.connect(DB_NAME)
    return db


if __name__ == '__main__':
    import os

    if not os.path.exists(DB_NAME):
        init_db()
