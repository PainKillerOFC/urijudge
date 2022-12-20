-- nome dos produtos
-- o nome do fornecedor
-- nome da categoria
select pd.name, pv.name, cat.name
from products pd

join providers pv
	on pv.id = pd.id_providers
join categories cat
	on cat.id = pd.id_categories

-- somente do fornecedor ‘Sansul SA’
-- somente da categoria 'Imported'.
where
	pv.name = 'Sansul SA' and
	cat.name = 'Imported'