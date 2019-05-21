import numpy as np
import matplotlib.pyplot as plt
import pickle


# generate point in ascending order
def generate_data():
    array = np.random.random_integers(-100, 100, 15)
    points = set(array)
    points = sorted(list(points))
    plt.scatter(points, [0 for i in points])
    plt.title("Generated points")
    plt.show()
    print(points)
    return points


def save_points(points):
    with open("test_points", mode='wb') as file:
        pickle.dump(points, file)
    return points


def read_points():
    with open("test_points", mode='rb') as file:
        points = pickle.load(file)
    plt.title("Read points")
    plt.scatter(points, [0 for i in points])
    plt.show()
    return points

# after this you should call plt.show()
def prepare_to_draw_hierarchy(clusters):
    for cluster in clusters:
        for sub in cluster.subclusters:
            list1 = [cluster.center, sub.center]
            list2 = [cluster.height, sub.height]
            plt.plot(list1, list2, color="black")
        plt.scatter([cluster.center], [cluster.height])
        plt.text(cluster.center + 0.01 * plt.ylim()[0], cluster.height + 0.01 * plt.ylim()[1], ("{0:.2f}".format(cluster.center)))

        for c in cluster.subclusters:
            prepare_to_draw_hierarchy([c])


