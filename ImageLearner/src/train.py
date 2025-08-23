import argparse
import os
import random
import torch
import torchvision
import torchvision.transforms as transforms
from models.simple_cnn import SimpleCNN

def set_seed(seed):
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def load_data(batch_size):
    from torch.utils.data import TensorDataset, DataLoader
    
    # Load mock data
    train_images = torch.load('./data/mock_train_images.pt').float() / 255.0
    train_labels = torch.load('./data/mock_train_labels.pt')
    test_images = torch.load('./data/mock_test_images.pt').float() / 255.0
    test_labels = torch.load('./data/mock_test_labels.pt')
    
    # Add channel dimension and normalize
    train_images = train_images.unsqueeze(1)  # Add channel dimension
    test_images = test_images.unsqueeze(1)    # Add channel dimension
    
    # Normalize to [-1, 1] range  
    train_images = (train_images - 0.5) / 0.5
    test_images = (test_images - 0.5) / 0.5
    
    # Create datasets
    trainset = TensorDataset(train_images, train_labels)
    testset = TensorDataset(test_images, test_labels)
    
    trainloader = DataLoader(trainset, batch_size=batch_size, shuffle=True)
    testloader = DataLoader(testset, batch_size=batch_size, shuffle=False)

    return trainloader, testloader

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
        print(f'Epoch [{epoch + 1}/{epochs}], Loss: {running_loss / len(trainloader):.4f}')

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
    print(f'Accuracy of the model on the test images: {100 * correct / total:.2f}%')

def save_model(model, path):
    torch.save(model.state_dict(), path)

def main():
    parser = argparse.ArgumentParser(description='Train a Simple CNN on MNIST')
    parser.add_argument('--epochs', type=int, default=5, help='Number of epochs to train')
    parser.add_argument('--batch_size', type=int, default=64, help='Batch size for training')
    parser.add_argument('--lr', type=float, default=0.001, help='Learning rate')
    parser.add_argument('--seed', type=int, default=42, help='Random seed for reproducibility')
    args = parser.parse_args()

    set_seed(args.seed)
    trainloader, testloader = load_data(args.batch_size)

    model = SimpleCNN()
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)

    train_model(model, trainloader, criterion, optimizer, args.epochs)
    evaluate_model(model, testloader)
    save_model(model, 'outputs/best.pt')

if __name__ == '__main__':
    main()