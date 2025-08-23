import torch
from src.models.simple_cnn import SimpleCNN


def test_simple_cnn_mnist():
    model = SimpleCNN(num_classes=10)
    input_tensor = torch.randn(1, 1, 28, 28)  # MNIST input shape
    output = model(input_tensor)
    assert output.shape == (1, 10), "Output shape for MNIST should be (1, 10)"


def test_simple_cnn_cifar10():
    model = SimpleCNN(num_classes=10, in_channels=3)
    input_tensor = torch.randn(1, 3, 32, 32)  # CIFAR-10 input shape
    output = model(input_tensor)
    assert output.shape == (1, 10), "Output shape for CIFAR-10 should be (1, 10)"
