select cus.name from customers cus

join legal_person lp
    on lp.id_customers = cus.id

where lp.id_customers = cus.id