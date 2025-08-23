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
    from torch.utils.data import TensorDataset, DataLoader
    
    # Load mock data
    if train:
        images = torch.load(f'{data_dir}/mock_train_images.pt').float() / 255.0
        labels = torch.load(f'{data_dir}/mock_train_labels.pt')
    else:
        images = torch.load(f'{data_dir}/mock_test_images.pt').float() / 255.0
        labels = torch.load(f'{data_dir}/mock_test_labels.pt')
    
    # Add channel dimension and normalize
    images = images.unsqueeze(1)  # Add channel dimension
    
    # Normalize to standard range
    images = (images - 0.1307) / 0.3081
    
    # For fuzzy binarization, we need binary labels (0 or 1)
    # Convert MNIST labels (0-9) to binary (0: even digits, 1: odd digits)
    labels = labels % 2
    
    # Create dataset
    dataset = TensorDataset(images, labels)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=train)
    return loader