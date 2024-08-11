-- USERS
INSERT INTO users (id, first_name, last_name, username, password) VALUES
(1, 'Alan', 'Garber', 'alan', 'password'),
(2, 'Reid', 'Hoffman', 'reid', 'password');

-- SCHOOLS
INSERT INTO schools (id, name, type, location, founded_year) VALUES
(1, 'Harvard University', 'university', 'Cambridge, Massachusetts', 1636);

-- COMPANIES
INSERT INTO companies (id, name, industry, location) VALUES
(1, 'LinkedIn', 'technology', 'Sunnyvale, California');

-- Education of Alan Garber in Harvard
INSERT INTO user_school_connections (user_id, school_id, start_date, end_date, degree_type) VALUES
(1, 1, '1973-09-01', '1976-06-01', 'BA');

-- Reid Hoffman's job on linkedin
INSERT INTO user_companies_connections (user_id, company_id, start_date, end_date, title) VALUES
(2, 1, '2003-01-01', '2007-02-01', 'CEO and Chairman');
