try:
    f_l = open ("operacions.txt","r", encoding='utf-8') 
    f_es = open ("resultats.txt","w", encoding='utf-8')

    operacions=[]
    suma = lambda x, y: print(x+y)
    resta = lambda x, y: print(x-y)
    multiplicacio = lambda x, y: print(x*y)
    divisio = lambda x, y: print(x+y)
    res = 0
    linies=f_l.readlines()
    for linia in linies:
        operacions.append(linia)
        operacions.split(" ")
        try:
            operacions[1] = {
        
                "+" : f_es.write(operacions[0]+operacions[1]+operacions[2] +" = "+ suma(operacions[0],operacions[2])),
                "-" : f_es.write(operacions[0]+operacions[1]+operacions[2] +" = "+ resta(operacions[0],operacions[2])),
                "*" : f_es.write(operacions[0]+operacions[1]+operacions[2] +" = "+ multiplicacio(operacions[0],operacions[2])),
                "/" : f_es.write(operacions[0]+operacions[1]+operacions[2] +" = "+ divisio(operacions[0],operacions[2]))
      
        }
        except(IOError):
            print("Error operacio no definida") 
except(IOError,NameError):
    print("Error obrint el fitcher")
        
    