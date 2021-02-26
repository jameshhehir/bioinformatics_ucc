# Student Name: James Henry Hehir; Student No: 120224791; Module: ST3300 Data Analysis 1;

sampleA = c(19.5,24.1,17.2,12.8,17.9)
sampleB = c(26.5,22.2,24.2,25.3,20.6)
sampleC = c(22.4,23.3,21.7,20.8,28.9)

#Question 3 (b)
eg1=data.frame(sampleA,sampleB,sampleC)
st_eg1<-stack(eg1)
names(st_eg1)<-c("response","sample")
av1<-aov(response~sample, data=st_eg1)
av1
summary(av1)

require(DescTools);
PostHocTest(av1, method = "bonferroni");


#Question 3 (c)(iii)
uniResults <- read.csv(file = 'uni1.csv', header=T)
uniResults
anova2 <-aov(output ~ delivery * type, data =uniResults)
anova2
summary(anova2, conf.level=0.10)

tk_anova2 <-TukeyHSD(anova2)
tk_anova2
