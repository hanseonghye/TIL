# ��¥�� DATA Type

> date --> DATE
����� 4712�� ���� 9999������� ��,��,��,��,��,���� �ڷḦ ����.

> ����
insert into dateTable(d1) values(to_date('20180105','YYMMDD));
select to_char(d1,'YY/MM/DD') from dateTable;

> date type ����
alter session set nls_Date_format='YYYY.MM.DD HH24:MI:SS';

> date type Ȯ��
select sysdate from dual;
