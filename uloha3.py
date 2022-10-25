def uloha_3(veticka:str)->str:

    saumohlausky='a,á,ä,e,é,i,í,y,ý,o,ó,u,ú, '
    p=0
    v=True
    for i in range(0,len(veticka)):
        a=veticka[i]
        if  a in saumohlausky:
            p+=1
    if p!=len(veticka):
            v=False

    return v
print(uloha_3('aa io'))
