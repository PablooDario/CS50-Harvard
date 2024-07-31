# Schema

In Massachusetts, public education is delegated to districts, a type of school government often associated with an individual town. These districts, in turn, contain many individual schools. Consider the entity relationship diagram below, which codifies the relationship between districts, schools, and other data DESE collects.

![DeseSchema](..\imgs\DeseSchema.png)

### Districts table

The **districts table** contains the following columns:

- `id`, which is the ID of the district
- `name`, which is the name of the district
- `type`, which denotes the type of district. In Massachusetts, there are public school districts (denoted “Public School District”) and charter districts (denoted “Charter District”). 
- `city`, which is the city in which the district is located
- `state`, which is the state in which the district is located
- `zip`, which is the ZIP Code in which the district is located

### Schools table

The **schools table** contains the following columns:

- `id`, which is the ID of the school
- `district_id`, which is the ID of the district to which the school belongs
- `name`, which is the name of the school
- `type`, which denotes the type of school. 
- `city`, which is the city in which the school is located
- `state`, which is the state in which the school is located
- `zip`, which is the ZIP Code in which the school is located

### Graduation_rates table

The **graduation_rates** table contains the following columns:

- `id`, which is the ID of the graduation rate
- `school_id`, which is the ID of the school with which the graduation is associated
- `graduated`, which is the percentage of students, 0–100, who graduated on time
- `dropped`, which is the percentage of students, 0–100, who dropped out of school before graduation
- `excluded`, which is the percentage of students, 0–100, who were “excluded” (i.e., expelled)

### Expenditures table

The **expenditures** table contains the following columns:

- `id`, which is the ID of the expenditure
- `district_id`, which is the ID of the district with which the expenditure is associated
- `pupils`, which is the number of pupils attending the given district
- `per_pupil_expenditure`, which is the amount of money spent, in dollars, on each student attending the district

### Staff_evaluations table

The **staff_evaluations** table contains the following columns:

- `id`, which is the ID of the evaluation report
- `district_id`, which is the ID of the district with which the evaluation is associated
- `evaluated`, which is the percentage of district staff, 0–100, formally evaluated
- `exemplary`, which is the percentage of district staff, 0–100, evaluated as “exemplary”
- `proficient`, which is the percentage of district staff, 0–100, evaluated as “proficient”
- `needs_improvement`, which is the percentage of district staff, 0–100, evaluated as “needing improvement”
- `unsatisfactory`, which is the percentage of district staff, 0–100, evaluated as “unsatisfactory”