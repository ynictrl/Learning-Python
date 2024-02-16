a = 'AAA'
b = 'BBB'
c = 3.3

string = 'b={1} a={0} c={nome3:.2f}'
formato = string.format(a, b, nome3=c) #nome é parametro

print(formato)