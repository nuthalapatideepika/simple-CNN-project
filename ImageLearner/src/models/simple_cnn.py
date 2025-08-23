import torch.nn as nn
import torch.nn.functional as F


class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10, in_channels=1):
        super(SimpleCNN, self).__init__()
        self.in_channels = in_channels
        self.conv1 = nn.Conv2d(in_channels, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)

        # Calculate fc1 input size based on input dimensions
        # For 28x28 (MNIST): after 2 pools -> 7x7
        # For 32x32 (CIFAR-10): after 2 pools -> 8x8
        if in_channels == 1:  # MNIST
            fc1_input_size = 64 * 7 * 7
        else:  # CIFAR-10 or other 3-channel inputs
            fc1_input_size = 64 * 8 * 8

        self.fc1 = nn.Linear(fc1_input_size, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)  # Flatten the tensor dynamically
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

    def change_input_channels(self, in_channels):
        """Legacy method for compatibility"""
        self.conv1 = nn.Conv2d(in_channels, 32, kernel_size=3, stride=1, padding=1)
        if in_channels == 1:
            self.fc1 = nn.Linear(64 * 7 * 7, 128)  # MNIST
        else:
            self.fc1 = nn.Linear(64 * 8 * 8, 128)  # CIFAR-10
