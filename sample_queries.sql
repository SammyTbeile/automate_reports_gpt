-- Find the average price for each symbol:
SELECT symbol, AVG(price) as average_price
FROM stock
GROUP BY symbol;

-- Find the highest and lowest price for each symbol:
SELECT symbol, MAX(price) as highest_price, MIN(price) as lowest_price
FROM stock
GROUP BY symbol;

-- Find the total volume and total value traded for each symbol:
SELECT symbol, SUM(volume) as total_volume, SUM(volume * price) as total_value
FROM stock
GROUP BY symbol;

--Find the average price for each symbol over the last 7 days:
SELECT symbol, AVG(price) as average_price
FROM stock
WHERE event_time > NOW() - INTERVAL '7 days'
GROUP BY symbol;

--Find the top 10 symbols by total volume traded:
SELECT symbol, SUM(volume) as total_volume
FROM stock
GROUP BY symbol
ORDER BY total_volume DESC
LIMIT 10;
