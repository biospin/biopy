

## Slide with R Code and Output


getwd()
setwd("~/Documents/Dropbox/biopythonstudy/part2/part2ch13")


## Slide with R Code and Output


10^2 + 36
a <- 4 ; a
a*5
a = a+10; a


## Data structures

- vector 
- matrix
- dataframe
- list

## Vectors


vec1 = c(1,4,6,8,10) ; vec1
vec1[5] 
vec1[3]
vec1[3]=12 ; vec1

## Vectors


vec2 = 1:10
vec2[1]
vec2[-1]
sum(vec2)


## Matrices

mat = matrix(data = c(9,2,3,4,5,6), ncol=3); mat
mat[1,2]; mat[2,]
mean(mat)


## Dataframes

t = data.frame(x=c(11,12,14), y=c(19,20,21), z = c(10,9,7));  t
mean(t$z)
mean(t[["z"]])


## Lists

L = list(one=1, two = c(1,2), five = seq(0,1,length=5)); L
names(L);  L$five + 10


## Graphics

plot(rnorm(100), type="l", col="gold")


## Graphics - histogram

hist(rnorm(100))



## Reading and writing data files


d = data.frame(a= c(3,4,5), b = c(12,43,54))
d
write.table(d, file="tst0.txt", row.names=FALSE)
d2 = read.table(file="tst0.txt", header=TRUE)
d2


## not available data


j = c(1,2,NA)
max(j)
max(j, na.rm=TRUE)


## Classes - Characters

m = "apples"
m


## If-statements

w=3
if(w<5)
{
  d=2
}else{
  d=10  
}
d


## For-loop

h = seq(from=1, to=8)
s = c()
for(i in 2:10)
{
  s[i] = h[i] * 10
}
s

## writing your own functions

fun1 = function(arg1, arg2)
{
  w = arg1 ^2
  return(arg2 + w)
}
fun1(arg1 = 3, arg2 = 5)



## install packages

- CRAN 
- devtools : github
- bioconductor (http://www.bioconductor.org)
- > source("http://bioconductor.org/biocLite.R")
- > biocLite("affy")

## CRAN
- install.packages("ggplot2")

## devtools
- install.packages("devtools")
- Windows: Install Rtools.
- Mac: Install Xcode from the Mac App Store.
- Linux: Install a compiler and various development libraries 

## devtools
- Mac and Linux:
  - devtools::install_github("hadley/devtools")

- Windows:
  - library(devtools)
- build_github_devtools()

## example : rCharts
- http://ramnathv.github.io/rCharts/
  - require(devtools)
- install_github('rCharts', 'ramnathv')

## bioconductor
- bioconductor (http://www.bioconductor.org)
- source("http://bioconductor.org/biocLite.R")
- biocLite("affy")




## ggplot2


# ggplot2 examples
library(ggplot2) 

# create factors with value labels 
mtcars$gear <- factor(mtcars$gear,levels=c(3,4,5),
                      labels=c("3gears","4gears","5gears")) 
mtcars$am <- factor(mtcars$am,levels=c(0,1),
                    labels=c("Automatic","Manual")) 
mtcars$cyl <- factor(mtcars$cyl,levels=c(4,6,8),
                     labels=c("4cyl","6cyl","8cyl")) 


## ggplot2


# Kernel density plots for mpg
qplot(mpg, data=mtcars, geom="density", fill=gear, alpha=I(.5), 
      main="Distribution of Gas Milage", xlab="Miles Per Gallon", 
      ylab="Density")


## ggplot2

p <- qplot(hp, mpg, data=mtcars, shape=am, color=am, 
           facets=gear~cyl, main="Scatterplots of MPG vs. Horsepower",
           xlab="Horsepower", ylab="Miles per Gallon")
p + theme_bw()
p + theme(axis.title=element_text(face="bold.italic", 
                                  size="12", color="brown"), legend.position="top")




