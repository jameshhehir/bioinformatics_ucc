#Q3
#a
ensembl1 <- "ENS"
i <- substr(row.names(data), 0, nchar(ensembl1))==ensembl1
rows_ens <- data[i,]
nrow(rows_ens)

#b
library(biomaRt)

mart = useMart("ENSEMBL_MART_ENSEMBL")
mart_mouse <- useDataset("mmusculus_gene_ensembl", mart= mart)
qb <- getBM(attributes = c("ensembl_gene_id", "description"), filters = "ensembl_gene_id", values = (rownames(rows_ens)), mart = mart_mouse)
qb

#c
x <- getSequence(id="ENSMUSG00000000120", type = "ensembl_gene_id", seqType = "peptide", mart= mart_mouse)
x$peptide

#d
nchar(x$peptide)

