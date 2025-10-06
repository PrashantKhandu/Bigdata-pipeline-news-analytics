-- To fetch top 100 records
SELECT * FROM news LIMIT 100;

-- Count today's scraped records
SELECT count(*) FROM news 
    WHERE DATE('date_added') == CURRENT_DATE;

-- Count today's published records
SELECT count(*) as todays_count FROM news
    WHERE DATE('date_published') == CURRENT_DATE;
