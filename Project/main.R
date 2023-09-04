library(GEOquery)
library(limma)
library(Biobase)
library(ggplot2)


dataset <- getGEO( "GSE48558", GSEMatrix = TRUE,AnnotGPL = TRUE , destdir = ".")

dataset <- dataset[[1]]

dataset<- dataset[,which(dataset$source_name_ch1 == "AML Patient"
                         | dataset$`phenotype:ch1` == "Normal")]


grouped = list()
for(i in 1:length(dataset$`phenotype:ch1`) ) {                                   
  if (dataset$source_name_ch1[i] != "AML Patient") {
    grouped[[length(grouped) + 1]] <- "Normal"
  } else {
    grouped[[length(grouped) + 1]] <- "Test"
  }
}

a <- 0
for(i in 1:length(dataset$`phenotype:ch1`)){
  if (grouped[[i]] == "Normal"){
    a <- a + 1
  }
}
print(a / length(dataset$`phenotype:ch1`))




print(min(exprs(dataset)))
print(max(exprs(dataset)))


plot(exprs(dataset))
boxplot(exprs(dataset))

summary(exprs(dataset))
library(caret)
preproc1 <- preProcess(exprs(dataset), method=c("center", "scale"))
norm1 <- predict(preproc1, exprs(dataset))
plot(norm1)




sourcenames = list()
for(i in 1:length(dataset$`phenotype:ch1`) ) {                                   
  if (dataset$source_name_ch1[i] != "AML Patient") {
    sourcenames[[length(sourcenames) + 1]] <- strsplit2(dataset$source_name_ch1[i], "\\+")[1, 1]
  } else {
    sourcenames[[length(sourcenames) + 1]] <- "AML" 
  }
}

library(pheatmap)

pheatmap(cor(exprs(dataset)), fontsize = 15
         ,color=colorRampPalette(c("red", "white", "green"))(50),
         labels_row =  sourcenames
         , labels_col =  sourcenames)



pca <- prcomp(exprs(dataset))
plot(pca)
pcr <- data.frame(pca$r[,1:3] , Group = grouped)
ggplot(pcr , aes(PC1 , PC2 , size = 4, color=dataset$source_name_ch1)) + geom_point(size=3)




better_pca <- prcomp(t(scale(t(exprs(dataset)) , scale = FALSE)))
plot(better_pca)
better_pcr <- data.frame(pca$r[,1:3] , Group = grouped)
ggplot(better_pcr , aes(PC1 , PC2 , size = 4, color=dataset$source_name_ch1)) + geom_point(size=3)


library(M3C)
tnse_model <- tsne(dataset,labels=as.factor(dataset$source_name_ch1))
plot(tnse_model)





library(RDRToolbox)
lle_model = LLE(t(exprs(dataset)), dim=2, k=18)
plotDR(data=lle_model, labels=as.factor(dataset$source_name_ch1), axesLabels=c("", ""), legend=TRUE)

