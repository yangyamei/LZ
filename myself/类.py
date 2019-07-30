# class Person:
#     name="小甲鱼"
#     def test(self):
#         print(self.name)
# p=Person()
# p.test()
class ticket:
    def __init__(self,weekend=False,child=False):
        self.ex=100
        if weekend:
            self.inc=1.2
        else:
            self.inc=1
        if child:
            self.discout=0.5
        else:
            self.discout=1
    def calcount(self,num):
        return self.ex*self.inc*self.discout*num



