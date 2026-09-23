#1360
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1_split=date1.split("-")
        date2_split=date2.split("-")
        result=0
        #year
        result=(int(date2_split[0])-int(date1_split[0]))*365+(int(date2_split[0])-int(date1_split[0]))
        #🔥怎么高效处理每个月天数不一致的情况呢

#参考答案：计算每一个日期距离基准日（如 1970-01-01）的总天数
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeap(year: int) -> bool:
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)#判断是否是闰年的逻辑

        def daysFrom1970(date_str: str) -> int:#计算date1和date2分别距离基准日的天数
            y, m, d = map(int, date_str.split('-'))
            
            # 每个平月的天数前缀和/查找表
            days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            
            total_days = 0
            
            # 1. 累加 1970 年到 y-1 年的天数
            for year in range(1970, y):
                total_days += 366 if isLeap(year) else 365
                
            # 2. 累加当年 1 月到 m-1 月的天数
            for month in range(1, m):
                total_days += days_in_months[month]
                # 遇上闰年且超过 2 月，多加 1 天
                if month == 2 and isLeap(y):
                    total_days += 1
                    
            # 3. 加上当月的天数
            total_days += d
            
            return total_days

        return abs(daysFrom1970(date1) - daysFrom1970(date2))
        
#optiver变体:要注意输入的两个日期没有范围限制，可以是任何日期
class Solution:
    def DaysInMonth(self,year,month):#[provided]
        return 30 #placeholder
    
    def isLeap(year):
        if int(year)%4==0 and int(year)%100!=0 or int(year)%400==0:
            return True
        else:
            return False
        
    def DaysBetween(self,year1,month1,day1,year2,month2,day2):
        delta=0
        for i in range(int(year1),int(year2)):
            if self.isLeap(i):
                delta+=366
            else:
                delta+=365 #🔥(1970-12-1, 1971-12-1),(1970-11-1,1971-12-1),(1970-12-1,1971-11-1)三个case这里条件判断无论怎么改总有跑不通的

#参考答案：永远都是找基准日，无论有没有范围
class Solution:
    # 题目提供的函数（直接通过 self.DaysInMonth(month, year) 调用）
    # 注意：根据题目描述，参数顺序是 (month, year)
    def DaysInMonth(self, month: int, year: int) -> int:
        # placeholder for environment
        pass

    def dateToDays(self, year: int, month: int, day: int) -> int:#无需分BC AD
        y = year - 1#公元1年做基准，注意没有公元0年
        
        # 1. 前 y 年的绝对天数 (O(1) 数学公式)
        # 平年 365 天 + 闰年增加的 1 天
        # 使用 Python 整除 //，天然支持无限大的年份（甚至包含负数年份）
        leap_years = (y // 4) - (y // 100) + (y // 400)
        total_days = y * 365 + leap_years
        
        # 2. 累加当年前 m - 1 个月的天数
        # 严格使用题目提供的 self.DaysInMonth(m, year)
        for m in range(1, month):
            total_days += self.DaysInMonth(m, year)
            
        # 3. 加上当月天数
        total_days += day
        
        return total_days

    def DaysBetween(self, year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
        days1 = self.dateToDays(year1, month1, day1)
        days2 = self.dateToDays(year2, month2, day2)
        
        return days2 - days1