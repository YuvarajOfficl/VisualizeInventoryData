import sqlite3


conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        vendor TEXT,
        item TEXT,
        quantity INTEGER,
        month TEXT,
        location TEXT
    )
""")


dummy_data = [
    ("Vendor A", "Spark Plug", 100, "Dec 2024", "Mumbai"),
    ("Vendor A", "Spark Plug", 50, "Jan 2025", "Mumbai"),
    ("Vendor A", "Spark Plug", 25, "Feb 2025", "Mumbai"),
    ("Vendor A", "Lubricant", 80, "Dec 2024", "Mumbai"),
    ("Vendor A", "Lubricant", 60, "Jan 2025", "Mumbai"),
    ("Vendor A", "Lubricant", 40, "Feb 2025", "Mumbai"),
    ("Vendor B", "Spark Plug", 150, "Dec 2024", "Delhi"),
    ("Vendor B", "Spark Plug", 120, "Jan 2025", "Delhi"),
    ("Vendor B", "Spark Plug", 90, "Feb 2025", "Delhi"),
    ("Vendor B", "Lubricant", 70, "Dec 2024", "Delhi"),
    ("Vendor B", "Lubricant", 50, "Jan 2025", "Delhi"),
    ("Vendor B", "Lubricant", 30, "Feb 2025", "Delhi"),
    ("Vendor C", "Spark Plug", 80, "Dec 2024", "Mysore"),
    ("Vendor C", "Lubricant", 90, "Dec 2024", "Mysore"),
    ("Vendor C", "Lubricant", 70, "Jan 2025", "Mysore"),
    ("Vendor C", "Lubricant", 55, "Feb 2025", "Mysore")
]

cursor.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?, ?)", dummy_data)
conn.commit()
conn.close()

print("✅ Data inserted successfully!")
