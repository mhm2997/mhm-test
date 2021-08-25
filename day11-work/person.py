class Person:
    __age = None
    __sex = None
    __name = None

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age
    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

# 工人
class Worker(Person):
    __xingwei = None

    def setxingwei(self,xingwei):
        self.__xingwei = xingwei
    def getxingwei(self):
        return self.__xingwei

    def work(self):
        print("有一名%s岁的%s性%s正在%s"%(super().getAge(),super().getSex(),super().getName(),self.__xingwei))

# 学生
class Student(Worker):
    __sid = None

    def setSid(self,sid):
        self.__sid = sid
    def getSid(self):
        return self.__sid

    def studenting(self):
        print("我是学生", self.getName(), "，性别：", self.getSex(), "，年龄：", self.getAge(),"，学号：",self.getSid(),"，我正在",self.getxingwei(),"。")

class test(Student):
    a = Student()
    a.setAge(21)
    a.setName("孟会明")
    a.setSex("男")
    a.setSid("2021107269")
    a.setxingwei("学习、唱歌")
    a.studenting()
    a.work()