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
