from table import emp,Students,Session
from sqlalchemy import distinct
from sqlalchemy.sql import func
session=Session()

print('#'*30,(1),'#'*30)
qset1=session.query(Students.id,Students.name)
print('%-6s%-6s' % ('id号', '姓名'))
for a,b in qset1:
    print('%-6s%-6s'% (a,b))

print('#'*30,(2),'#'*30)
qset2=session.query(Students.name,Students.chinese)
print('%-8s%-8s' % ('姓名', '语文'))
for a,b in qset2:
    print('%-8s%-8s' % (a, b))

print('#'*30,(3),'#'*30)
qset3=session.query(distinct(emp.job)).all()
print('%-6s' %  '工作岗位')
for i in qset3:
    print(i)

print('#'*30,(4),'#'*30)
qset4=session.query(Students.chinese,Students.english,Students.math)
print('%-6s' %  '所有学生总分数')
for a,b,c in qset4:
    d=a+b+c+10
    print(d)

print('#'*30,(5),'#'*30)
qset5=session.query(Students.chinese,Students.english,Students.math).filter(Students.name=='张小明').all()
for i in qset5:
    print(i[0],i[1],i[2])

print('#'*30,(6),'#'*30)
qset6=session.query(Students.name).filter(Students.english>=90).all()
for i in qset6:
    print(i)

print('#'*30,(7),'#'*30)
qset7=session.query(Students.name,Students.chinese,Students.english,Students.math)
for z,x,c,t in qset7:
    n=x+c+t
    if n>200:
        print(z)

print('#'*30,(8),'#'*30)
qset8=session.query(Students.name,Students.math)
for n1,m1 in qset8:
    if m1 in [89,90,91]:
        print(n1)

print('#'*30,(9),'#'*30)
qset9=session.query(Students.name,Students.english)
for n2,e1 in qset9:
    if 80<=e1<=90:
        print(n2)

print('#'*30,(10),'#'*30)
qset10=session.query(Students).filter(Students.name.like("李%")).all()
for i in qset10:
    print(i.name,i.chinese,i.english,i.math)

print('#'*30,(11),'#'*30)
qset11=session.query(Students).filter(Students.name.like("_李%")).all()
for i in qset11:
    print(i.name,i.chinese,i.english,i.math)

print('#'*30,(12),'#'*30)
qset12=session.query(Students).filter(Students.name.like("李_")).all()
for i in qset12:
    print(i.name)

print('#'*30,(13),'#'*30)
qset13=session.query(Students).filter(Students.name.like("李_")).all()
for i in qset13:
    print(i.name)

print('#'*30,(14),'#'*30)
qset14=session.query(Students).filter(Students.name.like("%李%")).all()
for i in qset14:
    print(i.name,i.chinese,i.english,i.math)

print('#'*30,(15),'#'*30)
qset15=session.query(Students).filter(Students.name.like("李__")).all()
for i in qset15:
    print(i.name,i.chinese,i.english,i.math)

print('#'*30,(16),'#'*30)
qset16=session.query(Students).order_by(Students.math.desc()).all()
for i in qset16:
    print(i.name,i.math)

print('#'*30,(17),'#'*30)
qset17=session.query(Students).order_by(Students.math.desc(),Students.chinese.desc())
for i in qset17:
    print(i.name,i.chinese,i.english,i.math)

print('#'*30,(18),'#'*30)
qest18=session.query(Students).order_by(Students.chinese.desc(),Students.english.desc(),Students.math.desc()).all()
for i in qest18:
    zf=i.chinese+i.english+i.math
    print('%-8s%-8s' % (i.name,zf))

print('#'*30,(19),'#'*30)
qset19=session.query(Students).order_by(Students.chinese.desc(),Students.english.desc(),\
                                        Students.math.desc()).filter(Students.name.like("李%"))
for i in qset19:
    zf=i.chinese+i.english+i.math
    print(i.name,zf)

print('#'*30,(20),'#'*30)
qset20=session.query(Students.name).count()
print(qset20)



print('#'*30,(21),'#'*30)
qset21=session.query(Students).filter(Students.math>80).all()
for i in qset21:
    print(i.name)

print('#'*30,(22),'#'*30)
qset22=session.query(Students.name,Students.chinese,Students.english,Students.math)
a=0
for z,x,c,t in qset22:
    n=x+c+t
    if n>250:
        a+=1
print(a)


print('#'*30,(23),'#'*30)
qset23=session.query(Students.math)
s=0
for i in qset23:
    s=s+i[0]
print(s)

print('#'*30,(24),'#'*30)
qset24=session.query(Students.chinese,Students.english,Students.math)
ch=0;en=0;ma=0
for a1,a2,a3 in qset24:
    ch=ch+a1
    en=en+a2
    ma=ma+a3
print(ch,en,ma)


print('#'*30,(25),'#'*30)
qset25=session.query(Students.chinese,Students.english,Students.math)
ch=0;en=0;ma=0
for a1,a2,a3 in qset24:
    ch=ch+a1
    en=en+a2
    ma=ma+a3
    sun=ch+en+ma
print(sun)


print('#'*30,(26),'#'*30)
qset26=session.query(func.avg(Students.chinese))
for i in qset26:
    print(i[0])

print('#'*30,(27),'#'*30)
qset27=session.query(func.sum(Students.chinese),func.sum(Students.english),func.sum(Students.math),func.count(Students.id))
for ch,en,ma,sid in qset27:
    av=(ch+en+ma)/sid
    print(av)


print('#'*30,(28),'#'*30)
qset28=session.query(func.max(Students.math),func.min(Students.math))
for mx,mi in qset28:
    print(mx,mi)


print('#'*30,(29),'#'*30)
f1=session.query(emp).filter(emp.sal>15000).filter(emp.job=='分析师').count()
f2=session.query(emp).filter(emp.sal>15000).filter(emp.job=='销售员').count()
f3=session.query(emp).filter(emp.sal>15000).filter(emp.job=='经理').count()
f4=session.query(emp).filter(emp.sal>15000).filter(emp.job=='董事长').count()
f5=session.query(emp).filter(emp.sal>15000).filter(emp.job=='文员').count()
print('分析师:%s人,销售员:%s人,经理:%s人,董事长:%s人,文员:%s人'%  (f1,f2,f3,f4,f5))


print('#'*30,(30),'#'*30)
ff=[f1,f2,f3,f4,f5]
for i in ff:
    if i>=3:
        print(i)




session.commit()
session.close()

