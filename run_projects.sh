#!/usr/bin/env bash
# run_projects.sh - Script to run both AI projects

set -e  # Exit on any error

echo "==================================="
echo "Running AI Projects"
echo "==================================="

echo ""
echo "📊 Setting up mock data (if needed)..."

# Create mock data for testing (since real MNIST download requires network access)
python3 -c "
import os
import torch
import numpy as np

def create_mock_mnist_data(data_dir, train=True):
    os.makedirs(data_dir, exist_ok=True)
    if train:
        num_samples = 1000
        filename_prefix = 'train'
    else:
        num_samples = 200
        filename_prefix = 'test'
    
    images = torch.randint(0, 256, (num_samples, 28, 28), dtype=torch.uint8)
    labels = torch.randint(0, 10, (num_samples,), dtype=torch.long)
    
    torch.save(images, os.path.join(data_dir, f'mock_{filename_prefix}_images.pt'))
    torch.save(labels, os.path.join(data_dir, f'mock_{filename_prefix}_labels.pt'))

# Create for both projects
for project in ['ImageLearner', 'fuzzy binarization']:
    data_dir = os.path.join(project, 'data')
    create_mock_mnist_data(data_dir, train=True)
    create_mock_mnist_data(data_dir, train=False)

print('Mock datasets created successfully!')
"

echo ""
echo "🧠 Running ImageLearner (CNN for Image Understanding)..."
echo "-----------------------------------"
cd "ImageLearner"
make train
cd ..

echo ""
echo "🔬 Running Fuzzy Binarization (FuzzyCNN)..."
echo "-----------------------------------"
cd "fuzzy binarization"
make train
cd ..

echo ""
echo "✅ Both projects completed successfully!"
echo ""
echo "Project outputs:"
echo "- ImageLearner: outputs/best.pt (model weights)"
echo "- Fuzzy Binarization: Training completed with accuracy metrics"