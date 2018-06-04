new = {'a':'@', 'b':'8', 'c':'(', 'd':'|)', 'e':'3', 'f':'#', 'g':'6',
'h':'[-]', 'i':'|', 'j':'_|', 'k':'|<', 'l':'1', 'm':'[]\/[]', 'n':'[]\[]',
'o':'0', 'p':'|D', 'q':'(,)', 'r':'|z', 's':'$', 't':"']['", 'u':'|_|',
'v':'\/', 'w':'\/\/', 'x':'}{', 'y':'`/', 'z':'2'}

inp = input().lower()
translation = ''
for char in inp:
    if char in new:
        translation += new[char]
    else:
        translation += char
print(translation)
