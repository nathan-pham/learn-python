import sqlite3 as sql

connection = sql.connect("emaildb.sqlite")
ref = connection.cursor()

ref.execute("DROP TABLE IF EXISTS Count")
ref.execute("CREATE TABLE Count (email TEXT, count INTEGER)")

handle = open("../files/mbox-short.txt")

for line in handle:
    if not line.startswith("From:"):
        continue

    parsed = line.split()
    email = parsed[1]

    ref.execute("SELECT count FROM Count WHERE email = ?", (email,))
    row = ref.fetchone()

    if row:
        ref.execute("UPDATE Count SET count = count + 1 WHERE email = ?", (email,))
    else:
        ref.execute("INSERT INTO Count (email, count) VALUES(?, 1)", (email, ))

    connection.commit()

counts = ref.execute("SELECT email, count FROM Count ORDER BY count DESC LIMIT 10")
for row in counts:
    print(row[0], row[1])