class computer():
    __name=""
    __screen=0  #屏幕
    __price=0
    __cpu=""
    __memory=""
    __time=0


    def computer_name(self,name):
        self.__name=name

    def screen(self,screen):
        if screen>0:
            self.__screen=screen
        else:
            print("输入非法")

    def price(self,price):
        if price>0:
            self.__price=price
        else:
            print("输入非法")

    def cpu(self,cpu):
        self.__cpu=cpu

    def memory(self,memory):
        self.__memory=memory

    def time(self,time):
        if time>0:
            self.__time=time
        else:
            print("输入非法")

    def mode(self):
        print("这台电脑的显示尺寸是",self.__screen,"英寸,价格是",self.__price,"cpu是",self.cpu,
              "内存是",self.__memory,"待机时长",self.__time,"秒")


    def type(self):
        print("我正在用", self.__name, "打字")

    def play(self, game):
        print("我正在用", self.__name, "玩", game)

    def watch(self, watching):
        print("我正在用", self.__name, "看", watching)

c = computer()
c.computer_name("玩家国度rog枪神5puls")
c.screen(17.3)
c.price(18000)
c.cpu("AMD5900X")
c.time(60)
c.mode()
c.type()
c.play("英雄联盟")
c.watch("盗墓笔记")
