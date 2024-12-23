SET SERVEROUTPUT ON;

CREATE TYPE numbers IS
    TABLE OF NUMBER;
/

CREATE OR REPLACE FUNCTION get_lists_distance (
    p_first_list  numbers,
    p_second_list numbers
) RETURN NUMBER AS
    v_first_list_sorted  numbers;
    v_second_list_sorted numbers;
    v_solution           NUMBER := 0;
BEGIN
    IF p_first_list.count <> p_second_list.count THEN
        raise_application_error(-20001, 'Inputs have to be the same length.');
    END IF;

    SELECT
        column_value
    BULK COLLECT
    INTO v_first_list_sorted
    FROM
        TABLE ( p_first_list )
    ORDER BY
        1;

    SELECT
        column_value
    BULK COLLECT
    INTO v_second_list_sorted
    FROM
        TABLE ( p_second_list )
    ORDER BY
        1;

    FOR i IN 1..v_first_list_sorted.count LOOP
        v_solution := v_solution + abs(v_first_list_sorted(i) - v_second_list_sorted(i));
    END LOOP;

    RETURN v_solution;
EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line('Error occurred: ' || sqlerrm);
        RETURN NULL;
END;
/

DECLARE
    v_first_example  numbers := numbers(3, 4, 2, 1, 3,
                                      3);
    v_second_example numbers := numbers(4, 3, 5, 3, 9,
                                       3, 3);
BEGIN
    dbms_output.put_line(get_lists_distance(v_first_example, v_second_example));
END;
/