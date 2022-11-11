x<-c(1,12,18,22,8,9,18,17,16,5,3)
y<-c(10,20,13,12,4,2,9,10,12,17,20)
plot(x,y,main="Cars", xlab="speed", ylab="distance", col="red")

x2<-c(10,11,9,2,7,6,8,14,11,2,1)
y2<-c(1,2,3,2,9,5,3,6,17,11,19)
points(x2,y2,col="blue")

# scatter plot
plot(x,y,main="Cars", xlab="speed", ylab="distance", col="red")

# line chart
plot(x, type="o")

# bar graph
barplot(x, xlab = "X-axis", ylab = "Y-axis", main ="Bar-Chart", horiz=TRUE)

# histogram
hist(x, xlab = "X-axis", ylab = "Y-axis", main ="histogram")

# pie chart
geeks<- c(23, 56, 20, 63)
labels <- c("Mumbai", "Pune", "Chennai", "Bangalore")
pie(geeks, labels)
