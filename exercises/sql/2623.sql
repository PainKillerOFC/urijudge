-- exiba o nome do produto
-- exiba o nome da categoria
select prod.name, cat.name
from products prod

join categories cat
	on cat.id = prod.id_categories

-- cuja quantidade seja maior que 100
-- e o código da categoria seja 1,2,3,6 ou 9.
where
	prod.amount > 100 and
	prod.id_categories in (1,2,3,6,9)