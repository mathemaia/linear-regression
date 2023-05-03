# Linear Regression
<p align="justify">My intention by writing this code was to study the probably more basic machine learning algorithm, the Linear Regression. As you can see in notebook named <i>main.ipynb</i> that contains all of the mainly code, I've written all in Python and didn't use any machine learning library to assist. Instead, I've written all from scratch and used libraries only to auxiliate the data manipulation and visualization, like <i>pandas</i> and <i>matplotlib</i>. On the next lines, I am going to comment how the problem the problem was modeled and solved, even as the logic used to the object operation.</p>

## Neuron
<p align="justify">As we are working with a neural network with only one neuron, a perceptron that receives one input, the figure I imagined on implementing it was something like this: the <i>x</i> is the data that multiplies the weight <i>w</i> and goes to the sommatory. As we are working with one feature, the sum is just the addition of the bias <i>b</i> on the multiplication of the feature by the weight.</p>

![neuron](/images/neuron.png)

The class neuron was implemmented 

```
# neuron class
class Neuron:
    global x
    
    # constructor
    def __init__(self, w, b, lr, N) -> None:
        self.w = w
        self.b = b 
        self.lr = lr
        self.predict = 0.0
        self.error = 0.0
        self.N = N
```

<<<<<<< HEAD
<p align="justify">As we are working with a neural network with only one neuron, a perceptron that receives one input, the figure I imagined on implementing it was something like this: the **x** is the data that multiplies the weight **w** and goes to the sommatory. As we are working with one feature, the sum is just the addition of the bias **b** on the multiplication of the feature by the weight.</p>
=======
## Base Algorithm
1. **Forward**: the perceptron receives the data and makes the prediction with it's current variables values
2. **MSE**: calculate the error on prediction made
3. **Backward**: update the values of the variables based on their derivatives and learning rate


## Forward
![forward](/images/forward.png)

## MSE
![mse](/images/mse.png)

## Backward
![backward](/images/backward.png)
>>>>>>> e646a96ffdae7fed67ba085a7577e75f28f71236
