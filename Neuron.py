# classe neurônio
class Neuron:
    global x

    # método construtor que inicializa as variáveis w, b e lr
    def __init__(self, w, b, lr, N) -> None:
        self.w = w
        self.b = b 
        self.lr = lr
        self.predict = 0.0
        self.error = 0.0
        self.N = N
        self.x = 0

    # método que calcula a predição
    def forward(self, x) -> float:
        self.x = x
        self.predict = self.w * self.x + self.b

    # método que calcula as derivadas e atualiza as variáveis
    def backward(self) -> None:
        dw = (1 / self.N) * self.x * self.error
        db = (1 / self.N) * self.error

        self.w = self.w - self.lr * dw
        #self.b = self.b - self.lr * db
    
    # função que calcula o erro
    def MSE(self, y) -> float:
        self.error = (self.predict - y) ** 2

    
    
