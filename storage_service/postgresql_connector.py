import psycopg2

def store_in_postgresql(data):
    conn = psycopg2.connect(database="finance_db", user="username", password="password", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO stock_prices (symbol, price)
        VALUES (%s, %s)
    """, (data['symbol'], data['price']))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    stock_data = {
        "symbol": "AAPL",
        "price": 150.25
    }
    store_in_postgresql(stock_data)
