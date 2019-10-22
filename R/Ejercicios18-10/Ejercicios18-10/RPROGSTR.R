# Ejercicios R Programming Structures
# Autor: Luis Balderas Ruiz

## EJERCICIO 1
creciente = function(v){
  crec = v[1] <= v[2]
  i = 3
  l = length(v)
  while(crec & (i+1)<l){
    crec = v[i] <= v[i+1]
    i = i+1
  }
  return(crec)
}
creciente(1:10)
creciente(10:1)

## EJERCICIO 2
montecarlo = function(N){
  hits = 0
  for(i in c(1:N)){
    r = runif(2,0,1)
    if(r[2]<r[1]^2)
      hits = hits + 1
  }
  return(hits/N)
}
montecarlo(10)
montecarlo(10000)
montecarlo(10000000)

## EJERCICIO 3

lista = list(runif(10,1,10),runif(10,5,9),runif(10,7,96),runif(10,4,10),runif(10,5,9))
posiciones = lapply(lista,order)
for (i in 1:5){
  lista[i] = list(unlist(lista[i])[unlist(posiciones[i])])
}
## EJERCICIO 4. 

M = matrix(sample(1:100,20,replace=T),nrow=5,ncol=4)
if(M[1,1]%%2==0){
  mini=M[1,1]
}else{
  mini=-M[1,1]
}
v = 1:ncol(M)
for (i in 1:ncol(M)){
  for(j in 1:nrow(M)){
    if(M[j,i]%%2==0){
      if(M[j,i]<mini){
        mini=M[j,i]
      }
    }
    else{
      if(-M[j,i]<mini){
        mini=-M[j,i]
      }
    }
  }
  v[i] = mini
  mini = 200 # Los valores de la matriz van de 1 a 100, luego está fuera del rango
}  
v = -v
print(v)
## EJERCICIO 5

A = matrix(runif(20,1,14),nrow=5,ncol=4)
l = list(A[A >7])
