class watercup():
    __height = None
    __color = None
    __cailiao = None
    __rongliang = None
    __liquid = None
    __drank = None

    def setwatercup(self,height,rongliang,color,cailiao,liquid,drank):
        self.setheight(height)
        self.setronglaing(rongliang)
        self.setcolor(color)
        self.setcailiao(cailiao)
        self.setliquid(liquid)
        self.setdrank(drank)

    def setheight(self,height):
        if height <= 0:
            print("水杯高度不合理！")
        else:
            self.__height = height
    def getheight(self):
        return self.__height

    def setronglaing(self,rongliang):
        self.__rongliang = rongliang
    def getrongliang(self):
        return self.__rongliang

    def setcolor(self,color):
        self.__color = color
    def getcolor(self):
        return self.__color

    def setcailiao(self,cailiao):
        self.__cailiao = cailiao
    def getcailiao(self):
        return self.__cailiao

    def setliquid(self,liquid):
        self.__liquid = liquid
    def getliquid(self):
        return self.__liquid

    def setdrank(self,drank):
        self.__drank = drank
    def getdrank(self):
        return self.__drank()

    def cunfang(self):
        print(self.__height,"厘米高的",self.__color,"色",self.__cailiao,"杯里存放了",self.__rongliang,"毫升",self.__liquid)

    def drank(self,):
        print("喝了几口，被子里还剩下",self.__rongliang - self.__drank,"毫升。")
w = watercup()
w.setwatercup(20,550,"透明","塑料","青梅绿茶",400)
w.cunfang()
w.drank()

ww = watercup()
ww.setwatercup(13,250,"白","瓷","白酒",200)
ww.cunfang()
ww.drank()