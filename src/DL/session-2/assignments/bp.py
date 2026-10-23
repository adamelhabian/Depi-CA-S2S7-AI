# the assignment of this session is writable equations on my notebook and in this file i will apply what i made in backpropagation using python code

import math

# Sigmoid function it's the activation function that i use for hidden layer neurons and output layer neurons 
def sigmoid(z):
    return 1 / (1 + math.exp(-z))


#  we have 2 input neurons , 1 hidden layer with 2 neurons and output layer with 2 neurons 
X1, X2 = 0.05, 0.10
target1, target2 = 0.01, 0.99


W1, W2 = 0.15, 0.20
W3, W4 = 0.25, 0.30
W5, W6 = 0.40, 0.45
W7, W8 = 0.50, 0.55

# Initial biases
# Each hidden layer has one bias so the 2 neurons of 
B1 = 0.35
B2 = 0.60

# Learning rate
learning_rate = 0.5


def forward():
    # Hidden layer: pre-activation values
    ZH1 = X1 * W1 + X2 * W2 + B1
    ZH2 = X1 * W3 + X2 * W4 + B1

    # Hidden layer: post-activation values
    H1 = sigmoid(ZH1)
    H2 = sigmoid(ZH2)

    # Output layer: pre-activation values
    ZO1 = H1 * W5 + H2 * W6 + B2
    ZO2 = H1 * W7 + H2 * W8 + B2

    # Output layer: predictions
    O1 = sigmoid(ZO1)
    O2 = sigmoid(ZO2)

    # Total squared-error loss
    E1 = 0.5 * (target1 - O1) ** 2
    E2 = 0.5 * (target2 - O2) ** 2
    E_total = E1 + E2

    return (
        ZH1, ZH2, H1, H2,
        ZO1, ZO2, O1, O2,
        E1, E2, E_total
    )


def backpropagation():
    global W1, W2, W3, W4
    global W5, W6, W7, W8
    global B1, B2

    # Forward pass
    (
        ZH1, ZH2, H1, H2,
        ZO1, ZO2, O1, O2,
        E1, E2, E_total
    ) = forward()

    # Save old output weights before updating anything
    old_W5, old_W6 = W5, W6
    old_W7, old_W8 = W7, W8

    # Derivatives of total error with respect to output pre-activations
    # dzo1 -> d Et / d zo1 = (d Et / d o1) * (do1 / d zo1)
    DZO1 = (O1 - target1) * O1 * (1 - O1)
    DZO2 = (O2 - target2) * O2 * (1 - O2)

    # Gradients for output weights
    dW5 = DZO1 * H1
    dW6 = DZO1 * H2
    dW7 = DZO2 * H1
    dW8 = DZO2 * H2

    # Gradients for output biases
    # since d zo1 and d zo2 for d b
    dB2 = DZO1+ DZO2

    # Backpropagate through both output neurons
    # DH1 , DH2 are  the h1 , h2 before activation 
    DH1 = (
        DZO1 * old_W5 + DZO2 * old_W7
    ) * H1 * (1 - H1)

    DH2 = (
        DZO1 * old_W6 + DZO2 * old_W8
    ) * H2 * (1 - H2)

    # Gradients for hidden weights
    dW1 = DH1 * X1
    dW2 = DH1 * X2
    dW3 = DH2 * X1
    dW4 = DH2 * X2

    # Gradients for hidden biases
    dB1 = DH1+ DH2

    # Update all weights
    W1 -= learning_rate * dW1
    W2 -= learning_rate * dW2
    W3 -= learning_rate * dW3
    W4 -= learning_rate * dW4

    W5 -= learning_rate * dW5
    W6 -= learning_rate * dW6
    W7 -= learning_rate * dW7
    W8 -= learning_rate * dW8

    # Update all biases
    B1 -= learning_rate * dB1
    

    B2 -= learning_rate * dB2
    

    return E_total, O1, O2




print("INITIAL VALUES OF PARAMETERS USING FORWARD PASS")

initial = forward()

print(f"ZH1 = {initial[0]:.6f}")
print(f"ZH2 = {initial[1]:.6f}")
print(f"H1  = {initial[2]:.6f}")
print(f"H2  = {initial[3]:.6f}")
print(f"ZO1 = {initial[4]:.6f}")
print(f"ZO2 = {initial[5]:.6f}")
print(f"O1  = {initial[6]:.6f}")
print(f"O2  = {initial[7]:.6f}")
print(f"E1  = {initial[8]:.6f}")
print(f"E2  = {initial[9]:.6f}")
print(f"Total Error = {initial[10]:.6f}")

# Perform the first backpropagation update
backpropagation()

print("\n AFTER FIRST UPDATE ")

first_update = forward()

print(f"O1 = {first_update[6]:.6f}")
print(f"O2 = {first_update[7]:.6f}")
print(f"Total Error = {first_update[10]:.6f}")



# Train for 10,000 iterations


for iteration in range(2, 10001):
    backpropagation()

    if iteration in (100, 1000, 5000, 10000):
        result = forward()
        print(
            f"Iteration {iteration:5d} | "
            f"O1 = {result[6]:.6f} | "
            f"O2 = {result[7]:.6f} | "
            f"Error = {result[10]:.8f}"
        )
        



# Final prediction


final = forward()

print("\nFINAL PREDICTION")
print(f"Input: X1 = {X1}, X2 = {X2}")
print(f"Desired Output 1 = {target1}")
print(f"Desired Output 2 = {target2}")
print(f"Predicted Output 1 = {final[6]:.6f}")
print(f"Predicted Output 2 = {final[7]:.6f}")
print(f"Final Total Error = {final[10]:.8f}")