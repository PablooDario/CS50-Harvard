-- Create the Database and Insert sql statements
-- cat import.sql | sqlite3 meteorites.db

-- create table to clean up meteorites csv data
CREATE TABLE IF NOT EXISTS "meteorites_temp"(
    name TEXT,
    id INTEGER,
    nametype TEXT,
    class TEXT,
    mass NUMERIC,
    discovery TEXT,
    year NUMERIC,
    lat NUMERIC,
    long NUMERIC
);

.import --csv --skip 1 meteorites.csv meteorites_temp

-- Update empty data to NULL
UPDATE "meteorites_temp" SET "mass" = NULL WHERE "mass" = "";
UPDATE "meteorites_temp" SET "year" = NULL WHERE "year" = "";
UPDATE "meteorites_temp" SET "lat" =  NULL WHERE "lat" = "";
UPDATE "meteorites_temp" SET "long" = NULL WHERE "long" = "";

-- All columns with decimal values should be rounded to the nearest hundredths place
UPDATE "meteorites_temp"
SET lat = ROUND(lat, 2), long = ROUND(long, 2);

-- All meteorites with the nametype “Relict” are not included in the meteorites table.
DELETE FROM "meteorites_temp"
WHERE nametype = "Relict";

-- Create Final Table
CREATE TABLE IF NOT EXISTS "meteorites"(
    id INTEGER,
    name TEXT NOT NULL,
    class TEXT,
    mass NUMERIC,
    discovery TEXT,
    year NUMERIC,
    lat NUMERIC,
    long NUMERIC,
    PRIMARY KEY (id)
);

-- The meteorites are sorted by year, oldest to newest, and then—if any two meteorites landed in the same year—by name, in alphabetical order.
INSERT INTO "meteorites" (name, class, mass, discovery, year, lat, long)
SELECT name, class, mass, discovery, year, lat, long  FROM "meteorites_temp" ORDER BY year, name;

-- Drop temporal table
DROP TABLE "meteorites_temp";
