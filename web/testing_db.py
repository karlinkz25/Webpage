import sqlite3

create_table = """
CREATE TABLE IF NOT EXISTS contacts (
    contact_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
"""
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute(create_table)
conn.commit()

insert_command = """
INSERT INTO contacts(first_name, last_name)
VALUES("ab", "cd");
"""

cursor = conn.cursor()
cursor.execute(insert_command)
conn.commit()


cursor = conn.cursor()
cursor.execute("select * from contacts;")
print(cursor.fetchall())
conn.close()