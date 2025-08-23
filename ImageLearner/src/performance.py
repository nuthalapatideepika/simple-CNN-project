#!/usr/bin/env python3
"""
Performance monitoring script for ImageLearner
This simulates performance metrics collection that could be used in CI/CD
"""

import time
import json
import torch
import os
from src.models.simple_cnn import SimpleCNN


def measure_inference_time(model, input_shape, num_runs=100):
    """Measure model inference time"""
    model.eval()
    input_tensor = torch.randn(*input_shape)

    # Warmup
    for _ in range(10):
        with torch.no_grad():
            _ = model(input_tensor)

    # Measure
    start_time = time.time()
    for _ in range(num_runs):
        with torch.no_grad():
            _ = model(input_tensor)
    end_time = time.time()

    avg_time = (end_time - start_time) / num_runs
    return avg_time * 1000  # Return in milliseconds


def measure_model_size(model):
    """Measure model size in MB"""
    torch.save(model.state_dict(), "temp_model.pt")
    size_bytes = os.path.getsize("temp_model.pt")
    os.remove("temp_model.pt")
    return size_bytes / (1024 * 1024)  # Return in MB


def count_parameters(model):
    """Count total and trainable parameters"""
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return total_params, trainable_params


def generate_performance_report():
    """Generate performance metrics report"""
    print("🚀 ImageLearner Performance Metrics")
    print("=" * 40)

    # Test MNIST model
    mnist_model = SimpleCNN(num_classes=10, in_channels=1)
    mnist_inference_time = measure_inference_time(mnist_model, (1, 1, 28, 28))
    mnist_size = measure_model_size(mnist_model)
    mnist_total_params, mnist_trainable_params = count_parameters(mnist_model)

    # Test CIFAR-10 model
    cifar_model = SimpleCNN(num_classes=10, in_channels=3)
    cifar_inference_time = measure_inference_time(cifar_model, (1, 3, 32, 32))
    cifar_size = measure_model_size(cifar_model)
    cifar_total_params, cifar_trainable_params = count_parameters(cifar_model)

    # Performance metrics
    metrics = {
        "models": {
            "mnist": {
                "inference_time_ms": round(mnist_inference_time, 3),
                "model_size_mb": round(mnist_size, 3),
                "total_parameters": mnist_total_params,
                "trainable_parameters": mnist_trainable_params,
                "input_shape": [1, 1, 28, 28],
            },
            "cifar10": {
                "inference_time_ms": round(cifar_inference_time, 3),
                "model_size_mb": round(cifar_size, 3),
                "total_parameters": cifar_total_params,
                "trainable_parameters": cifar_trainable_params,
                "input_shape": [1, 3, 32, 32],
            },
        },
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "device": "cpu",
    }

    # Print metrics
    print("📊 MNIST Model:")
    print(f"   • Inference time: {mnist_inference_time:.3f} ms")
    print(f"   • Model size: {mnist_size:.3f} MB")
    print(
        f"   • Parameters: {mnist_total_params:,} total, {mnist_trainable_params:,} trainable"
    )
    print()
    print("📊 CIFAR-10 Model:")
    print(f"   • Inference time: {cifar_inference_time:.3f} ms")
    print(f"   • Model size: {cifar_size:.3f} MB")
    print(
        f"   • Parameters: {cifar_total_params:,} total, {cifar_trainable_params:,} trainable"
    )
    print()

    # Save JSON report
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/performance_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("💾 Performance metrics saved to outputs/performance_metrics.json")
    print("✅ Performance evaluation completed!")

    return metrics


if __name__ == "__main__":
    generate_performance_report()
