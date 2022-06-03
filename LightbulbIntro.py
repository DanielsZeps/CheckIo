from datetime import datetime
from typing import List

def sum_light(els: List[datetime]):
    compValues = {
        "day": 0,
        "hour": 0,
        "minute": 0,
        "second": 0
    }
    for x in range(0, len(els), 2):
        compValues["day"] += els[x+1].day - els[x].day
        compValues["hour"] += els[x+1].hour - els[x].hour
        compValues["minute"] += els[x+1].minute - els[x].minute
        compValues["second"] += els[x+1].second - els[x].second
    x = round(compValues["day"] * 24 * 60 * 60 + compValues["hour"] * 60 * 60 +
        compValues["minute"] * 60 + compValues["second"])
    return x
