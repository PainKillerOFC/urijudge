select c.id, l.name from customers c
join locations l
    on l.id_customers = c.id
where l.locations_date = null