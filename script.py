# listar numeros primos

# listar os numeros primos de 1 a 250

# estrutura de repetiçao


    # verificar se o numero e primo
    # numero primo sao aqueles que apresenta dois divisores
    # um e o propio numero
    # print(i)

    # verificar se e divisivel
    # condicilnal

 


start = 1
end = 250
  
for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 

