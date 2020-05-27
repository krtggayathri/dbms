

class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass
class Student:
    a=''
    b=0
    
    def __init__(self,name,age, score):
        self.student_id = None
        self.name = name
        self.age = age
        self.score = score
    
    @classmethod
    def get(cls,**kid):
        
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
                                
       
        for k,v in kid.items():
           cls.a=k
           cls.b=v
        #print(cls.a)
        #print(cls.b)
        col=["student_id","name","age","score"]  
        if cls.a not in col:
            raise InvalidField
        if cls.a == 'name':
            sql_query="select * from Student where {}=\'{}\'".format(cls.a,cls.b) 
        else:
            sql_query="select * from Student where {}={}".format(cls.a,cls.b) 
        
        crsr.execute(sql_query) 
        ans=crsr.fetchall()
        #print(ans)
        if len(ans)==0:
            raise DoesNotExist
        if len(ans)>1:
            raise MultipleObjectsReturned
        obj=Student(ans[0][1],ans[0][2],ans[0][3])
        obj.student_id=ans[0][0]
        #print(obj.student_id)
        conn.close()
        return obj
        
        
    def delete(self):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
        crsr.execute("PRAGMA foreign_keys=on;") 
        sql_query="Delete FROM Student where student_id={}".format(self.student_id)
        
        crsr.execute(sql_query) 
        conn.commit()
        conn.close()
    
    
    def save(self):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
        crsr.execute("PRAGMA foreign_keys=on;") 
        #print(self.student_id)
        #print(self.b)
        if self.student_id!=None:
            sql_query="UPDATE Student SET student_id={},name='{}',age={},score={} where student_id={};".format(self.student_id,self.name,self.age,self.score,self.b)
            crsr.execute(sql_query) 
        else:
            sql_query="INSERT INTO Student(name,age,score) values('{}',{},{})".format(self.name,self.age,self.score)
            crsr.execute(sql_query)
            q="select student_id from student where name='{}' and age={} and score={}".format(self.name,self.age,self.score)
            crsr.execute(q)
            ans=crsr.fetchall()
            #self.student_id=crsr.lastrowid
            self.student_id=ans[0][0]
        print(self.student_id)
        conn.commit()
        conn.close
        









