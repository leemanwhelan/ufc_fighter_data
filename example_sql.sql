/*
--Some Example SQL code used to set up my data base
--Creating the table:
CREATE TABLE first_20_fighters(
	fighter_id SERIAL PRIMARY KEY,
	first_name VARCHAR(100),
	last_name VARCHAR(100), 
	wins SMALLINT,
	losses SMALLINT,
	draws SMALLINT,
	no_contests SMALLINT,
	nickname VARCHAR(100),
	height INTEGER,
	weight INTEGER,
	reach INTEGER, 
	stance VARCHAR(50),
	birth_date DATE, 
	sig_strikes_per_min NUMERIC,
	sig_strikes_accur NUMERIC,
	sig_strikes_absrb_min NUMERIC, 
	sig_strikes_defnce NUMERIC, 
	take_down_avg NUMERIC, 
	take_down_accur NUMERIC, 
	take_down_def NUMERIC, 
	sub_avg NUMERIC
);

--After Importing the data, we have a look:
SELECT * FROM ufc_fighters
LIMIT 50;

--Best Significant Strike Accuracy in UFC history:
SELECT first_name, last_name, sig_strikes_accur
FROM ufc_fighters
ORDER BY sig_strikes_accur;

--Show average reach, height, sig_strikes_per_min of each 
--weight class:

SELECT weight, AVG(reach) as avg_reach, AVG(height) as avg_height, 
AVG(sig_strikes_per_min) as avg_sigStrikesPerMin
FROM ufc_fighters
WHERE weight IN(125, 135, 145, 155, 170, 185, 205)
OR weight BETWEEN 206 AND 265
GROUP BY weight
ORDER BY weight;

