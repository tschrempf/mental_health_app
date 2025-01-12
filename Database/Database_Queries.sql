#Shows the Tables in the Database
SELECT name FROM sqlite_master WHERE type='table';

#Shows the Columns in the cloudy_recommendation Table - only 10 rows
SELECT * FROM cloudy_recommendation LIMIT 10;

#Shows information about the cloudy_recommendation Table
PRAGMA table_info(cloudy_recommendation);

#Shows me the first 10 rows of the cloudy_recommendation Table with the interest of 'Outdoor'
SELECT * FROM cloudy_recommendation WHERE interest = 'Outdoor';
