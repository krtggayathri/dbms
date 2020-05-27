
def write_data(sql_query):
	import sqlite3
	connection=sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection=sqlite3.connect("selected_students.sqlite3")

	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

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
    
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)
            
    @classmethod
    def get(cls,**kid):
          
       
        for k,v in kid.items():
            print(k,v)
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
        
        ans=read_data(sql_query) 
        
        
       # print(ans)
        if len(ans)==0:
            raise DoesNotExist
        if len(ans)>1:
            raise MultipleObjectsReturned
        obj=Student(ans[0][1],ans[0][2],ans[0][3])
        obj.student_id=ans[0][0]
        #print(obj.student_id)
        
        return obj
        
        
    def delete(self):
       
        sql_query="Delete FROM Student where student_id={}".format(self.student_id)
        
        write_data(sql_query)
    
    def save(self):
        
        if self.student_id!=None:
            sql_query="UPDATE Student SET student_id={},name='{}',age={},score={} where student_id={};".format(self.student_id,self.name,self.age,self.score,self.b)
            write_data(sql_query) 
        else:
            sql_query="INSERT INTO Student(name,age,score) values('{}',{},{})".format(self.name,self.age,self.score)
            write_data(sql_query)
            q="select student_id from student where name='{}' and age={} and score={}".format(self.name,self.age,self.score)
            r=read_data(q)
           
            #self.student_id=crsr.lastrowid
            self.student_id=r[0][0]
            
   
        
    @classmethod 
    def filter(cls,**keys):
        a=''
        d=0
        cls.objects=[]
        cls.li=[]
        for key,value in keys.items():
            cls.a=key
            cls.d=value
        
            #if '__' in cls.a :
            
            e=cls.a.split("__")
                #cls.d=value
            
                
            if e[0] not in ('student_id','name','age','score'):
                raise InvalidField
           
            if len(e)>1:
                if e[1]=='lt':
                        sql_query="{}<{}".format(e[0],cls.d)
                           
                elif e[1]=='lte':
                    sql_query="{}<='{}'".format(e[0],cls.d)
                           # obj=read_data(sql_query)
                elif e[1]=='gt':
                    sql_query="{}>{}".format(e[0],cls.d)
                            #obj=read_data(sql_query)
                elif e[1]=='gte':
                    sql_query="{}>={}".format(e[0],cls.d)
                            #obj=read_data(sql_query)
                elif e[1]=='neq':
                    sql_query="{}!='{}'".format(e[0],cls.d)
                            #obj=read_data(sql_query)
                elif e[1]=='in':
                    sql_query="{} in {}".format(e[0],tuple(cls.d))
                           # obj=read_data(sql_query)
                elif e[1]=='contains':
                    sql_query="{} like '%{}%'".format(e[0],cls.d)
            elif (len(e))==1:
                sql_query="{}='{}'".format(cls.a,cls.d)
                
                
            cls.li.append(sql_query)
            print(cls.li)
            v=' and '.join(cls.li)
            print(v)
        v='select * from student where '+v
                
        print(v)       
                
        obj=read_data(v)
        for i in range (len(obj)):
            obj1=Student(obj[i][1],obj[i][2],obj[i][3])
            obj1.student_id=obj[i][0]
            cls.objects.append(obj1)
        return cls.objects


selected_students = Student.filter(age__in = [25, 34], score__lt=50)
print(selected_students)

'''
def write_data(sql_query):
	import sqlite3
	connection=sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection=sqlite3.connect("selected_students.sqlite3")

	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

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
    
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)
            
    @classmethod
    def get(cls,**kid):
          
       
        for k,v in kid.items():
            print(k,v)
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
        
        ans=read_data(sql_query) 
        
        
       # print(ans)
        if len(ans)==0:
            raise DoesNotExist
        if len(ans)>1:
            raise MultipleObjectsReturned
        obj=Student(ans[0][1],ans[0][2],ans[0][3])
        obj.student_id=ans[0][0]
        #print(obj.student_id)
        
        return obj
        
        
    def delete(self):
       
        sql_query="Delete FROM Student where student_id={}".format(self.student_id)
        
        write_data(sql_query)
    
    def save(self):
        
        if self.student_id!=None:
            sql_query="UPDATE Student SET student_id={},name='{}',age={},score={} where student_id={};".format(self.student_id,self.name,self.age,self.score,self.b)
            write_data(sql_query) 
        else:
            sql_query="INSERT INTO Student(name,age,score) values('{}',{},{})".format(self.name,self.age,self.score)
            write_data(sql_query)
            q="select student_id from student where name='{}' and age={} and score={}".format(self.name,self.age,self.score)
            r=read_data(q)
           
            #self.student_id=crsr.lastrowid
            self.student_id=r[0][0]
            
   
        
    @classmethod 
    def filter(cls,**keys):
        a=''
        d=0
        cls.objects=[]
        cls.li=[]
        for key,value in keys.items():
            cls.a=key
            cls.d=value
            print(cls.a)
            print(cls.d)
            #if '__' in cls.a :
            
            e=cls.a.split("__")
                #cls.d=value
            
                
            if e[0] not in ('student_id','name','age','score'):
                raise InvalidField
           
            if len(e)>1:
                if e[1]=='lt':
                        sql_query="select * from student where {}<{}".format(e[0],cls.d)
                           
                elif e[1]=='lte':
                    sql_query="select * from student where {}<='{}'".format(e[0],cls.d)
                           # obj=read_data(sql_query)
                elif e[1]=='gt':
                    sql_query="select * from student where {}>{}".format(e[0],cls.d)
                            #obj=read_data(sql_query)
                elif e[1]=='gte':
                    sql_query="select * from student where {}>={}".format(e[0],cls.d)
                            #obj=read_data(sql_query)
                elif e[1]=='neq':
                    sql_query="select * from student where {}!='{}'".format(e[0],cls.d)
                            #obj=read_data(sql_query)
                elif e[1]=='in':
                    sql_query="select * from student where {} in {}".format(e[0],tuple(cls.d))
                           # obj=read_data(sql_query)
                elif e[1]=='contains':
                    sql_query="select * from student where {} like '%{}%'".format(e[0],cls.d)
            elif (len(e))==1:
                sql_query="select * from student where {}='{}'".format(cls.a,cls.d)
                
        obj=read_data(sql_query)  
            
        cls.li.append(obj)
        x=list(set.intersection(*map(set, cls.li)))
        
          #  print(cls.li)
            #v=' and '.join(cls.li)
            #print(v)
        #v='select * from student where '+v
                
       # print(v)       
                
        
        for i in range (len(x)):
            obj1=Student(obj[i][1],obj[i][2],obj[i][3])
            obj1.student_id=obj[i][0]
            cls.objects.append(obj1)
        return cls.objects



selected_students = Student.filter(age__in = [21,20], score__lt=100)
print(selected_students)
'''







