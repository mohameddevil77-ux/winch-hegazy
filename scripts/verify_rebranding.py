with open(r'D:\winch-hegazy\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

print('Has أوناش إنقاذ أولاد حجازي:', 'أوناش إنقاذ أولاد حجازي' in c)
print('Has أولاد حجازي:', 'أولاد حجازي' in c)
print('Has Awlad Hegazy:', 'Awlad Hegazy' in c)
print('Has awladhegazy.com:', 'awladhegazy.com' in c)
print('Title:', c[c.find('<title>')+7:c.find('</title>')])
print('H1:', c[c.find('<h1'):c.find('</h1>')+5])
