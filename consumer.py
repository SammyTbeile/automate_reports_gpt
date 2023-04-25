import faust
import psycopg2

app = faust.App('stock-consumer', broker='kafka://localhost:29092')

class Stock(faust.Record):
    event_time: str
    price: float
    symbol: str


# Define a Faust topic
topic = app.topic('stock-events', value_type=Stock)

# Define a PostgreSQL connection
conn = psycopg2.connect(
    dbname='reports',
    user='myuser',
    password='mypassword',
    host='localhost',
    port=5432
)

# Define a PostgreSQL cursor
cur = conn.cursor()

# Define a Faust table to store the events
table = app.Table('stock', partitions=1)

# Define a Faust agent that consumes events and writes them to PostgreSQL
@app.agent(topic)
async def stock_events(events):
    async for event in events:
        # Store the event in the Faust table
        table[event.symbol] = event

        print(event.symbol)
        # Write the event to the PostgreSQL database
        cur.execute("INSERT INTO stock (symbol, price, event_time) VALUES (%s, %s, %s)",
                    (event.symbol, event.price, event.event_time))
        conn.commit()

if __name__ == '__main__':
    app.main()
