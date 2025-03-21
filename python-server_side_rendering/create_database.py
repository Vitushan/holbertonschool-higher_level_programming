import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Drop table if it exists to avoid duplicate entries when script is run multiple times
    cursor.execute('DROP TABLE IF EXISTS Products')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()
    print("Database created and populated successfully!")

if __name__ == '__main__':
    create_database()