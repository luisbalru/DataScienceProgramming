# Ejercicios de Strings
# Autor: Luis Balderas Ruiz

## EJERCICIO 1: Acrónimo
acron = paste(substr(nombreC[1],1,1),".",nombreC[2],nombreC[3],sep="")

## EJERCICIO 2: Meses impares
fechas = c("01-01-2019","01-02-2019","01-03-2019","01-04-2019","01-05-2019","01-06-2019","01-07-2019")
meses_impares = as.numeric(substr(fechas,4,5)) %% 2 != 0
fechas[meses_impares]

## EJERCICIO 3: Vector de palabras
frase = "Esta es una frase, pero no cualquier frase."
resultado = unlist(strsplit(frase, split=" "))

## EJERCICIO 4: palabras con a y e
frase = "La clase del master es muy interesante y chuli"
lista = intersect(grep("[a]",unlist(strsplit(frase,split=" "))), grep("[e]", unlist(strsplit(frase,split=" "))))

## EJERCICIO 5: dia mes anno
dia = 1:31
mes = 1:12
anno = 2012:2017
dates = paste(dia,"-",mes,"-",anno,sep="")
fechas = as.Date(dates)
