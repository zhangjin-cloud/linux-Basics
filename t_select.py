from table import emp,Students,Session
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
qset3=session.query(emp.job)
print('%-6s' %  '工作岗位')
for i in qset3:
    print(i)

session.commit()
session.close()

