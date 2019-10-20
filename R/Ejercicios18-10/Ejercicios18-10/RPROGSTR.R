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
for (i in 1:5){
  lista[i] = list(unlist(lista[i])[order(unlist(lista[i]))])
}
## EJERCICIO 4. No entiendo el enunciado



## EJERCICIO 5

A = matrix(runif(20,1,14),nrow=5,ncol=4)
l = list(A[A >7])
