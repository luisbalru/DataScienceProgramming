# Ejercicios Día 2 Matrices
# Luis Balderas Ruiz

# MATRICES

#*

new_hope = c(460.998007, 314.4)
empire_strikes = c(290.475067, 247.9)
return_jedi = c(309.306177, 165.8)
# a) Creo la matriz por filas
star_wars_matrix = rbind(new_hope,empire_strikes,return_jedi)
# b) 
colnames(star_wars_matrix) <- c("Millones EEUU", "Millones Resto Mundo")
rowname(star_wars_matrix) <- c("New Hope", "Empire Strikes", "Return Jedi")
# c)
worldwide_vector = c(sum(star_wars_matrix[1,]),sum(star_wars_matrix[2,]),sum(star_wars_matrix[3,]))
# d)
all_wars_matrix = cbind(star_wars_matrix,worldwide_vector)
colnames(all_wars_matrix) <- c("Millones EEUU", "Millones Resto Mundo", "Total")
# e)
colSums(star_wars_matrix)
# f)
non_us_all = mean(sum(star_wars_matrix[,2]))
# g)
non_us_some = mean(sum(star_wars_matrix[1:2,2]))
# h)
visitantes = star_wars_matrix*1000000/5
colnames(visitates) <- c("Nº espectadores EEUU", "Nº espectadores resto del mundo")

# SUBSETTING ARRAYS
#*
i <- array(c(1:5,5:1),dim=c(3,2))
dim(i) # Dimensión de la matriz (3x2)
nrow(i) # Número de filas
ncol(i) # Número de columnas
#*
archivo = read.table("Datos/array_datos.txt")
#*
write.table(archivo,sep="\t", "Datos/array_datos.csv")