def mmc(a,b):
    mmc = a
    while mmc % b:
        mmc += a
    return mmc
print(mmc(456578451202, 4561231))