

INSERT INTO Ingredients (id, ingredient, unit_measure, price_per_unit) VALUES
(1, 'Cocoa', 'pound', 5.00),
(2, 'Sugar', 'pound', 2.00),
(3, 'Flour', 'pound', 1.50),
(4, 'Buttermilk', 'pound', 1.00),
(5, 'Sprinkles', 'pound', 3.00);

INSERT INTO Donuts (id, donut_name, is_gluten_free, price) VALUES
(1, 'Belgian Dark Chocolate', 0, 4.00),
(2, 'Back-To-School Sprinkles', 0, 4.00);


INSERT INTO DonutIngredients (donut_id, ingredient_id) VALUES
(1, 1), -- Belgian Dark Chocolate includes Cocoa
(1, 3), -- Belgian Dark Chocolate includes Flour
(1, 4), -- Belgian Dark Chocolate includes Buttermilk
(1, 2), -- Belgian Dark Chocolate includes Sugar
(2, 3), -- Back-To-School Sprinkles includes Flour
(2, 4), -- Back-To-School Sprinkles includes Buttermilk
(2, 2), -- Back-To-School Sprinkles includes Sugar
(2, 5); -- Back-To-School Sprinkles includes Sprinkles

INSERT INTO Customers (id, first_name, last_name) VALUES
(1, 'Luis', 'Singh');

INSERT INTO Orders (id, customer_id) VALUES
(1, 1);

INSERT INTO OrderItems (order_id, donut_id, quantity) VALUES
(1, 1, 3), -- 3 Belgian Dark Chocolate donuts
(1, 2, 2); -- 2 Back-To-School Sprinkles donuts
