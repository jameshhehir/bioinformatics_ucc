# Student Name: James Henry Hehir; Student No: 120224791; Module: ST3300 Data Analysis 1;

sampleA=c(40,42,36,41,56,41,48,50,40,43)
sampleB=c(35,33,38,35,49,46,46,41,38,37)

#Question 2 (a)
wilcox.test(sampleA, mu=42, correct=F)
wilcox.test(sampleA, mu = 42, conf.level=0.10,correct=F)

#Question 2 (b)
wilcox.test(sampleA,sampleB, correct = F)

#Question 2 (c)
wilcox.test(sampleA,sampleB, m=0, conf.level=0.95, correct=F,paired = T)
