spam = input()
lgth = len(spam)
print(len([_ for _ in spam if _ == '_'])/lgth)
print(len([a for a in spam if a.islower()])/lgth)
print(len([A for A in spam if A.isupper()])/lgth)
print(len([c for c in spam if not(c == '_' or c.isalpha())])/lgth)
