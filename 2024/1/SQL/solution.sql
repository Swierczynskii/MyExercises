-- Create tables
CREATE TABLE first_example_list (
    id NUMBER
); 

CREATE TABLE second_example_list (
    id NUMBER
); 

-- Insert values
INSERT INTO first_example_list
VALUES (3);
INSERT INTO first_example_list
VALUES (4);
INSERT INTO first_example_list
VALUES (2);
INSERT INTO first_example_list
VALUES (1);
INSERT INTO first_example_list
VALUES (3);
INSERT INTO first_example_list
VALUES (3);

INSERT INTO second_example_list
VALUES (4);
INSERT INTO second_example_list
VALUES (3);
INSERT INTO second_example_list
VALUES (5);
INSERT INTO second_example_list
VALUES (3);
INSERT INTO second_example_list
VALUES (9);
INSERT INTO second_example_list
VALUES (3);

-- Calculate total distance
WITH ordered_first_list AS (
    SELECT
    -- Order first list
        id,
        ROW_NUMBER()
        OVER(
            ORDER BY
                id
        ) rn
    FROM
        first_example_list
), ordered_second_list AS (
    SELECT
    -- Order second list
        id,
        ROW_NUMBER()
        OVER(
            ORDER BY
                id
        ) rn
    FROM
        second_example_list
)
SELECT
-- Sum up absolute value of ids difference = list distance
    SUM(abs(f.id - s.id)) as result
FROM
         ordered_first_list f
    JOIN ordered_second_list s ON ( f.rn = s.rn );