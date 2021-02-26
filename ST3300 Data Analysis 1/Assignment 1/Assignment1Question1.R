# Student Name: James Henry Hehir; Student No: 120224791; Module: ST3300 Data Analysis 1;

sample1 = c(7.2,5.6,6.8,6.7,6.2,5.1,6.9,8.1,7.2,6.7,6.1,6.8)
sample2 = c(1.1,3.2,19.4,1.5,16.4,8,11.5,1.2,2.7,25.5,50.1,2.2)
sample3 = c(18.2,14.2,19.1,4.3,15.1,12.2,15.3,-5.4,16.2,15.5,9.1,-2.1)

#This is question 1 (a)
mean(sample1)
mean(sample2)
mean(sample3)
median(sample1)
median(sample2)
median(sample3)
var(sample1)
var(sample2)
var(sample3)
sd(sample1)
sd(sample2)
sd(sample3)
IQR(sample1)
IQR(sample2)
IQR(sample3)

#This question 1 (b)
#Graphical 
qqnorm(sample1)
qqline(sample1)
qqnorm(sample2)
qqline(sample2)
qqnorm(sample3)
qqline(sample3)
#Numerical 
shapiro.test(sample1)
shapiro.test(sample2)
shapiro.test(sample3)

#Question 1 (c)
t.test(sample2, mu = 5, alternative = "greater", conf.level=0.90)

#Question 1 (d)
t.test(sample1, sample2, paired=F)

#Question 1 (e)
t.test(sample2, sample3, conf.level=0.10, paired=T)

