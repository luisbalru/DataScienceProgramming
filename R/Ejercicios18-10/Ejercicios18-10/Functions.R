# Ejercicios de Funciones
# Autor: Luis Balderas Ruiz

## EJERCICIO 1
impares = function(v){
  pos = v%%2 != 0
  return(length(v[pos]))
}
impares(1:10)

## EJERCICIO 2
cambio = function(M){
  pos = is.na(M)
  M[pos] = 0
  return(M)
}
M = c(1,2,NA)
print(cambio(M))

## EJERCICIO 3
unir = function(u,v){
  return(union(unique(u),unique(v)))
}
unir(c(1,1,2,3),c(2,3,5,5,7))

## EJERCICIO 4
vyc = function(cadena){
  
}

## EJERCICIO 5
partir = function(v,x,y){
  pos_x = match(x,v)
  pos_y = match(y,v)
  ifelse(is.na(pos_y) == F, return(v[pos_x:pos_y]),return(v[(-pos_x+1):0]))
}

v = 1:10
partir(v,2,7)
partir(v,8,15)