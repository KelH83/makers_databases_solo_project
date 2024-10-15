## 1. Extract nouns from the user stories or specification

```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```

```
Nouns:

students, full_name, cohort_id, cohort_name, start_date
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                  | Properties                 |
| ---------------------   | ------------------         |
| cohorts                 | cohort_name, starting_date |
| students                | full_name, cohort_id       |


1. Name of the first table (always plural): `cohorts` 

    Column names: `cohort_name`, `starting_date`

2. Name of the second table (always plural): `students` 

    Column names: `full_name`, `cohort_id`

## 3. Decide the column types
```
# EXAMPLE:

Table: cohorts
id: SERIAL
cohort_name: text
starting_date: int

Table: students
id: SERIAL
full_name: text
cohort_id: foreign key
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (no)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes)

You'll then be able to say that:

1. **[students] has many [cohorts]**
2. And on the other side, **[cohorts] belongs to [students]**
3. In that case, the foreign key is in the table [students]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one cohort have many students? YES
2. Can one student have many cohorts? NO

-> Therefore,
-> A cohort HAS MANY students
-> A student BELONGS TO a cohort

-> Therefore, the foreign key is on the cohorts table.
Except that makes no sense with foreign keys because 1 cohort cannot have multiple foreign keys for multiple students, 1 student would have a single cohort foreign key
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: students_table.sql

-- Create the table without the foreign key first.
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name VARCHAR(250),
  starting_date int
);

-- Then the table with the foreign key second.
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(250),
-- The foreign key name is always {other_table_singular}_id
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 student_directory_2 < students_table_2.sql
```