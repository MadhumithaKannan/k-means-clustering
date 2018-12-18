from statistics import mean
import numpy as np


def kmeans():
    data_points = [[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]]
    cluster_head = [data_points[0], data_points[3], data_points[6]]
    print('LABEL                     CLUSTER HEADS')

    while (1):
        new_cluster_head = []
        sum = 0
        x = []
        y = []
        label = []

        for i in range(0, len(data_points)):
            mindist = 1000
            for j in range(0, len(cluster_head)):
                sum = (data_points[i][0] - cluster_head[j][0]) ** 2 + (data_points[i][1] - cluster_head[j][1]) ** 2
                dist = np.sqrt(sum)
                if dist <= mindist:
                    mindist = dist
                    minc = j
            label.append(minc)
        print(label,cluster_head)

        for j in range(0, len(cluster_head)):
            for i in range(0, len(data_points)):
                if label[i] == j:
                    x.append(data_points[i][0])
                    y.append(data_points[i][1])

            newx = mean(x)
            newy = mean(y)
            x.clear()
            y.clear()
            new_cluster_head.append([newx, newy])

        if cluster_head != new_cluster_head:
            cluster_head = new_cluster_head
        else:
            break
    print('---FINAL RESULT--- \n',label,cluster_head)


if __name__ == '__main__':
    kmeans()
