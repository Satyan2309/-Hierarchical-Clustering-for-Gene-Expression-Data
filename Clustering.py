# clustering.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.preprocessing import StandardScaler


df = pd.read_csv(r'E:\ML_project\data\Leukemia_GSE9476.csv')


print("Data shape :" ,df.shape)
print(df.head())


sample_labels = df['type']


expression_data = df.drop(columns=['samples', 'type'])

expression_data = expression_data.apply(pd.to_numeric, errors='coerce')


scaler = StandardScaler()
scaled_data = scaler.fit_transform(expression_data)


linked = linkage(scaled_data, method='ward')


plt.figure(figsize=(15, 6))
dendrogram(linked, labels=sample_labels.values, leaf_rotation=90)
plt.title('Hierarchical Clustering of Samples')
plt.xlabel('Sample Type')
plt.ylabel('Euclidean Distance')
plt.tight_layout()
plt.show()



cluster_labels = fcluster(linked, t=4, criterion='maxclust')


df['Cluster'] = cluster_labels
print("\nSample cluster assignments:")
print(df[['type', 'Cluster']].head(10))

#
df_clustered = pd.DataFrame(scaled_data)
df_clustered['Cluster'] = cluster_labels


mean_cluster_exp = df_clustered.groupby('Cluster').mean().T

print("\nHeatmap matrix shape:", mean_cluster_exp.shape)
print("Any NaNs in heatmap data?", mean_cluster_exp.isnull().values.any())

mean_cluster_exp = mean_cluster_exp.fillna(0)

plt.figure(figsize=(12, 8))
sns.heatmap(mean_cluster_exp, cmap='viridis')
plt.title('Average Gene Expression per Cluster')
plt.xlabel('Cluster')
plt.ylabel('Gene')
plt.tight_layout()
plt.show()
