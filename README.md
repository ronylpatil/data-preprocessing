Data Preprocessing
==============================

Will explore categorical encoding, discretization, missing value treatment, feature scaling, handle outliers, and feature transformation in depth

Advance Preprocessing Techniques
------------

    ├── Outlier Detection Technique
    │   ├── Univariate Technique        
    │   │    ├── Z-Score      
    │   │    └── IQR
    │   └── Bivariate/Multivariate Technique               
    │       ├── Isolation Forest
    │       ├── KNN
    │       ├── LoF (Local Outlier Factor)
    │       └── DBSCAN (Density-Based Spatial Clustering of Application with Noise)
    │
    ├── Missing Value Handling
    │   ├── MCAR (Missing Completely At Random)
    │   ├── MAR (Missing at Random)
    │   └── MNAR (Missing Not at Random)
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

