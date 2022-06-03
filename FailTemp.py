def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None):
    #compValues = {
    #    "day": 0,
    #    "hour": 0,
    #    "minute": 0,
    #    "second": 0
    #}
    compValues = 0
    try:
        time0 = round(start_watching.day * 24 * 60 * 60 + start_watching.hour * 60 * 60
            + start_watching.minute * 60 + start_watching.second)
    except:
        time0 = 0
    try:
        time3 = round(end_watching.day * 24 * 60 * 60 + end_watching.hour * 60 * 60
            + end_watching.minute * 60 + end_watching.second)
    except:
        time3 = 0
    for x in range(0, len(els), 2):
        time1 = els[x]
        time2 = els[x+1]
        time1 = time1.day * 24 * 60 * 60 + time1.hour * 60 * 60 + time1.minute * 60 + time1.second
        time2 = time2.day * 24 * 60 * 60 + time2.hour * 60 * 60 + time2.minute * 60 + time2.second
        if not (time2 < time0 or not time0 == 0) or (time1 > time3 or not time3 == 0):
            print("c")
            if time1 <= time0 and time3 <= time2:
                print("a", 1)
                compValues += time3 - time0
                print("b", compValues)
            elif time1 <= time0 and time2 >= time0:
                print("a", 2)
                compValues += time2 - time0
                print("b", compValues)
            elif time1 >= time0 and time3 <= time2 and time1 < time3:
                print("a", 3)
                compValues += time3 - time1
                print("b", compValues)
            elif time1 > time0 and time3 > time2:
                print("a", 4)
                compValues += time2 - time1
                print("b", compValues)
    print(compValues)
    return compValues
