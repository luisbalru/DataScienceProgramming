# Ejercicios de Gráficos
# Autor: Luis Balderas Ruiz

# EJERCICIO 1
boxplot(iris$Sepal.Length,iris$Sepal.Width,iris$Petal.Length,iris$Petal.Width,names=c("Sepal Length","Sepal Width", "Petal Length", "Petal Width"), ylab = "cm")

# EJERCICIO 2
M = matrix(runif(800),nrow=200,ncol=4)
plot(1:200,M[,1],type="l",col="blue",main="Tasa de acierto clasificación", xlab = "Experimento",ylab="Accuracy",ylim=c(0,1.2))
lines(1:200,M[,2],col="red")
lines(1:200,M[,3],col="green")
lines(1:200,M[,4],col="black")
legend(0,1.27,legend=c("Alg. 1", "Alg. 2","Alg. 3", "Alg. 4"),col=c("blue","red","green","black"),lty=1, cex=0.8)

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