select prd.id, prd.name from products prd
join categories cat
    on prd.id_categories = cat.id
where cat.name like 'super%'