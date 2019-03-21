'''
定义一个类
'''

class Student():
    pass

# 定义一个对象
mingyue = Student()

# 再定义一个类
class PythonStudent():
    # 用None跟不确定赋值
    name = None
    age = 18
    course = "Python"
    def doHomework(self):
        print("I 在做作业")

        return None

yueyue = PythonStudent()
print(yueyue.name)
yueyue.doHomework()
