import time
class oldphone(object):
    __brand = None
    __num = None
    __vioce = None
    __address = None

    def setbrand(self,brand):
        self.__brand = brand
    def getbrand(self):
        return self.__brand
    def setbnum(self,num):
        self.__num = num
    def getnum(self):
        return self.__num
    def setvioce(self,vioce):
        self.__vioce = vioce
    def getvioce(self):
        return self.__vioce
    def setaddress(self,address):
        self.__address = address
    def getaddress(self):
        return self.__address

    def call(self,phonenum):
        print("手机号为",self.getnum(),"的",self.getbrand(),"牌手机正在给",phonenum,"打电话。",)
        for i in range(0,5):
            print(".",end="")
            time.sleep(0.3)
        print("正在响铃:",self.getvioce(),"、本机号码归属地为：",self.getaddress())

class newphone(oldphone):
    def newcall(self,newnum):
        super().call(newnum)
        print("品牌为：%s的手机很好用..."%self.getbrand())

class test(newphone):
    a = oldphone()
    a.setbrand("红米")
    a.setaddress("沧州")
    a.setvioce("星河万里")
    a.setbnum(13832735229)
    a.call(17720137069)

    b = newphone()
    b.setbrand("HuaWei")
    b.setbnum(123)
    b.newcall(456)

#定义类后边要有括号
#super(). 调用父类时可以用父类的变量参数也可以用自己的变量参数