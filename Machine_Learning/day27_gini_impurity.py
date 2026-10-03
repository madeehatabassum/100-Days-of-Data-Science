# Day 27: Gini Impurity
# ---------------------
def gini(p):
    return 1 - sum([pi**2 for pi in p])
if __name__ == '__main__': print(gini([0.5, 0.5]))
