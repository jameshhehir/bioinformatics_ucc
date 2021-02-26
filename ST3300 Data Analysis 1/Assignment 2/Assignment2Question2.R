#Question 2 James Henry Hehir 120224791

data <- read.csv("shares.csv")
data

datats=ts(data)
#Part (A)
plot(datats, ylab="Shares")

#Part (B)
pacf(datats)
#Part (C)
model_ar3=arima(datats,order=c(3,0,0))
model_ar3
model_ma1=arima(datats,order=c(0,0,1))
model_ma1
#Part(D)
predict(model_ar3,2)
predict(model_ma1,2)
#Part(E)
resid1=residuals(model_ar3)
resid2=residuals(model_ma1)
plot(resid1)
plot(resid2)
hist(resid1)
hist(resid2)
acf(resid1)
acf(resid2)
