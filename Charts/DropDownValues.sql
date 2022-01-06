
/*WITH
  cte1 AS (SELECT a, b FROM table1),
  cte2 AS (SELECT c, d FROM table2)
SELECT b, d FROM cte1 JOIN cte2
WHERE cte1.a = cte2.c;
*/

/*check completeness*/

WITH
  cte1 AS (SELECT name, id FROM RubyDB.experiments),
  cte2 AS (select distinct experiment FROM RubyDB.limits)
SELECT id, name, experiment FROM cte1 JOIN cte2
WHERE cte1.name = cte2.experiment;

SELECT name, id
FROM RubyDB.experiments;

select distinct experiment
FROM RubyDB.limits;


SELECT distinct
case
	when result_type = 'Th' then 'Theory'
	when result_type = 'Proj' then 'Project'
	when result_type = 'Exp' then 'Experiment'
	else result_type end label,
result_type as value
FROM RubyDB.limits;

-- {'label': 'All', 'value': 'All'},
--            {'label': 'spin-dependent', 'value': 'spin-dependent'},
--            {'label': 'spin-indpendent', 'value': 'spin-indpendent'}   

SELECT distinct
case
	when spin_dependency = 'SD' then 'spin-dependent'
	when spin_dependency = 'SI' then 'spin-indpendent'
	else spin_dependency end name,
spin_dependency as value
FROM RubyDB.limits;

select
case
	when greatest_hit = 0 then 'No'
	when greatest_hit = 1 then 'Yes'
	else greatest_hit end label,
distinct greatest_hit value
FROM RubyDB.limits;

