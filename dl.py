import random
import math

X_train = [[random.random() for _ in range(10)] for _ in range(100)] 
y_train = [random.randint(0, 1) for _ in range(100)]  


weights = [random.random() for _ in range(10)]
bias = random.random()


learning_rate = 0.1
epochs = 10
for epoch in range(epochs):
    for inputs, label in zip(X_train, y_train):

        weighted_sum = sum(w * x for w, x in zip(weights, inputs)) + bias
   
        predicted = 1 / (1 + math.exp(-weighted_sum))
      
        error = predicted - label
        
        weights = [w - learning_rate * error * x for w, x in zip(weights, inputs)]
        bias -= learning_rate * error

X_test = [[random.random() for _ in range(10)] for _ in range(10)] 
predictions = []
for inputs in X_test:
 
    weighted_sum = sum(w * x for w, x in zip(weights, inputs)) + bias
    
    predicted = 1 / (1 + math.exp(-weighted_sum))
    predictions.append(predicted)

print("Predictions:", predictions)
