-- Insert some sample data into the ATL DataBase

INSERT INTO "passengers" ("id", "first_name", "last_name", "age") VALUES (1, "Amelia", "Earhart", 39);

INSERT INTO "airlines" ("name") VALUES ("Delta");

INSERT INTO "concourses" ("concourse") VALUES
    ("A"),
    ("B"),
    ("C"),
    ("D"),
    ("E"),
    ("F"),
    ("T");

INSERT INTO "airlines_concourses" ("airline_name", "concourse_type") VALUES
    ("Delta", "A"),
    ("Delta", "B"),
    ("Delta", "C"),
    ("Delta", "D"),
    ("Delta", "T");

INSERT INTO "flights" ("id", "flight_number", "airline_name", "departing_airport_code", "heading_airport_code", "departure_time", "arrival_time") VALUES
    (1,  300, "Delta",  "ATL", "BOS",  "2023-08-03 18:46:00", "2023-08-03 21:09:00");

INSERT INTO "CHECK-INS" ("passenger_id", "flight_id", "datetime") VALUES (1, 1, "2023-08-03 15:03:00")
