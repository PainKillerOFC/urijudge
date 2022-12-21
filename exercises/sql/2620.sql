-- exiba o nome dos clientes
-- e o número do pedido
select cus.name, ord.id
from customers cus

join orders ord
	on ord.id_customers = cus.id

-- para os clientes que fizeram pedidos
-- no primeiro semestre de 2016.
where
	ord.orders_date > '2016-01-01' and
	ord.orders_date < '2016-07-01'