r <- 1000
c <- 50
randomLetters <- matrix(data = NA, nrow = r, ncol = c)

new.rownames<-NULL
for (i in 1:r) {
  randomLetters[i,] <- sample(LETTERS, c, TRUE)
  new.rownames[i]<-paste("row_",i,sep="")
}

rownames(randomLetters)<-new.rownames
colnames(randomLetters) <- paste("col_", 1:50, sep = "")


#B
lowerRandomLetters <- tolower(randomLetters)
lowerRandomLettersHi <- sub("h","hi",lowerRandomLetters)
columnsCount <- colCounts(lowerRandomLettersHi, rows = NULL, cols = NULL, value = "hi", na.rm = FALSE, dim. = dim(lowerRandomLettersHi))
totalCount<- length(grep("hi", lowerRandomLettersHi))
extractHi <- grep("hi", lowerRandomLettersHi, value = TRUE)
updated_num <- paste0("_", 1:2003, sep="")
paste(extractHi,updated_num, sep = "")


#C
c <- 20
randomVector <- list()
for (i in 1:c) {
  randomVector[[i]]<- sample(1:100, 50, TRUE)
}
mean1 <- sapply(randomVector, mean)
updated_mean <- paste0("mean_", mean1, sep="")
names(randomVector)<-updated_mean 

Matrix_x <- matrix(unlist(randomVector), ncol = 50, byrow = TRUE) #convert list to matrix
rownames(Matrix_x)<-updated_mean #give rows names
summary(Matrix_x) # summary

#D
vector = 0
i=0
while (i < 10000) {
  if (i %% 2 ==1)
    {vector <- c(vector, i)}
  i= i+1
}
vector <- vector[-1]
match(c(9855), vector)

new_vector <- gsub("9", "8", vector)




lowerRandomLetters <- tolower(randomLetters)
lowerRandomLettersHi <- sub("h","hi",lowerRandomLetters)
columnsCount <- colCounts(lowerRandomLettersHi, value = "hi", dim. = dim(lowerRandomLettersHi))
totalCount<- length(grep("hi", lowerRandomLettersHi))
extractHi <- grep("hi", lowerRandomLettersHi, value = TRUE)
nums <- 1:2003
updated_num <- paste0("_", nums, sep="")
paste(extractHi,updated_num, sep = "")

