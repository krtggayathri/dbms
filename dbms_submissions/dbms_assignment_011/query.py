Q1='''select a.id,a.fname,a.lname,a.gender FROM Actor as a 
INNER JOIN cast as c on c.pid=a.id 
INNER JOIN Movie as m on m.id=c.mid 
WHERE m.name LIKE "Annie%"
'''
Q2='''select m.id,m.name,m.rank,m.year FROM Movie as m 
INNER JOIN MovieDirector as md on md.mid=m.id 
INNER JOIN Director as d on d.id=md.did
WHERE (fname="Biff" and lname="Malibu") and year IN (1999,1994,2003)
ORDER By rank desc,year ASC;
'''
Q3='''select year,count(id) as no_of_movies FROM movie GROUP By year 
HAVING AVG(rank)>(select avg(rank) from movie) order by year asc;
'''
Q4='''select id,name,year,rank FROM Movie where year=2001 and rank<(select avg(rank) 
FROM Movie where year=2001) order by rank desc limit 10;
'''
Q5='''SELECT m.id,
(SELECT count(a.gender) from Actor as a 
INNER JOIN cast as c on c.pid=a.id where c.mid=m.id and gender='M') as no_of_males,
(SELECT count(a.gender) from Actor as a 
INNER JOIN cast as c on c.pid=a.id where  c.mid=m.id and gender='F' ) as no_of_females
from Movie as m order by m.id ASC limit 10;
'''

Q6='''select c.pid from cast as c INNER JOIN Actor as a on  a.id=c.pid 
group by c.pid,c.mid having count(distinct role)>1 order by c.pid ASC;
'''


Q7='''select fname,count(id) FROM director group by fname having count(fname)>1;
'''

Q8='''select d.id,d.fname,d.lname FROM director as d
WHERE EXISTS
(select c.pid From MovieDirector as md
INNER JOIN Cast as c on c.mid=md.mid where d.id=md.did group by md.mid having count(distinct pid)>=100) 
AND NOT EXISTS
(select c.pid From MovieDirector as md
INNER JOIN Cast as c on c.mid=md.mid where d.id=md.did group by md.mid having count(distinct pid)<100) 
'''

Q5='''select no_of_males.pid,no_of_males.md,no_of_females.pid,no_of_females.fd
FROM(
select pid,count(gender) as md from Actor 
INNER JOIN Cast on pid=id where
 gender='M') AS no_of_males JOIN
 (
select pid,count(gender) as fd from Actor 
INNER JOIN Cast on pid=id where
 gender='F') AS no_of_females
 


''' 