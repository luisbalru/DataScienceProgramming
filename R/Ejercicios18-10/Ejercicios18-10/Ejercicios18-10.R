# Ejercicios 17-10-2019
# Luis Balderas Ruiz

# FACTORES

#*
x <- c(1,2,3,3,5,3,2,4,NA)
factor(x)
# a) 1,2,3,4,5

#*
x <- c(11,22,47,47,11, 47, 11)
factor(x, levels=c(11, 22, 47), ordered=TRUE)
# c) 47

#*
z <- c("p", "a" , "g", "t", "b")
z[3] <- "b"
# c) z[3] <- "b"

#*
z <- factor(c("p", "q", "p", "r", "q")) 
levels(z)[levels(z) == "p"] <- "w"

#*
# 5 niveles
iris$Sepal.Length=factor(cut(iris$Sepal.Length,5))
table(iris$Petal.Length<5,iris$Species)

#*
responses <- factor(c("Agree", "Agree", "Strongly Agree","Disagree", "Agree"))
responses <- factor(responses, levels=c("Strongly Agree","Agree", "Disagree", "Strongly Disagree"),ordered=TRUE)

#*
x <- c("high","low","medium","high","high","low","medium")
x <- factor(x,levels=unique(x),labels=c(1,2,3))
