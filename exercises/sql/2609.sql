select ctg."name", sum(prd."amount")
from categories ctg

join products prd
	on ctg."id" = prd."id_categories"

group by ctg."name"
order by ctg."name"