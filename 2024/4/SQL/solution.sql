WITH grid AS (
    SELECT
        'MMMSXXMASM' AS letters
    FROM
        dual
    UNION ALL
    SELECT
        'MSAMXMSMSA'
    FROM
        dual
    UNION ALL
    SELECT
        'AMXSXMAAMM'
    FROM
        dual
    UNION ALL
    SELECT
        'MSAMASMSMX'
    FROM
        dual
    UNION ALL
    SELECT
        'XMASAMXAMM'
    FROM
        dual
    UNION ALL
    SELECT
        'XXAMMXXAMA'
    FROM
        dual
    UNION ALL
    SELECT
        'SMSMSASXSS'
    FROM
        dual
    UNION ALL
    SELECT
        'SAXAMASAAA'
    FROM
        dual
    UNION ALL
    SELECT
        'MAMMMXMMMM'
    FROM
        dual
    UNION ALL
    SELECT
        'MXMXAXMASX'
    FROM
        dual
), y_axis AS (
    SELECT
        letters,
        ROWNUM arr_y
    FROM
        grid
), full_grid AS (
    SELECT
        substr(t.letters, level, 1) AS letter,
        level                       AS arr_x,
        t.arr_y
    FROM
        y_axis t
    CONNECT BY level <= length(t.letters)
               AND PRIOR t.arr_y = t.arr_y
               AND PRIOR sys_guid() IS NOT NULL -- avoid infinite loop on connect by
)
SELECT
    *
FROM
    full_grid;
    
--   
-- max(arr_x) - min(arr_x) = 3 and concat(letter) = 'XMAS' or = 'SMAX'
--