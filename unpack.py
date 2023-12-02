# spread args into the function an stay verbose instead of
# defining ...args like in JavaScript
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts;

coins = {"galleons": 100, "sickles": 50, "knuts": 25};

# similar to spreading args in JavaScript
print(total(**coins), "Knuts")