select c.id, c.name
from customers c

where not exists(
	select id_customers
	from locations l
	where id_customers = c.id
)