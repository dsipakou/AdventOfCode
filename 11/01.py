from collections import Counter
s = input().split(',')

c = Counter(s)
print(c)
min1 = min(c['s'], c['n'])
c['s'] -= min1
c['n'] -= min1
min2 = min(c['nw'], c['se'])
c['nw'] -= min2
c['se'] -= min2
min3 = min(c['sw'], c['ne'])
c['sw'] -= min3
c['ne'] -= min3
print(c)
min4 = min(c['s'], c['ne'])
c['se'] += min4
c['s'] -= min4
c['ne'] -= min4
print(sum(c.values()))