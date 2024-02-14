def ordena_burbuja(lista_desordenada:list):
    for i in range(len(lista_desordenada)-1,0,-1):
        for j in range(0,i):
            if lista_desordenada[j] > lista_desordenada[j+1]:
                lista_desordenada[j],lista_desordenada[j+1]  = lista_desordenada[j+1],lista_desordenada[j]