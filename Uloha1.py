def uloha_1_podla_seba (n,slovo:str)->str:
    a=len(slovo)
    if a < n:
        print('zly index')
    else:
        print(slovo[n-1])
    return ''
print(uloha_1_podla_seba(6,'kamikadze'))
print(uloha_1_podla_seba(3,'kuk'))
print(uloha_1_podla_seba(1,' '))
print(uloha_1_podla_seba(1,''))

def uloha_1_jak_ma_byc (n,slovo:str)->str:
    a=len(slovo)
    if a <= n:
        print('zly index')
    else:
        print(slovo[n])
    return ''
print(uloha_1_jak_ma_byc(6,'kamikadze'))
print(uloha_1_jak_ma_byc(3,'kuk'))
print(uloha_1_jak_ma_byc(0,' '))
print(uloha_1_jak_ma_byc(0,''))
