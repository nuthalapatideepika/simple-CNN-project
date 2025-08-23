# src/models/fuzzy_cnn.py
import torch
from torch import nn

class FuzzyCNN(nn.Module):
    """Compact CNN for fuzzy binarization."""
    def __init__(self, in_channels=1, num_classes=2, dropout=0.2):
        super().__init__()
        c = 32
        self.features = nn.Sequential(
            nn.Conv2d(in_channels, c, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(c, c, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Conv2d(c, 2 * c, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Conv2d(2 * c, 4 * c, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.AdaptiveAvgPool2d((1, 1)),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Dropout(p=dropout),
            nn.Linear(4 * c, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x
    