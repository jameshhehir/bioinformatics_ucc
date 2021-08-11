library("DESeq2")
count_data <- read.table("RNA_Seq_assignment3.txt")
condition <- c("A", "A", "A", "A", "B", "B","B", "B")
sample <- c("sample1", "sample2","sample3","sample4","sample5","sample6","sample7","sample8")
metadata <- data.frame(sample, condition)

dds <- DESeqDataSetFromMatrix(countData=count_data, 
                              colData=metadata, 
                              design=~condition)

dds <- DESeq(dds)
res <- results(dds)


summary(res,alpha=0.05)
select <- rownames(resSig)
select

resOrdered = res[order(res$log2FoldChange),]
resSig = subset(resOrdered, padj<0.05)
bottom5 <- tail(resSig, n=5)
top5 <- head(res, n=5)
merged <- rbind(bottom5, top5)

library("pheatmap")
merged1 <- rownames(merged) 
rlog1 <- rlog(dds, blind = F) 
dataframe <- as.data.frame(colData(dds)[,c("condition")]) 
colnames(df) = "condition" 
heatmap(assay(rlog1)[merged1,])

resOrdered1 = res[order(res$lfcSE),]
resSig1 = subset(resOrdered1, padj<0.05)
top10 <- head(resSig1,n=10)

sd_top10 <- rownames(top10) 
rlog2 <- rlog(dds, blind = F) 
dataframe1 <- as.data.frame(colData(dds)[,c("condition")]) 
colnames(dataframe1) = "condition" 
heatmap(assay(rlog2)[sd_top10,])

library(biomaRt)

mart <- useMart(dataset="merged",biomart='ensembl')

boxplot(merged)

