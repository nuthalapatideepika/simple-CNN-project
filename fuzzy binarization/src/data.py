# src/data.py
import random
import numpy as np
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def set_random_seeds(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

def get_loaders(batch_size, train=True, data_dir="data"):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    dataset = datasets.MNIST(root=data_dir, train=train, download=True, transform=transform)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=train)
    return loader