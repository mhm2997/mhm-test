class cook(object): #厨师
    __name = None
    __age = None
    def setname(self,cookname):
        self.__name = cookname
    def getname(self):
        return self.__name
    def setage(self,cookage):
        if 0 < cookage <120:
            self.__age = cookage
        else:
            print("年龄有误！")
    def getage(self):
        return self.__age

    def cooking(self):
        print("%s岁的 %s 厨师正在蒸饭"%(self.getage(),self.getname()))

class stirfry(cook):    #炒菜
    def stirfrying(self):
        print("%s岁的%s厨师正在炒菜"%(super().getage(),super().getname()))

class customer(stirfry):
    def eat(self):
        print("%s岁的%s厨师正在炒菜"%(super().getage(),super().getname()))

class test(customer):
    a = customer()
    a.setage(39)
    a.setname("王宝强")
    a.cooking()

