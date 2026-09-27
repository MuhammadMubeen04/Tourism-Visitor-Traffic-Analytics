USE tourism_analytics;

-- 1. OVERALL KPIs
SELECT 
    SUM(Visitors) AS total_visitors,
    ROUND(AVG(AvgStayNights), 2) AS avg_stay_nights,
    ROUND(SUM(EstSpendSAR), 2) AS total_est_spend_sar,
    ROUND(AVG(HotelOccupancyPct), 1) AS avg_occupancy_pct,
    COUNT(DISTINCT City) AS cities,
    COUNT(DISTINCT YearMonth) AS months
FROM monthly_city_traffic;

-- 2. VISITORS BY CITY
SELECT City,
       SUM(Visitors) AS visitors,
       ROUND(SUM(EstSpendSAR), 2) AS est_spend,
       ROUND(AVG(HotelOccupancyPct), 1) AS avg_occupancy
FROM monthly_city_traffic
GROUP BY City
ORDER BY visitors DESC;

-- 3. MONTHLY TREND
SELECT YearMonth,
       SUM(Visitors) AS visitors,
       ROUND(SUM(EstSpendSAR), 2) AS est_spend,
       ROUND(AVG(HotelOccupancyPct), 1) AS avg_occupancy
FROM monthly_city_traffic
GROUP BY YearMonth
ORDER BY YearMonth;

-- 4. YEARLY SUMMARY
SELECT Year,
       SUM(Visitors) AS visitors,
       ROUND(SUM(EstSpendSAR), 2) AS est_spend
FROM monthly_city_traffic
GROUP BY Year
ORDER BY Year;

-- 5. PURPOSE BREAKDOWN (visits sample)
SELECT Purpose,
       COUNT(*) AS visits,
       ROUND(AVG(StayNights), 1) AS avg_nights,
       ROUND(SUM(SpendSAR), 2) AS total_spend,
       ROUND(AVG(SpendSAR), 2) AS avg_spend
FROM visits
GROUP BY Purpose
ORDER BY visits DESC;

-- 6. ORIGIN BREAKDOWN
SELECT Origin,
       COUNT(*) AS visits,
       ROUND(SUM(SpendSAR), 2) AS total_spend,
       ROUND(AVG(SpendSAR), 2) AS avg_spend
FROM visits
GROUP BY Origin
ORDER BY visits DESC;

-- 7. CITY + PURPOSE
SELECT City, Purpose, COUNT(*) AS visits
FROM visits
GROUP BY City, Purpose
ORDER BY City, visits DESC;

-- 8. TOP MONTHS BY TRAFFIC
SELECT YearMonth, SUM(Visitors) AS visitors
FROM monthly_city_traffic
GROUP BY YearMonth
ORDER BY visitors DESC
LIMIT 12;
