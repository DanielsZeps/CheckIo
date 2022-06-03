def sum_light(els: List[datetime], start_watching: Optional[datetime] = None):
    compValues = {
        "day": 0,
        "hour": 0,
        "minute": 0,
        "second": 0
    }
    try:
        time0 = round(start_watching.day * 24 * 60 * 60 + start_watching.hour * 60 * 60
            + start_watching.minute * 60 + start_watching.second)
    except:
        time0 = 0
    for x in range(0, len(els), 2):
        time1 = round(els[x].day * 24 * 60 * 60 + els[x].hour * 60 * 60 + els[x].minute * 60 + els[x].second)
        time2 = round(els[x+1].day * 24 * 60 * 60 + els[x+1].hour * 60 * 60 + els[x+1].minute * 60 + els[x+1].second)
        if time1 > time0:
            compValues["day"] += els[x+1].day - els[x].day
            compValues["hour"] += els[x+1].hour - els[x].hour
            compValues["minute"] += els[x+1].minute - els[x].minute
            compValues["second"] += els[x+1].second - els[x].second
        elif time2 > time0:
            compValues["day"] += els[x+1].day - start_watching.day
            compValues["hour"] += els[x+1].hour - start_watching.hour
            compValues["minute"] += els[x+1].minute - start_watching.minute
            compValues["second"] += els[x+1].second - start_watching.second
    x = round(compValues["day"] * 24 * 60 * 60 + compValues["hour"] * 60 * 60 +
        compValues["minute"] * 60 + compValues["second"])
    return x
