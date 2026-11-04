import mariadb
from config import DB_CONFIG

conn = mariadb.connect(**DB_CONFIG)

cursor = conn.cursor()

cursor.execute("SELECT visits FROM counter WHERE id = 1")

result = cursor.fetchone()

print("Tietokantayhteys toimii!")
print("Käyntimäärä:", result[0])

cursor.close()
conn.close()
