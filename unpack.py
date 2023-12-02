# spread args into the function an stay verbose instead of
# defining ...args like in JavaScript
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts;

const = [100, 50, 25];

# similar to spreading args in JavaScript
print(total(*const), "Knuts")