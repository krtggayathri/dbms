def write_data(sql_query):
	import sqlite3
	connection=sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection=sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
class InvalidField(Exception):
    pass
class Student:
    a=''
    b=0
    def __init__(self,name=None,age=None,score=None):
        self.student_id = None
        self.name = name
        self.age = age
        self.score = score
    @classmethod 
    def filter(cls,**kwargs):
        fields=[*cls().__dict__.keys()]
       
        a=''
        d=0
        cls.objects=[]
        cls.li=[]
      #  r=''
        
        for key,value in kwargs.items():
            cls.a=key
            cls.d=value
    
            e=cls.a.split("__")

            if e[0] not in fields:
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
    
            v=' and '.join(cls.li)
            return v
    @classmethod
    def aggregation(cls,agg,field,**kwargs):  
        fields=[*cls().__dict__.keys()]
        #cls.r=''
        if len(kwargs)>=1:
            filter_result=cls.filter(**kwargs)
            print(filter_result)
            v='select {}({}) from student where {} '.format(agg,field,filter_result)
        elif field is None:
            d='select {}(*) FROM student'.format(agg)
        else:
            if field not in fields:
                raise InvalidField
            v='select {}({}) from student '.format(cls.r,field)
        obj=read_data(v)
    
        return obj
    @classmethod
    def avg(cls,field,**kwargs):
         # cls.r='avg'
          d=Student.aggregation('avg',field,**kwargs)
          return d[0][0]
    @classmethod
    def sum(cls,field,**kwargs):
          #cls.r='sum'
          d=Student.aggregation('sum',field,**kwargs)
          return d[0][0]
   
    @classmethod
    def max(cls,field,**kwargs):
          cls.r='max'
          d=Student.aggregation('max',field,**kwargs)
          return d[0][0]
    @classmethod
    def min(cls,field,**kwargs):
          #cls.r='min'
          d=Student.aggregation('min',field,**kwargs)
          return d[0][0]
    @classmethod
    def count(cls,field=None,**kwargs):
        #cls.r='count'
        
        d=Student.aggregation('count',field,**kwargs)
        return d[0][0]
        
        
selected_students = Student.filter(age=40)

