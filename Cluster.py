class Cluster:

    def __init__(self, x=None, clusters=None, diff=None):
        if x is not None:
            # creation a cluster by one point
            self.height = 0
            self.center = x
            self.subclusters = []
            self.left_point = x  # to easily compute distances
            self.right_point = x  # to easily compute distances
            return
        else:
            # creation a cluster by uniting 2 or more cluster
            # where clusters is list of clusters in ascending order (left to right) to unite
            # diff is a space between them
            # both parameters are necessary
            self.height = diff / 2

            self.center = 0
            for cluster in clusters:
                self.center += cluster.center
            self.center /= len(clusters)

            self.subclusters = clusters

            self.left_point = clusters[0].left_point
            self.right_point = clusters[-1].right_point
