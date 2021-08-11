library(limma)

eset <- expresso(assignment3,bgcorrect.method="rma",
                 normalize.method="quantiles",
                 pmcorrect.method="pmonly",
                 summary.method="medianpolish")


annot <- pData(eset)
design <- model.matrix(~0 +annot[, "sample"])
colnames(design) <- c("diseased", "healthy")
cm <- makeContrasts(DiseasedVsHealthy = diseased-healthy, levels=design)
print(cm)
fit <- lmFit(eset, design)
fit2 <- contrasts.fit(fit, cm)
fit2 <- eBayes(fit2)
results <- topTable(fit2, "DiseasedVsHealthy",number=Inf, p.value = 0.05)
head(results)

