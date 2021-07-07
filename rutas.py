def contar_rutas_mas_cortas(C):
    r = len(C)
    c = len(C[0])

    if C[0][0] == 1:
        return 0

    
    for i in range(r):
        C[i][0] = 1
    
    
    for j in range(c):
        C[0][j] = 1
    

    for i in range(1, r):
        for j in range(1, c):

            if C[i][j] == 1:
                C[i][j] = 0
            
            else:
                C[i][j] = C[i-1][j]+C[i][j-1]
    
    return C[r-1][c-1]
