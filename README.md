# Linear Regression
My intention by writing this code was to study the probably more basic machine learning algorithm, the **linear regression**. As you can see in notebook named *main.ipynb* that contains all of the mainly code, I've written all in **Python** and didn't use any machine learning library to assist. Instead, I've written all from scratch and used libraries only to auxiliate the data manipulation and visualization, like *pandas* and *matplotlib*. 


## Neuron

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
![neuron](/images/neuron.png)

## Forward
![forward](/images/forward.png)

## MSE
![mse](/images/mse.png)

## Backward
![backward](/images/backward.png)
