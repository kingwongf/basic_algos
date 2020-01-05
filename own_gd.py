import numpy as np

def step_gd(points, current_beta, current_alpha, learning_rate):
    d_beta = d_alpha = 0
    for i in range(len(points)):
        d_beta += 2/len(points)*(points[i,1] - points[i,0]*current_beta)*-points[i,0]
        d_alpha += 2/len(points)*-(points[i,1] - points[i,0]*current_beta)
    new_beta = current_beta - learning_rate*d_beta
    new_alpha = current_alpha - learning_rate*d_alpha
    return new_beta, new_alpha

def run_gd():
    beta = 0
    alpha = 0
    points = np.genfromtxt("data.csv", delimiter=",")
    for i in range(1000):
        beta, alpha = step_gd(np.array(points), beta, alpha, 0.0001)
        print(beta,alpha)

run_gd()