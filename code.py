import numpy as np
class NeuralNetworkLayer:
    def __init__(self, input_size, output_size):
        input_size = max(1, int(input_size)) 
        output_size = max(1, int(output_size)) 
        self.W = np.random.rand(input_size, output_size)
        self.b = np.random.rand(output_size)
    def forward(self, x):
 
        return np.dot(x, self.W) + self.b
    def display(self):
     
        print("\nWeight matrix W:")
        print(self.W)
        print("\nBias vector b:")
        print(self.b)
if __name__ == "__main__":
    input_x = float(input("Enter the input size x: "))
    output_y = float(input("Enter the output size y: "))

    layer = NeuralNetworkLayer(input_x, output_y)
    
    layer.display()
    
    x = np.random.rand(int(max(1, input_x))) 
    print("\nInput vector x:")
    print(x)
    
    output = layer.forward(x)
    print("\nOutput vector y:")
    print(output)