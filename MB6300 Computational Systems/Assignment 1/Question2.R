#Question2
#a
data <-read.table("MB6300_Assignment_1_data.txt")
dim(data)
class(data)

#b
ptm <- proc.time()
averages <- apply(data,1,mean)
which.max(averages)
# Stop the clock
proc.time() - ptm
data["gene_25722",]

#c
ptm <- proc.time()
averages1 <- NULL
for(i in 1:nrow(data)) {
  averages1[i] <- rowMeans(data[i ,])
}
which.max(averages1)
# Stop the clock
proc.time() - ptm

#d
highest_avg_exp <- function(input_file, output_file) {
  data <- read.table(input_file)
  output <- apply(data,1,mean)
  max1 <- which.max(output)
  write.table(max1, output_file)
}

highest_avg_exp("MB6300_Assignment_1_data.txt", "Q2D.txt")