from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],
               [10, 2], [10, 4], [10, 0]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)
###array([1, 1, 1, 0, 0, 0], dtype=int32)
print(kmeans.predict([[0, 0], [12, 3]]))
###array([1, 0], dtype=int32)
print(kmeans.cluster_centers_)
# array([[10.,  2.],
#        [ 1.,  2.]])