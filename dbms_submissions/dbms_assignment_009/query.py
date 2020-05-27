

Q1='''SELECT AVG(age) FROM player'''
Q2='''SELECT match_no,play_date FROM match WHERE audience>50000 ORDER By match_no ASC;'''
Q3='''SELECT team_id, count(win_lose) as no_of_matches FROM MatchTeamDetails WHERE win_lose='W' GROUP BY team_id order by no_of_matches desc, 
team_id asc;'''

Q4='''SELECT match_no,play_date FROM match WHERE stop1_sec>
(SELECT AVG(stop1_sec) FROM match) order BY match_no DESC;'''

Q5='''SELECT mtd.match_no,t.name,p.name FROM ((Team as t INNER JOIN Matchcaptain as mtd on 
t.team_id=mtd.team_id)INNER JOIN Player as p on p.player_id=mtd.captain) ORDER BY mtd.match_no asc,t.name asc;'''

Q6='''SELECT match_no,name,jersey_no FROM match INNER JOIN player on player_id=player_of_match order BY match_no;'''

Q7='''SELECT name,(SELECT avg(age) FROM player p  WHERE t.team_id=p.team_id) As avg_age  FROM team as t 
WHERE avg_age>26 order by name ;'''
Q8='''SELECT mtd.name,mtd.jersey_no,mtd.age ,count(goal_id) as no_of_goals FROM goaldetails as t INNER JOIN player mtd on
t.player_id=mtd.player_id where age<=27  
group by mtd.player_id order by no_of_goals DESC,mtd.name ASC;'''

Q10='''SELECT avg(count_goals) FROM (SELECT count(goal_id) as count_goals FROM goaldetails
GROUP By team_id);'''
Q11='''SELECT player_id,name,date_of_birth FROM player as p WHERE NOT EXISTS 
(SELECT goal_id from goaldetails as g WHERE g.player_id=p.player_id)'''

Q9='''SELECT team_id,count(goal_id)*100.0/(select count(goal_id) from goaldetails) from goaldetails group By team_id;'''





Q12='''SELECT t.name,m.match_no,m.audience,
m.audience-(SELECT avg(audience)
FROM matchcaptain as mtc INNER JOIN match as m on mtc.match_no=m.match_no where t.team_id=mtc.team_id)
FROM match m INNER JOIN matchcaptain as mtc on mtc.match_no=m.match_no
INNER JOIN team as t on t.team_id=mtc.team_id 
order by m.match_no asc;
'''




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 