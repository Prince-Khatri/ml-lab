# Using any dataset implement Hierarchical Clustering (AGNES and DIANA). 
# Plot the Dendrogram for Hierarchical Clustering and analyze your result. 
# Plot the clustering output for the same dataset using these two hierarchical techniques. 
# Compare the results. Write the inference.

from sklearn.cluster import AgglomerativeClustering, BisectingKMeans
from scipy.cluster.heirarchy import linkage, dendrogram
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
X,y = make_blobs(10)
agnes = AgglomerativeClustering()
diana = BisectingKMeans()

a_l = agnes.fit_predict(X)
d_l = diana.fit_predict(X)


plt.scatter(X[:,0],X[:,1],c=a_l)
plt.show()
plt.scatter(X[:,0],X[:,1],c=d_l)
plt.show()

dendrogram(linkage(X,method="ward"))

