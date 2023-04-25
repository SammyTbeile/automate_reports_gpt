-- Create database
CREATE DATABASE reports;

-- Connect to database
\c reports;

-- Create table
CREATE TABLE stock (
  event_time timestamp with time zone NOT NULL,
  price numeric(10,2) NOT NULL,
  symbol varchar(10) NOT NULL
);

-- Add primary key constraint
ALTER TABLE stock ADD CONSTRAINT pk_stock PRIMARY KEY (event_time, symbol);
