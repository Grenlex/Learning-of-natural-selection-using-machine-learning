

import torch
from torch import nn
import torch.nn.functional as F
import numpy as np
import torch.optim as optim



class Model(nn.Module):
    def __init__(self, input_size, num_classes, h_size):
        super(Model, self).__init__()

        self.h_size = h_size
        self.input_size = input_size
        self.num_classes = num_classes
        self.num_layers = 1

        self.rnn = nn.RNN(input_size=input_size, hidden_size=h_size, num_layers=self.num_layers)
        self.fc1 = nn.Linear(h_size, num_classes)
        self.relu=nn.ReLU()

    def forward(self, input_tensor):
        out, _ = self.rnn(input_tensor)
        ans = torch.tensor([0.0,0.0,0.0])
        for i in range (out.size()[1]): #seq_lenght = 10
            teni=self.fc1(out[0][i])
            teni=self.relu(teni)
            ans = torch.cat((ans, teni), 0)
        return ans[3:].view(out.size()[1], 3)
input_size = 1
seq_lenght = 10
num_classes = 3
h_size = 5

mymodel = Model(input_size, num_classes, h_size)

criterion = nn.MSELoss()
learning_rate = 0.7
optimizer=optim.SGD(mymodel.parameters(), lr=learning_rate)

for i in range (20):
    output = mymodel((x[i%20].view(1,10,1)).float())
    loss = criterion(output, y[i%20].float())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print(loss)
