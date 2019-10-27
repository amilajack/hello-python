import random
import math

def k_means(items = [], k = 1):
    # Shuffle the elements
    random.shuffle(items)

    # Split into k groups
    clusters = []
    items_per_cluster = len(items) / k
    for i in range(k):
        clusters.append(items[i * items_per_cluster : (i + 1) * items_per_cluster])
    
    # Take averages of each cluster (ie. find the centers)
    centers = []
    for cluster in clusters:
        sum = 0
        for item in cluster:
            sum += item
        avg = sum / len(cluster)
        centers.append(avg)

    # For each item in each cluster, move that item to the cluster who's average (ie. the center) it is closest to
    # Note that this is only one iteration of the k-means algorithm. More complete implementations will iterate until
    # convergance
    for cluster in clusters:
        min_dist = math.inf
        min_cluster_idx = 0;
        for (cluster_idx, item) in enumerate(cluster):
            for (idx, center) in enumerate(centers):
                dist = math.abs(center - item)
                if dist < min_dist:
                    min_cluster_idx = idx
                    min_dist = dist
            if min_cluster_idx != cluster_idx:
                cluster.remove()
                clusters[cluster_idx].append(item)

    return clusters


k_means([1, 2, 3, 11, 12, 13, 21, 22, 23], 3)