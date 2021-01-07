library(ggplot2)
library(dplyr)
library(plyr)
library(tidyr)

d <- read.csv(file="../model/mushrooms_v2.csv", header=TRUE, sep=",")
ggplot(data.frame(animals), aes(x=animals)) +
  geom_bar()

d %>%
  gather() %>% 
  ggplot(aes(value)) +
  facet_wrap(~ key, scales = "free") +
  geom_bar()

#number of columns
nc <- 2
level.byrow <- function(vec, nc){
  fac <- factor(vec) #if it is not a factor
  mlev <- matrix(levels(fac), nrow=nc, byrow=T)
  factor(fac, levels= c(mlev))
}

library(randomForest)
fit_rf = randomForest(class~., data=d)
# Create an importance based on mean decreasing gini
varImpPlot(fit_rf)
imp[order(MeanDecreaseGini),]
imp

hist <- ggplot( d, aes( x = odor, fill = class )) 
hist <- hist + geom_bar(stat='count', position='dodge') + labs(x = 'Odor', y = 'Count of Class')
hist
