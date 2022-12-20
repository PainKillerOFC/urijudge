select p.name, pv.name from products p
join providers pv
    on pv.id = p.id_providers
where pv.name = 'Ajax SA'