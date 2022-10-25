def uloha_2(veticka:str)->str:

    p=0
    cisla='1,2,3,4,5,6,7,8,9,0'

    for i in range(0,len(veticka)):
        a=veticka[i]
        if  a in cisla:
            p+=1
    return p
print(uloha_2('Hladam 3 mesacneho kocura na 5tej ulici 4 roh z 6teho poschodia na 18 stupni.'))
