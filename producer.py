import faust
import random
from datetime import datetime

app = faust.App('stock-events', broker='kafka://localhost:29092')

class Stock(faust.Record):
    event_time: str
    price: float
    symbol: str

stock_topic = app.topic('stock-events')

@app.timer(interval=1.0)
async def generate_stock_events():
    # Generate a random stock price between 1 and 100
    price = random.uniform(1, 100)

    # Choose a random symbol

    symbols = ['AAPL', 'AMZN', 'GOOG', 'FB', 'NFLX', 'TSLA', 'MSFT', 'NVDA', 'PYPL', 'ADBE',
           'CRM', 'BABA', 'JPM', 'BAC', 'GS', 'WFC', 'C', 'JNJ', 'PFE', 'MRK', 'UNH',
           'CVS', 'WMT', 'TGT', 'KO']

    random_symbol = random.choice(symbols)
    
    # Create a new Stock event with the current timestamp, random price, and symbol
    event = Stock(event_time=datetime.now().isoformat(), price=price, symbol=random_symbol)
    
    # Publish the event to the Kafka topic
    await stock_topic.send(value=event)

if __name__ == '__main__':
    app.main()
