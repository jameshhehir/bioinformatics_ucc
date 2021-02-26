#Question 3 James Henry Hehir 120224791

data <- read.csv("shares.csv")
data

datats=ts(data, frequency = 12)

#Part (B)
ts1 <- HoltWinters(datats, gamma = TRUE, beta = FALSE)
ts1
plot(ts1)

#Part (C)
ts1predict2 <- predict(ts1,2,prediction.interval=TRUE)
ts1predict2

#Part (D)
set.seed(seed = 100)
m1<-arima.sim(n=500,list(ar=c(0.7,0,0.1)),sd=1)
plot(m1)

