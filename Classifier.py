from Cluster import *
from data import *


class HierarchyClassifier:

    def __init__(self):
        self.clusters = None
        self.ch_cluster = None

    def set_points(self, points):
        points = sorted(points)
        self.clusters = []
        for point in points:
            self.clusters.append(Cluster(x=point))

    # main algorithm
    def classify(self):
        clusters = self.clusters.copy()
        it = 1
        while len(clusters) != 1:
            print("\nIteration ", it)
            diff, starts_i, ends_i = self._find_least_diffence(clusters)
            # renew list of clusters
            temp = clusters[0:starts_i[0]]
            for i in range(len(starts_i)):
                temp.append(Cluster(clusters=clusters[starts_i[i]:ends_i[i] + 1], diff=diff))
                temp += clusters[ends_i[i] + 1:starts_i[i + 1] if i + 1 < len(starts_i) else len(clusters)]

            clusters = temp
            prepare_to_draw_hierarchy(clusters)
            plt.grid()
            plt.title("Iteration " + str(it))
            plt.show()
            it += 1

        return clusters

    # method returns min distance, indices of sequences where
    # distance of neighbors are the same
    # and indices of ends of these sequences
    def _find_least_diffence(self, clusters):
        min_diff = None
        seqOn = False
        starts = []
        ends = []
        for i in range(len(clusters) - 1):
            diff = clusters[i + 1].left_point - clusters[i].right_point
            if min_diff is None or min_diff > diff:
                min_diff = diff
                starts = [i]
                ends = [i + 1]
                seqOn = True
            elif min_diff == diff:
                if seqOn:
                    ends[len(ends) - 1] += 1
                else:
                    starts.append(i)
                    ends.append(i + 1)
                    seqOn = True
            elif seqOn:
                seqOn = False

        return min_diff, starts, ends