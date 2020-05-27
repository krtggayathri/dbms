



Q1='''SELECT d.id,d.fname FROM Director as d  
WHERE NOT EXISTS (SELECT m.did FROM MovieDirector as m INNER JOIN Movie as l on l.id=m.mid  
                                WHERE d.id=m.did and year<2000)
AND EXISTS (SELECT m.did FROM  MovieDirector as m INNER JOIN Movie as l on l.id=m.mid  
        WHERE d.id=m.did and year>2000) ORDER BY d.id ASC;'''
        

Q3='''SELECT * FROM Actor as ac
WHERE NOT EXISTS (SELECT c.pid FROM Cast as c INNER JOIN Movie as l on l.id=c.mid
WHERE ac.id=c.pid and year BETWEEN 1990 AND 2000) order by ac.id DESC LIMIT 100;'''





Q2='''SELECT d.fname,(SELECT l.name FROM Movie as l INNER JOIN MovieDirector as md on l.id=md.mid WHERE md.did=d.id order by rank desc,name asc) 
 FROM director as d limit 100;'''
 






