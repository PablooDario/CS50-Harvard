-- Create a DataBase for the ATL Airport

CREATE TABLE IF NOT EXISTS "airlines"(
    "name" TEXT NOT NULL,
    PRIMARY KEY ("name")
);

CREATE TABLE IF NOT EXISTS "concourses" (
    "concourse" TEXT NOT NULL CHECK("concourse" IN ('A', 'B', 'C', 'D', 'E', 'F', 'T')),
    PRIMARY KEY ("concourse")
);

CREATE TABLE IF NOT EXISTS "airlines_concourses" (
    "airline_name" TEXT,
    "concourse_type" TEXT NOT NULL CHECK("concourse_type" IN ('A', 'B', 'C', 'D', 'E', 'F', 'T')),
    PRIMARY KEY ("airline_name", "concourse_type"),
    FOREIGN KEY ("airline_name") REFERENCES "airlines"("name"),
    FOREIGN KEY("concourse_type") REFERENCES "concourses"("concourse")
);

CREATE TABLE IF NOT EXISTS "passengers"(
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "age" INTEGER NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "flights"(
    "id" INTEGER,
    "flight_number" INTEGER NOT NULL,
    "airline_name" TEXT NOT NULL,
    "departing_airport_code" TEXT NOT NULL,
    "heading_airport_code" TEXT NOT NULL,
    "departure_time" TIMESTAMP NOT NULL,
    "arrival_time" TIMESTAMP NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY ("airline_name") REFERENCES "airlines" ("name")
);

CREATE TABLE IF NOT EXISTS "Check-Ins"(
    "passenger_id" INTEGER,
    "flight_id" INTEGER NOT NULL,
    "datetime" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY("passenger_id", "flight_id"),
    FOREIGN KEY ("passenger_id") REFERENCES "passengers" ("id"),
    FOREIGN KEY ("flight_id") REFERENCES "flights" ("id")
);

