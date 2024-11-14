import numpy as np

class KMeans:
  def __init__(self, n_clusters, random_state=0):
    self.n_clusters = n_clusters
    self.random_state = random_state
    self.centroids = None
    self.clusters = None
    self.labels = None

  def fit(self, X):
    np.random.seed(self.random_state)
    self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]
    self.clusters = np.zeros(X.shape[0])
    self.labels = np.zeros((self.n_clusters, X.shape[1]))

    while True:
      new_clusters = np.zeros(X.shape[0])
      for i, x in enumerate(X):
        new_clusters[i] = np.argmin(np.linalg.norm(self.centroids - x, axis=1))
      if np.array_equal(self.clusters, new_clusters):
        break
      self.clusters = new_clusters

      for i in range(self.n_clusters):
        points_in_cluster = X[self.clusters == i]
        if len(points_in_cluster) > 0:
          self.labels[i] = np.mean(points_in_cluster, axis=0)
        else:
          self.labels[i] = self.centroids[i]

  def predict(self, X):
    return np.array([np.argmin(np.linalg.norm(self.labels - x, axis=1)) for x in X])

model = KMeans(3)
X = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])
model.fit(X)
print(model.predict(X))