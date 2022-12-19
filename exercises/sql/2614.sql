select c.name, r.rentals_date from customers c
join rentals r
    on r.id_customers = c.id
where r.rentals_date >= date '2016-09-01'
    and r.rentals_date < date '2016-10-01';