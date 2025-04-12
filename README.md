# Hierarchical Clustering for Gene Expression Data

 ## Project Overview
This project focuses on hierarchical clustering of gene expression data, specifically from the Leukemia GSE9476 dataset. Using scikit-learn, SciPy, and seaborn, we perform data preprocessing, standardization, and hierarchical clustering to explore patterns and similarities in gene expression data. The insights gained from this analysis can help identify subtypes of leukemia and related biological processes, which could be crucial for better understanding the disease and developing targeted therapies.

 ## Dataset: Leukemia GSE9476
The Leukemia GSE9476 dataset contains gene expression data from Leukemia patients, which includes samples of different leukemia types. This dataset is available from the Gene Expression Omnibus (GEO) and is often used for research related to leukemia classification.

### Dataset Features
* samples: This column contains unique identifiers for each sample (representing individual leukemia patient samples).

* type: The type of leukemia each sample represents (e.g., Acute Myelogenous Leukemia, Chronic Lymphocytic Leukemia, etc.).

 * Gene Expression Data: Each column represents the expression levels of a specific gene across the samples. The values are continuous and represent the level of gene expression.

## Insight Gained from Clustering Analysis
Hierarchical clustering was performed on the Leukemia GSE9476 dataset to uncover the hidden structure within the gene expression data. Below are the key insights gained:

**1.**  **Sample Grouping by Gene Expression** : The hierarchical clustering analysis successfully grouped the leukemia samples into clusters based on similarity in gene expression patterns. This suggests that there are underlying subgroups within the leukemia samples that share common gene expression profiles. These subgroups may represent different leukemia subtypes or stages, which can help in identifying more accurate diagnostic markers.

**2.** **Cluster-Specific Gene Expression Patterns**: By visualizing the average gene expression per cluster through a heatmap, we observed that certain clusters exhibited distinct gene expression patterns. This implies that different clusters may be driven by specific genes that are highly expressed or suppressed in those groups. These genes could serve as potential biomarkers for leukemia classification or therapeutic targeting.

**3.** **Potential Subtypes of Leukemia**: The clustering results show that the samples are grouped into several clusters (e.g., 4 clusters in this analysis). This indicates that the leukemia samples can be divided into distinct subtypes, each potentially having different genetic drivers and clinical behaviors. These clusters could be further analyzed to correlate with clinical outcomes or response to treatments.

**4.**  **Dendrogram Insights**: The dendrogram visualization revealed the hierarchical relationships between the samples. It helped us visualize how the samples are related to each other based on their gene expression. The structure of the dendrogram can also give insights into whether certain sample types (e.g., different leukemia subtypes) are more closely related or more distinct from each other.

**5.** **Average Gene Expression Per Cluster**: The heatmap of average gene expression across clusters provides an overview of how the genes behave differently across the identified clusters. Some clusters exhibit higher expression of certain genes, while others show lower expression, suggesting biologically meaningful distinctions between the clusters. These distinctions could be useful for diagnostic or prognostic purposes in leukemia research.

## Project Files
* **clustering.py**: Python script that handles data loading, preprocessing, clustering, and visualization.

* **Leukemia_GSE9476.csv**: Gene expression data (CSV format).

* **Leukemia_Clustering_Insights.pdf**: PDF report containing the analysis insights and visualizations.

* **README.md**: This file.

## How to Run the Project

**1.** **Clone the repository** :
```
git clone https://github.com/your-username/Hierarchical-Clustering-for-Gene-Expression-Data.git
```
**2.** **Navigate to the project directory:**
```
cd Hierarchical-Clustering-for-Gene-Expression-Data
```
**3.** **Set up your Python environment:**

* **It's recommended to create a virtual environment and install the required dependencies:**
```
python -m venv venv
.\venv\Scripts\activate  # For Windows
# or
source venv/bin/activate  # For macOS/Linux
```
* **Install required libraries:**
```
pip install -r requirements.txt
```
**5.** **Run the clustering.py script to perform hierarchical clustering and generate the results:**
```
python clustering.py
```

