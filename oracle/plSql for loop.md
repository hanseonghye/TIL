# for loop

for i in 0..100 loop
	ó����;
end loop;

> ����
set serveroutput on;

declare
	i number;
begin
	for i in 1..100 loop
		dbms_output.put_line('i:' || i);
	end loop;
end; 
