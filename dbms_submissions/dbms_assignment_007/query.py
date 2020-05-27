
Q1='''SELECT COUNT(ID) FROM Movie WHERE year<2000;'''
Q2='''SELECT AVG(rank) FROM Movie WHERE year=1991;'''
Q3='''SELECT MIN(rank) FROM Movie WHERE year=1991;'''
Q4='''SELECT fname,lname FROM Actor INNER JOIN Cast on id=pid WHERE mid=27;'''
Q5='''SELECT COUNT(DISTINCT mid) FROM Actor INNER JOIN Cast on id==pid WHERE 
        fname="Jon" and lname="Dough" '''
        
Q6='''SELECT name FROM Movie Where name LIKE "Young Latin Girls%" 
        AND (year BETWEEN 2003 AND 2006);'''
        
Q7='''SELECT DISTINCT fname,lname FROM ((Director INNER JOIN MovieDirector on `Director`.id='MovieDirector'.did)INNER JOIN Movie on 'Movie'.id='Moviedirector'.mid) 
        WHERE `Movie`.name LIKE "Star Trek%" and `MovieDirector`.mid>1;'''    
        
Q9='''SELECT fname,lname FROM ((Director INNER JOIN MovieDirector on `Director`.id=`MovieDirector`.did) INNER JOIN Movie on `Movie`.id=`Moviedirector`.mid) 
        WHERE year=2001 GROUP BY did HAVING COUNT(mid)>=4 ORDER By fname ASC,lname DESC;'''   
Q10='''SELECT gender,COUNT(gender) as 'M' FROM Actor Group By gender;'''

Q8='''SELECT name FROM ((Movie INNER JOIN MovieDirector on `movie`.id=`MovieDirector`.mid)
        INNER JOIN Director on `Director`.id=`MovieDirector`.did
        INNER JOIN Cast on `Cast`.mid=`Movie`.id 
        INNER JOIN Actor on  `Actor`.id=`Cast`.pid) 
        WHERE (`Actor`.fname="Jackie (I)" and `Director`.fname="Jackie (I)" ) and 
        (`Actor`.lname="Chan" and `Director`.lname="Chan" ) ORDER BY name ASC''';
        


Q11='''SELECT DISTINCT m1.name,m2.name,m1.rank,m1.year FROM Movie as m1,Movie as m2 WHERE (m1.year=m2.year and m1.rank=m2.rank) and m1.name<>m2.name 
        ORDER BY m1.name ASC lIMIT 100;'''

       

        
Q12='''SELECT fname,year,AVG(rank) FROM ((Movie  INNER JOIN Cast on `Movie`.id=`Cast`.mid)
        INNER JOIN Actor on `Actor`.id=`Cast`.pid) GROUP BY year,`actor`.id ORDER BY fname ASC,`movie`.year DESC LIMIT 100;'''  
        
Q13='''SELECT `actor`.fname,`Director`.fname,AVG(rank) FROM ((Actor INNER JOIN cast on `actor`.id=`cast`.pid)
        INNER JOIN MovieDirector on  `MovieDirector`.mid=`cast`.mid 
        INNER JOIN Director on `Director`.id=`MovieDirector`.did
        INNER JOIN Movie on `Movie`.id=`MovieDirector`.mid)
        GROUP BY `Director`.id ,`Actor`.id HAVING COUNT(`MovieDirector`.mid)>=5 ORDER BY avg(rank) DESC,`Director`.fname ASC,`Actor`.fname DESC LIMIT 100;'''









       
        
