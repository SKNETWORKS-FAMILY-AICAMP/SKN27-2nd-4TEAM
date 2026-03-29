

def fill_tenure(group, overall_median):
    if len(group) < 5:
        return group.fillna(overall_median)  
    return group.fillna(group.median())      


def fill_day(group, overall_median):
    if len(group) < 5:
        return group.fillna(overall_median)
    return group.fillna(group.median())


def fill_order_count(group, overall_median):
    if len(group) < 5:
        return group.fillna(overall_median)
    return group.fillna(group.median())

def fill_hike(group, overall_median_hike):
    if len(group) < 5:
        return group.fillna(overall_median_hike)
    return group.fillna(group.median())