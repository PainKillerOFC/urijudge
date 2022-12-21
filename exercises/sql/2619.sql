-- exibir nome dos produtos
-- nome dos fornecedores
-- preço
select prod.name, prov.name, prod.price
from products prod

join providers prov
	on prod.id_providers = prov.id
join categories cat
	on prod.id_categories = cat.id

where
-- somente produtos com preço > 1000
	prod.price > 1000 and
-- somente da categoria Super Luxury
	cat.name = 'Super Luxury'