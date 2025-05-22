import cv2
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def extract_dominant_color(image_path, k=3):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((-1, 3))
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(image)
    colors = kmeans.cluster_centers_.astype(int)
    counts = Counter(kmeans.labels_)
    dominant = colors[counts.most_common(1)[0][0]]
    return tuple(dominant)

def plot_colors(colors):
    patches = [np.ones((100, 100, 3), dtype=np.uint8) * color for color in colors]
    fig, axes = plt.subplots(1, len(patches))
    for ax, patch in zip(axes, patches):
        ax.imshow(patch)
        ax.axis('off')
    plt.show()
