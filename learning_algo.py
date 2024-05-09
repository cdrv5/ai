X_train = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
y_train = ['A', 'A', 'B', 'B', 'B']  

def euclidean_distance(x1, x2):
    
    return ((x1[0] - x2[0]) * 2 + (x1[1] - x2[1]) * 2) ** 0.5

def knn_predict(X_train, y_train, x_test, k=3):
    distances = []
    for i, x_train in enumerate(X_train):
        distance = euclidean_distance(x_train, x_test)
        distances.append((distance, i))

    distances.sort()  
    k_nearest = distances[:k]  

    nearest_labels = [y_train[i] for _, i in k_nearest]
    prediction = max(set(nearest_labels), key=nearest_labels.count)  
    return prediction


X_test = [2.5, 3.5]  
k = 3  

prediction = knn_predict(X_train, y_train, X_test, k)
print("Predicted class:", prediction)
