import torch
import torch.functional as F
import torch.nn as nn
from torch.autograd import Variable
from torch.nn import parameter
import torch.optim as optim
from torch.optim import optimizer
from torch.nn.parameter import Parameter



x = torch.tensor([[-1, 0],
                  [0, -1],
                  [0, 0], 
                  [0, 2], 
                  [1, 2], 
                  [2, 1]])

y = torch.tensor([[1],
                  [1],
                  [1],
                  [-1],
                  [-1],
                  [-1]])  

w = torch.tensor([0.1, 0.1]).unsqueeze(1)

b = torch.tensor([[0.1],
                 [0.1]])

w = Variable(w, requires_grad = True)
#b = Variable(b, requires_grad = True)

calcaulate = nn.Linear(6, 2)
calcaulate.weight = Parameter(w)
#calcaulate.bias = Parameter(b)


for i in range(1, 500):

    y_pred = calcaulate(x)

    loss = nn.SmoothL1Loss(y_pred, y)
    optimizer = optim.SGD()
    loss.backward()
    optimizer.step()

    if i % 50 == 0:
        print(loss)

print(calcaulate.weight)
print(calcaulate.bias)



