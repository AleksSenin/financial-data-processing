from cassandra.cluster import Cluster

CASSANDRA_HOST = "localhost"

def store_in_cassandra(data):
    cluster = Cluster([CASSANDRA_HOST])
    session = cluster.connect('finance_data')
    session.execute("""
        INSERT INTO stock_prices (symbol, price)
        VALUES (%s, %s)
    """, (data['symbol'], data['price']))

if __name__ == "__main__":
    stock_data = {
        "symbol": "AAPL",
        "price": 150.25
    }
    store_in_cassandra(stock_data)
