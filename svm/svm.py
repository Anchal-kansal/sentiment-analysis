# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# importing scikit learn with make_blobs
from sklearn.datasets.samples_generator import make_blobs
# import support vector classifier
from sklearn.svm import SVC # "Support Vector Classifier"

# creating datasets X containing n_samples
# Y containing two classes
X, Y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=0.40)

# plotting scatters
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring');
plt.show()
# creating line space between -1 to 3.5
xfit = np.linspace(-1, 3.5)

# plotting scatter
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring')

# plot a line between the different sets of data
for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, -0.2)]:
    yfit = m * xfit + b
    plt.plot(xfit, yfit, '-k')
    plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none',
    color='#AAAAAA', alpha=6.4)

plt.xlim(-1, 3.5);
plt.show()

# reading csv file and extracting class column to y.
with open('data.csv', 'rb') as f:
    x = f.readlines()
a = np.array(x)
y  = a[:]
# extracting two features
x = np.column_stack((x.positive,x.negative))
x.shape # 27 samples and 2 features


clf = SVC(kernel='linear')

# fitting x samples and y classes
clf.fit(x, y)
