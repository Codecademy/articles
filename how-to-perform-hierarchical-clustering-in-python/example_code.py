import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset from: https://data.cityofnewyork.us/Education/2005-2015-Graduation-Outcomes/qk7d-gecv
grad = pd.read_csv('2005_-_2015_Graduation_Outcomes.csv')

grad_data_points = grad.loc[:,['% of cohort Local','% of cohort Dropped Out']]

# Dendrogram Examples
import scipy.cluster.hierarchy as sch

# Dendrogram Example 1

d = sch.dendrogram(sch.linkage(grad_data_points, method = "ward"))

plt.title('Dendrogram')
plt.xlabel('Cohorts')
plt.ylabel('Distance')

plt.show()

# Dendrogram Example 2

d = sch.dendrogram(sch.linkage(grad_data_points, method = "complete", metric="cityblock"))

plt.title('Dendrogram')
plt.xlabel('Cohorts')
plt.ylabel('Distance')

plt.show()

# Clustering Examples

from sklearn.cluster import AgglomerativeClustering

# Clustering Example 1

cluster = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
grad_clustered = cluster.fit_predict(grad_data_points)

plt.scatter(grad_data_points['% of cohort Local'],grad_data_points['% of cohort Dropped Out'], s=100, c=grad_clustered)

plt.xlabel('% Local')
plt.ylabel('% Dropped Out')

plt.show()

# Clustering Example 2

cluster = AgglomerativeClustering(n_clusters = 3, linkage = 'complete', affinity = 'cityblock')
grad_clustered = cluster.fit_predict(grad_data_points)

plt.scatter(grad_data_points['% of cohort Local'],grad_data_points['% of cohort Dropped Out'], s=100, c=grad_clustred)

plt.xlabel('% Local')
plt.ylabel('% Dropped Out')

plt.show()
