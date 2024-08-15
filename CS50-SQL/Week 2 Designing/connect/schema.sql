-- Create a DataBase for Linkedin where users can connect with other users and post their professional and academic experience

CREATE TABLE IF NOT EXISTS users (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS schools (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "founded_year" INTEGER NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS companies (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "industry" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS user_user_connections (
    "user_a_id" INTEGER,
    "user_b_id" INTEGER,
    PRIMARY KEY ("user_a_id", "user_b_id"),
    FOREIGN KEY ("user_a_id") REFERENCES "users" ("id"),
    FOREIGN KEY ("user_b_id") REFERENCES "users" ("id")
);

CREATE TABLE IF NOT EXISTS user_school_connections (
    "user_id" INTEGER,
    "school_id" INTEGER,
    "start_date" TIMESTAMP NOT NULL,
    "end_date" TIMESTAMP NOT NULL,
    "degree_type" TEXT NOT NULL,
    PRIMARY KEY ("user_id", "school_id"),
    FOREIGN KEY ("user_id") REFERENCES "users" ("id"),
    FOREIGN KEY ("school_id") REFERENCES "schools" ("id")
);

CREATE TABLE IF NOT EXISTS user_companies_connections (
    "user_id" INTEGER,
    "company_id" INTEGER,
    "start_date" TIMESTAMP NOT NULL,
    "end_date" TIMESTAMP NOT NULL,
    "title" TEXT NOT NULL,
    PRIMARY KEY ("user_id", "company_id"),
    FOREIGN KEY ("user_id") REFERENCES "users" ("id"),
    FOREIGN KEY ("company_id") REFERENCES "companies" ("id")
);
