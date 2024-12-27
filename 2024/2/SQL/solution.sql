-- Create table
CREATE TABLE reports (
    lvls VARCHAR2(10)
); 

-- Insert values
INSERT INTO reports VALUES ( '7 6 4 2 1' );

INSERT INTO reports VALUES ( '1 2 7 8 9' );

INSERT INTO reports VALUES ( '9 7 6 2 1' );

INSERT INTO reports VALUES ( '1 3 2 4 5' );

INSERT INTO reports VALUES ( '8 6 4 4 1' );

INSERT INTO reports VALUES ( '1 3 6 7 9' );

WITH hierarchical_cte AS (
    SELECT
        ora_hash(lvls)   AS uuid,
        regexp_substr(TRIM(lvls),
                      '[^ ]+',
                      1,
                      n) value,
        n
    FROM
             reports
        CROSS JOIN LATERAL ( 
        -- cartesian product to create N rows, depends on the number of values in levels in reports
        -- https://blogs.oracle.com/sql/post/split-comma-separated-values-into-rows-in-oracle-database
            SELECT
                level n
            FROM
                dual
            CONNECT BY
                level <= length(TRIM(lvls)) - length(replace(lvls, ' ', '')) + 1
        )
), difference_cte AS (
    SELECT
        uuid,
        value,
        n,
        value - LAG(value)
                OVER(PARTITION BY uuid
                     ORDER BY
                         uuid, n
        ) diff
    FROM
        hierarchical_cte
)
SELECT
    r.lvls,
    CASE
        WHEN MAX(abs(dcte.diff)) BETWEEN 1 AND 3
             AND ( ( MAX(dcte.diff) > 0
                     AND MIN(dcte.diff) > 0 ) --only increasing
                   OR ( MAX(dcte.diff) < 0
                        AND MIN(dcte.diff) < 0 ) -- only decreasing
                    )
        THEN
            'SAFE'
        ELSE
            'UNSAFE'
    END
FROM
         reports r
    JOIN difference_cte dcte ON ( ora_hash(r.lvls) = dcte.uuid )
GROUP BY
    r.lvls;

DROP TABLE reports PURGE;