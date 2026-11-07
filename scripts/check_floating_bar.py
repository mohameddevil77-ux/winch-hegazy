with open(r'D:\winch-hegazy\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Floating Mobile Smart Action Bar')
print('Found floating bar in index.html:', idx != -1)
print(c[idx:idx+600])

with open(r'D:\winch-hegazy\blog\winch-obour-city.html', 'r', encoding='utf-8') as f:
    c_blog = f.read()
print('Found floating bar in blog article:', 'Floating Mobile Smart Action Bar' in c_blog)
