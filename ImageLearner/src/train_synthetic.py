#!/usr/bin/env python3
"""
Test training script that works without internet connection
"""

import argparse
import os
import random
import torch
import torch.nn as nn
import torch.utils.data as data
from models.simple_cnn import SimpleCNN


def set_seed(seed):
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def create_synthetic_dataset(batch_size, num_samples=1000):
    """Create synthetic MNIST-like dataset for testing"""
    # Create synthetic data that looks like MNIST
    X = torch.randn(num_samples, 1, 28, 28)
    y = torch.randint(0, 10, (num_samples,))

    dataset = data.TensorDataset(X, y)
    loader = data.DataLoader(dataset, batch_size=batch_size, shuffle=True)
    return loader


def train_model(model, trainloader, criterion, optimizer, epochs):
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for images, labels in trainloader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(
            f"Epoch [{epoch + 1}/{epochs}], Loss: {running_loss / len(trainloader):.4f}"
        )


def evaluate_model(model, testloader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in testloader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print(f"Accuracy of the model on the test images: {100 * correct / total:.2f}%")


def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    torch.save(model.state_dict(), path)
    print(f"Model saved to {path}")


def main():
    parser = argparse.ArgumentParser(description="Train a Simple CNN on synthetic data")
    parser.add_argument(
        "--epochs", type=int, default=5, help="Number of epochs to train"
    )
    parser.add_argument(
        "--batch_size", type=int, default=64, help="Batch size for training"
    )
    parser.add_argument("--lr", type=float, default=0.001, help="Learning rate")
    parser.add_argument(
        "--seed", type=int, default=42, help="Random seed for reproducibility"
    )
    args = parser.parse_args()

    set_seed(args.seed)

    # Create synthetic datasets
    trainloader = create_synthetic_dataset(args.batch_size, num_samples=1000)
    testloader = create_synthetic_dataset(args.batch_size, num_samples=200)

    model = SimpleCNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)

    print("Starting training with synthetic data...")
    train_model(model, trainloader, criterion, optimizer, args.epochs)
    evaluate_model(model, testloader)
    save_model(model, "outputs/best.pt")
    print("Training completed successfully!")


if __name__ == "__main__":
    main()
