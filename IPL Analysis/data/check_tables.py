import sqlite3

# Connect to the database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(f"- {table[0]}")

# Check a few records from each table
for table_name in ['dashboard_match', 'dashboard_player', 'dashboard_team']:
    try:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"\n{table_name}: {count} records")
        
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Exception as e:
        print(f"Error querying {table_name}: {e}")

conn.close()
