# Write a program to demonstrate PCA on any high-dimensional dataset. 
# Perform PCA to reduce the dataset to 2 principal components. 
# Visualize the transformed data in a 2D scatter plot. 
# Write the inference/analysis of each

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
data = load_iris()
X,y = data.data,data.target

model = PCA(n_components=2)
X_pca = model.fit_transform(X)

plt.scatter(X_pca[:,0], X_pca[:,1], c=y)