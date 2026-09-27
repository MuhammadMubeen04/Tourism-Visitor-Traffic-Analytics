-- Tourism & Visitor Traffic Analytics - MySQL Schema

CREATE DATABASE IF NOT EXISTS tourism_analytics;
USE tourism_analytics;

CREATE TABLE IF NOT EXISTS monthly_city_traffic (
    RecordID           VARCHAR(20),
    YearMonth          VARCHAR(10),
    Year               INT,
    Month              INT,
    City               VARCHAR(50),
    Visitors           INT,
    AvgStayNights      DECIMAL(6,1),
    EstSpendSAR        DECIMAL(14,2),
    HotelOccupancyPct  DECIMAL(6,1)
);

CREATE TABLE IF NOT EXISTS visits (
    VisitID        VARCHAR(20),
    YearMonth      VARCHAR(10),
    Year           INT,
    Month          INT,
    City           VARCHAR(50),
    Purpose        VARCHAR(50),
    Origin         VARCHAR(50),
    Accommodation  VARCHAR(50),
    StayNights     INT,
    SpendSAR       DECIMAL(12,2),
    PartySize      INT
);

-- Import data/monthly_city_traffic.csv and data/visits.csv
