class SimpleDate:
    __day = 1
    __mounth = 1
    __year = 2000
    __daysInMounth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    __isLeapYear = False
    
    def __init__(self, d, m, y):
        self.__year = y
        self.__calcLeap()
        if m > 0 and m < 13:
            self.__mounth = m
        if d > 0 and d <= self.__daysInMounth[m-1]:
            self.__day = d
        
    def __add__(self, other):
        new_d = SimpleDate(self.__day, self.__mounth, self.__year)
        new_d.addDays(other)
        return new_d

    def __lt__(self, other):
        if self.__year < other.__year:
            return True
        elif self.__year > other.__year:
            return False
        elif self.__mounth < other.__mounth:
            return True
        elif self.__mounth > other.__mounth:
            return False
        elif self.__day < other.__day:
            return True
        else:
            return False

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        if self.__day == other.__day and \
           self.__mounth == other.__mounth and \
           self.__year == other.__year:
               return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __qt__(self, other):
        return other < self

    def __ge__(self, other):
        return other < self or other == self
    
    def __str__(self):
        return '{:0=2}-{:0=2}-{:0=4}'.format(self.__day, self.__mounth, self.__year)

    def isLeap(self):
        return self.__isLeapYear

    def __calcLeap(self):
        if not(self.__year % 4):
            if not(self.__year%100) and self.__year%400:
                self.__isLeapYear = False
                self.__daysInMounth[1]=28
            else:
                self.__isLeapYear = True
                self.__daysInMounth[1]=29
        else:
            self.__isLeapYear = False
            self.__daysInMounth[1]=28
        
    def addDays(self, value):
        while self.__day + value > self.__daysInMounth[self.__mounth-1]:
            value = value - self.__daysInMounth[self.__mounth-1]
            self.addMounth(1)
        self.__day = self.__day + value
     
    def addMounth(self, value):
        while self.__mounth + value > 12:
            value = value - 12
            self.addYear(1)
        self.__mounth = self.__mounth + value
     
    def addYear(self, value):
        self.__year = self.__year + value
        self.__calcLeap()

