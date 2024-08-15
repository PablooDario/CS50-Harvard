-- Create a DataBase for a Donuts Store

CREATE TABLE Ingredients(
    "id" INTEGER,
    "ingredient" TEXT NOT NULL,
    "unit_measure" TEXT NOT NULL,
    "price_per_unit" REAL NOT NULL,
    PRIMARY KEY ("id")
);


CREATE TABLE Donuts (
    "id" INTEGER,
    "donut_name" TEXT NOT NULL,
    "is_gluten_free" INTEGER NOT NULL, -- 0 for False, 1 for True
    "price" INTEGER NOT NULL,
    PRIMARY KEY("id")
);


CREATE TABLE DonutIngredients (
    "donut_id" INTEGER,
    "ingredient_id" INTEGER,
    FOREIGN KEY("donut_id") REFERENCES "Donuts"("id"),
    FOREIGN KEY("ingredient_id") REFERENCES "Ingredients"("id"),
    PRIMARY KEY ("donut_id", "ingredient_id")
);


CREATE TABLE Orders (
    "id" INTEGER,
    "customer_id" INTEGER,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("customer_id") REFERENCES "customers" ("id")

);

CREATE TABLE OrderItems (
    "order_id" INTEGER,
    "donut_id" INTEGER,
    "quantity" INTEGER NOT NULL,
    FOREIGN KEY ("order_id") REFERENCES "Orders" ("id")
    FOREIGN KEY("donut_id") REFERENCES "Donuts"("id"),
    PRIMARY KEY ("order_id", "donut_id")
);


CREATE TABLE Customers(
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    PRIMARY KEY ("id")
);

