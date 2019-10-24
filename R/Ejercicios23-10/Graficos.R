# Ejercicios de Gráficos
# Autor: Luis Balderas Ruiz

# EJERCICIO 1
boxplot(iris$Sepal.Length,iris$Sepal.Width,iris$Petal.Length,iris$Petal.Width,names=c("Sepal Length","Sepal Width", "Petal Length", "Petal Width"), ylab = "cm")

# EJERCICIO 2
M = matrix(runif(800),nrow=200,ncol=4)

# EJERCICIO 3
library(MASS); 
str(quine); 
t=xtabs(~ Age,data=quine);
p=prop.table(xtabs(~ Age,data=quine))
union = cbind(t,p)
barplot(union, beside=T)

# EJERCICIO 4
pie(p,col=rainbow(length(t)),clockwise = TRUE, main="Edad por sectores")
dotchart(t,main="Puntos para las edades")

# EJERCICIO 5
m = lm(dist~speed, data=cars)
plot(cars$speed,cars$dist, main="Gráfica velocidad/distancia", xlab="Velocidad", ylab = "Distancia")
abline(m,col="red")