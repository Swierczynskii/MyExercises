create table corrupted_memories ( section )
   as
      select 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(123, 123)'
        from dual;



with muls as (
   select regexp_substr(
      section,
      'mul\(\d{1,3},\d{1,3}\)',
      1,
      level
   ) mul
     from corrupted_memories
   connect by
      level <= regexp_count(
         section,
         'mul\(\d{1,3},\d{1,3}\)'
      )
)
select sum(regexp_substr(
   mul,
   '\d{1,3}',
   1,
   1
) * regexp_substr(
   mul,
   '\d{1,3}',
   1,
   2
)) summed_up
  from muls;

drop table corrupted_memories purge;

-- Alternatively
-- try to do it without regexp (using substr/instr)