#!/usr/bin/env python3
"""
Demo script to show fuzzy binarization works without network dependencies
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import torch
import torch.nn as nn
from torch.optim import AdamW
from models.fuzzy_cnn import FuzzyCNN

def create_mock_data(batch_size=32, num_samples=100):
    """Create mock binary classification data for testing"""
    # Generate random data similar to MNIST (28x28 grayscale images)
    images = torch.randn(num_samples, 1, 28, 28)
    labels = torch.randint(0, 2, (num_samples,))  # Binary classification
    
    # Create simple data loader
    dataset = torch.utils.data.TensorDataset(images, labels)
    loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)
    
    return loader

def accuracy(logits, targets):
    """Calculate accuracy"""
    with torch.no_grad():
        preds = logits.argmax(dim=1)
        correct = (preds == targets).sum().item()
        return correct / targets.size(0)

def demo_training():
    print("=== Fuzzy Binarization Demo ===")
    print("Creating model...")
    device = torch.device("cpu")  # Use CPU for demo
    model = FuzzyCNN(in_channels=1, num_classes=2, dropout=0.3).to(device)
    optimizer = AdamW(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()
    
    print("Creating mock data...")
    train_loader = create_mock_data(batch_size=32, num_samples=100)
    
    print("Training for 1 epoch...")
    model.train()
    epoch_loss, epoch_acc, n = 0.0, 0.0, 0
    
    for x, y in train_loader:
        x, y = x.to(device), y.to(device)
        optimizer.zero_grad()
        logits = model(x)
        loss = criterion(logits, y)
        loss.backward()
        optimizer.step()
        
        bsz = x.size(0)
        epoch_loss += loss.item() * bsz
        epoch_acc += accuracy(logits, y) * bsz
        n += bsz
    
    avg_loss = epoch_loss / n
    avg_acc = epoch_acc / n
    print(f"Train loss: {avg_loss:.4f}, Train accuracy: {avg_acc:.4f}")
    
    print("Testing model...")
    model.eval()
    test_loader = create_mock_data(batch_size=32, num_samples=50)
    
    test_loss, test_acc, n = 0.0, 0.0, 0
    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device), y.to(device)
            logits = model(x)
            loss = criterion(logits, y)
            
            bsz = x.size(0)
            test_loss += loss.item() * bsz
            test_acc += accuracy(logits, y) * bsz
            n += bsz
    
    avg_test_loss = test_loss / n
    avg_test_acc = test_acc / n
    print(f"Test loss: {avg_test_loss:.4f}, Test accuracy: {avg_test_acc:.4f}")
    print("Fuzzy Binarization demo completed successfully!")

if __name__ == "__main__":
    demo_training()