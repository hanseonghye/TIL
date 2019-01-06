# for loop

for i in 0..100 loop
	처리문;
end loop;

> 예시
set serveroutput on;

declare
	i number;
begin
	for i in 1..100 loop
		dbms_output.put_line('i:' || i);
	end loop;
end; 
