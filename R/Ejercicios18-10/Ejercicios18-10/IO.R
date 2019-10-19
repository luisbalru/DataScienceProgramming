# Ejercicios de Input/Output
# Autor: Luis Balderas Ruiz

## EJERCICIO 1
n = scan("")
s = scan("",what = character())
cadena = rep(s,n)

## EJERCICIO 2
# Tabla del 2
write.table(matrix(seq(from=2,to=20,by=2),nrow=10),"dos.txt",row.names = FALSE, col.names = FALSE)
# Tabla del 3
write.table(matrix(seq(from=3,to=30,by=2),nrow=10),"tres.txt",row.names = FALSE, col.names = FALSE)
# Tabla del 5
write.table(matrix(seq(from=5,to=50,by=2),nrow=10),"cinco.txt",row.names = FALSE, col.names = FALSE)

## EJERCICIO 3
M = cbind(read.table("Ejercicios-20191018/dos.txt",header=F),read.table("Ejercicios-20191018/tres.txt",header=F),read.table("Ejercicios-20191018/cinco.txt",header=F))

## EJERCICIO 4
write.table(M[1:5,],file="inicio.txt",sep=",",row.names = F,col.names=F)
write.table(M[-5:0,],file="fin.txt",sep=",",row.names = F,col.names=F)

## EJERCICIO 5
