int = -10 # base 10
div = int if int >= 0 else -int # modulo de int
bin = [] # lista de binario
bin_value = '' # bin final

# 4 / 2 = 2 (%=0) | 2 / 2 = 1 (%=0) 1 / 2 = .5 (%=1)
# dividendo = div
# divisor = 2

# conversão
while div >= 1:
    bin.append(str(div % 2))

    div_succ = div // 2
    div = div_succ

# sinal
if int >= 0:
    bin.append('0')
else:
    bin.append('1')

# inverter a lista
bin.reverse()

# adcionar a bin_value
for i in bin:
    bin_value += i  

print(bin_value)