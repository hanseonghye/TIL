**sql 예시**



* pl/sql을 통한 1건 단위 처리

```sql 
declare
	v_cust_grade varchar2(1);
begin
	for rec in
	(
    	select
    		c.cust_id,
        	nvl(sum(oi.order_price),0) order_price
        from
        	customers c, orders o, order_items oi
        where
        	c.cust_id=o.cust_id(+)
        	and o.order_dt(+) >= to_date('20180107','YYYYMMDD')
        group by c.cust_id
        order by c.cust_id;
    )
    loop
    	if rec.order_price<10 then v_cust_grade:='1';
    	elsif rec.order_price<50 then v_cust_grade:='2';
    	else v_cust_grade:='3';
    	end if;
    	
    	update customers set cust_grade=v_cust_grade where cust_id=rec.cust_id;
    end loop;
    commit;
end;    
```



* 1개 sql문장에 의한 처리

```sql

merge into customers c
using
(
	select
		cust_id.
		case
			when order_price<10 then '1'
			when order_price<50 then '2'
			else '3'
		end cust_grade
	from
	(
		select c.cust_id, nvl(sum(oi.order_price),0) order_price
		from customers c, orders o, order_items oi
		where c.cust_id=o.cust_id(+)
		and o.order~
		group by c.cust_id
		)
) a
on (c.cust_id=a.cust_id)
when matched then
	update set cust_grade=cust_grade

```