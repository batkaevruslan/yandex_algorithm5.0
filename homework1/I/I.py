def getBestAdnWorstDays(year, yearStartDay, holidays): 
    monthNumberByName = {
        "January":1, 
        "February":2, 
        "March":3, 
        "April":4, 
        "May":5, 
        "June":6, 
        "July":7, 
        "August":8, 
        "September":9, 
        "October":10, 
        "November":11, 
        "December":12
        }
    dayCountByMonth = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    isLeapYear = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    totalDayCount = 366 if isLeapYear else 365
    dayCountByDayOfWeek = {}
    holidaySet = set(map(lambda x: (monthNumberByName[x[0]], x[1]), holidays))
    currentMonth = monthNumberByName["January"]
    currentMonthMaxDays = dayCountByMonth[currentMonth]
    currentMonthDay = 1
    holidayByDayOfWeek = {}
    for day in range(totalDayCount):
        currentDayOfWeek = (yearStartDay + day) % 7
        dayCountByDayOfWeek.setdefault(currentDayOfWeek, 0)
        dayCountByDayOfWeek[currentDayOfWeek] += 1

        if (currentMonth, currentMonthDay) in holidaySet:
            holidayByDayOfWeek.setdefault(currentDayOfWeek, 0)
            holidayByDayOfWeek[currentDayOfWeek] += 1
        
        currentMonthDay += 1
        if currentMonthDay > currentMonthMaxDays and currentMonth != monthNumberByName["December"]:
            currentMonth += 1
            currentMonthDay = 1
            currentMonthMaxDays = dayCountByMonth[currentMonth]
            if isLeapYear and currentMonth == monthNumberByName["February"]:
                currentMonthMaxDays += 1

    bestDay = 1
    maxNonWorkingDays = 0
    worstDay = 1
    minNonWorkingDays = 366
    dayOfWeekNameByNumber = { 0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    for nonWorkingDayOfWeek in dayOfWeekNameByNumber.keys():
        nonWorkingDayCount = dayCountByDayOfWeek[nonWorkingDayOfWeek]
        totalExtraHolidays = 0
        for workingDayOfWeek in dayOfWeekNameByNumber.keys():
            if nonWorkingDayOfWeek != workingDayOfWeek:                
                totalExtraHolidays += holidayByDayOfWeek.setdefault(workingDayOfWeek, 0)
                
        totalNonWorkingDays = nonWorkingDayCount + totalExtraHolidays
        if totalNonWorkingDays > maxNonWorkingDays:
            maxNonWorkingDays = totalNonWorkingDays
            bestDay = nonWorkingDayOfWeek
            
        if minNonWorkingDays > totalNonWorkingDays:
            minNonWorkingDays = totalNonWorkingDays
            worstDay = nonWorkingDayOfWeek
    
    return (dayOfWeekNameByNumber[bestDay], dayOfWeekNameByNumber[worstDay])


def main():
    dayNumberByName = {
        "Monday":0,
        "Tuesday":1,
        "Wednesday":2,
        "Thursday":3,
        "Friday":4,
        "Saturday":5,
        "Sunday":6
    }
    holidayCount = int(input())
    holidays = [None] * holidayCount
    year = int(input())
    for i in range(holidayCount):
        inputs = input().strip().split()
        day = int(inputs[0])
        month = inputs[1]
        holidays[i] = (month, day)
    yearStartDay = dayNumberByName[input().strip()]
    
    answer = getBestAdnWorstDays(year, yearStartDay, holidays)
    print(answer[0], answer[1])

if __name__ == '__main__':
    main()