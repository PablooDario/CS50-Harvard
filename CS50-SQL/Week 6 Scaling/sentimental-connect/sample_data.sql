-- Insert users
INSERT INTO users (first_name, last_name, password) VALUES
('Claudine', 'Gay', 'password'),
('Reid', 'Hoffman', 'password');

-- Insert school
INSERT INTO schools (name, type, location, foundation_year) VALUES
('Harvard University', 'Higher Education', 'Cambridge, Massachusetts', 1636);

-- Insert company
INSERT INTO companies (name, industry, location) VALUES
('LinkedIn', 'Technology', 'Sunnyvale, California');

-- Insert connections to schools
-- First, get the IDs for users and schools
SET @claudine_id = (SELECT id FROM users WHERE first_name = 'Claudine' AND last_name = 'Gay');
SET @harvard_id = (SELECT id FROM schools WHERE name = 'Harvard University');

INSERT INTO school_people_connections (school_id, user_id, start_date, end_date, degree_type) VALUES
(@harvard_id, @claudine_id, '1993-01-01', '1998-12-31', 'PhD');

-- Insert connections to companies
-- Get the IDs for users and companies
SET @reid_id = (SELECT id FROM users WHERE first_name = 'Reid' AND last_name = 'Hoffman');
SET @linkedin_id = (SELECT id FROM companies WHERE name = 'LinkedIn');

INSERT INTO company_people_connections (company_id, user_id, start_date, end_date) VALUES
(@linkedin_id, @reid_id, '2003-01-01', '2007-02-01');
