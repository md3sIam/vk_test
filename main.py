from Classifier import *
from data import *


# points = save_points(generate_data())
points = read_points()
hc = HierarchyClassifier()
hc.set_points(points)
classified = hc.classify()

prepare_to_draw_hierarchy(classified)
plt.grid()
plt.title("Result")
plt.show()
print(points)
# print([points[i + 1] - points[i] for i in range(len(points) - 1)])


