# Week 16 - ICA 1

class Car:
     def __inti__(self,yr,mk,md):
         self.year = yr
         self.make = mk
         self.model = md
         self.speed = 0

    def  accelerate(self):
        self.__speed += 1

    def brake(self):
        self.__speed -= 10

    def how_fast(self):
        return self.__speed

    def __str__(self):
        return 'Your ' + self.year + ' ' + self.__make + 