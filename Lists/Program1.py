## The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
# They would like your help with an application form that will tell prospective members which category they will be placed.
# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

def open_or_senior(data):
    return ["Senior" if m[0]>54 and m[1]>7 else "Open" for m in data]



