



Q1='''select p.player_id,mtc.team_id,p.jersey_no,p.name,p.date_of_birth,p.age 
from player as p JOIN matchcaptain as 
mtc  on mtc.captain=p.player_id 
LEFT JOIN goaldetails as g on mtc.captain=g.player_id where goal_id=null

'''

Q1='SELECT  P.PLAYER_ID, MC.TEAM_ID, P.JERSEY_NO, P.NAME,P.DATE_OF_BIRTH, P.AGE 
FROM MATCHCAPTAIN AS MC JOIN PLAYER AS P ON MC.CAPTAIN = P.PLAYER_ID
left JOIN GOALDETAILS AS GD ON GD.PLAYER_ID = MC.CAPTAIN
WHERE GOAL_ID IS NULL
'''

Q2='''select team_id,count(match_no) from matchteamdetails group by team_id;
'''

Q3='''select team_id,(select count(goal_id)/23.0) from goaldetails
group by team_id 
'''
 

Q4='''select captain,count(captain) from matchcaptain as mtc 
INNER JOIN player as p
on p.player_id=mtc.captain group by p.player_id
'''
Q5='''select count(distinct player_id) as no_players From player as p 
INNER JOIN MatchCaptain as mc on p.player_id=mc.captain 
inner join match as m on m.match_no=mc.match_no 
where p.player_id=mc.captain and
p.player_id=m.player_of_match;   
'''
Q6='''select distinct player_id from player p 
where exists (select mtc.captain FROM matchcaptain as mtc 
where mtc.captain=p.player_id)
AND NOT EXISTS (select m.player_of_match from match as m 
where p.player_id=m.player_of_match)
'''
Q7='''select strftime("%m",play_date),count(match_no) as no_of_matches 
FROM match group BY 
strftime("%m",play_date);
'''
Q8='''select p.jersey_no,count(captain) as no_of_captain from player as p 
   inner join matchcaptain as mc on mc.captain=p.player_id group by jersey_no 
   order by no_of_captain desc,p.jersey_no desc;
'''

Q9='''select p.player_id,avg(audience) as average_audience from player as p 
inner join matchteamdetails as mtc on mtc.team_id=p.team_id
inner join match as m on m.match_no=mtc.match_no group By p.player_id 
order by average_audience desc,p.player_id desc;
'''
Q10='''select team_id,avg(age) from player group by team_id'''

Q11='''select avg(age) as average_age_of_captain FROM player as p 
INNER JOIN matchcaptain as mtc on p.player_id=mtc.captain'''

Q12='''select strftime("%m",date_of_birth),count(player_id) as no_of_players 
from player as p group By strftime("%m",date_of_birth) 
order by no_of_players desc,strftime("%m",date_of_birth) desc;
'''
Q13='''select mc.captain,count(win_lose) as no_of_wins FROM matchcaptain as mc
INNER JOIN matchteamdetails as mtc on  mc.match_no=mtc.match_no
where mtc.win_lose='W' and mc.team_id=mtc.team_id
group by mc.captain order by no_of_wins desc;
'''












