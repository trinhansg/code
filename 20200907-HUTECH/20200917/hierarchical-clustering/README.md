# Hierarchical-Clustering

A very basic implementation of Agglomerative Hierarchical Clustering in python. The optimal number of clusters was found using a dendrogram. The scipy.cluster.hierarchy library was imported to use the dendrogram.

Once the optimal number of clusters was found, the sklearn.cluster library was imported to use the AgglomerativeClustering class. The object of the class was created with the following parameters:
 - n_clusters = 5  ( This was the optimal number of clusters found using the dendrogram.)
 - affinity = 'euclidean'
 - linkage = 'ward' ( This method was used to minimise the within cluster variance. )

Finally, the object of the class was fitted with the dataset and the cluster values were predicted. 
