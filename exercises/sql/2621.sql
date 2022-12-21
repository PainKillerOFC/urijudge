-- Exiba o nome dos produtos
select prod.name
from products prod

join providers prov
	on prov.id = prod.id_providers

where
-- cujas quantidades estejam entre 10 e 20
	amount between 10 and 20
-- cujo nome do fornecedor inicie com a letra ‘P’.
	and prov.name like 'P%'