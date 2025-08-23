#!/usr/bin/env python3
"""
Demo script to show ImageLearner works without network dependencies
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import torch
import torch.nn as nn
from models.simple_cnn import SimpleCNN

def create_mock_data(batch_size=32, num_samples=100):
    """Create mock MNIST-like data for testing"""
    # Generate random data similar to MNIST (28x28 grayscale images)
    images = torch.randn(num_samples, 1, 28, 28)
    labels = torch.randint(0, 10, (num_samples,))
    
    # Create simple data loader
    dataset = torch.utils.data.TensorDataset(images, labels)
    loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)
    
    return loader

def demo_training():
    print("=== ImageLearner Demo ===")
    print("Creating model...")
    model = SimpleCNN(num_classes=10)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    print("Creating mock data...")
    train_loader = create_mock_data(batch_size=32, num_samples=100)
    
    print("Training for 1 epoch...")
    model.train()
    total_loss = 0
    num_batches = 0
    
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        num_batches += 1
    
    avg_loss = total_loss / num_batches
    print(f"Average loss: {avg_loss:.4f}")
    
    print("Testing model...")
    model.eval()
    test_loader = create_mock_data(batch_size=32, num_samples=50)
    
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    accuracy = 100 * correct / total
    print(f"Test accuracy: {accuracy:.2f}%")
    print("ImageLearner demo completed successfully!")

if __name__ == "__main__":
    demo_training()