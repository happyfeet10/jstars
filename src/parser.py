def parse_unit(unit):
    keys = ["time", "index", "name", "lat", "lon", "alt", "heading", "coalition", "unitname", "groupname"]
    unitMap={}
    if len(unit) == len(keys):
        for i,k in keys:
            unitMap[k]=unit[i]
        return unitMap
    else:
        return None