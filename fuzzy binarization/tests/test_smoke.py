# tests/test_smoke.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import torch
from models.fuzzy_cnn import FuzzyCNN

def test_forward_shape():
    model = FuzzyCNN(in_channels=1, num_classes=2)
    x = torch.randn(4, 1, 28, 28)
    y = model(x)
    assert y.shape == (4, 2)