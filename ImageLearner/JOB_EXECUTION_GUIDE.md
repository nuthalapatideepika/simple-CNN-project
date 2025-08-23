# ImageLearner Job Execution Guide

## Overview
This guide explains how to run all the available jobs in the ImageLearner project.

## Available Commands

### 🧹 Code Quality
```bash
# Format code and fix style issues
make fmt

# Check code with linter
make lint
```

### 🧪 Testing
```bash
# Run all tests
make test
```

### 🏃‍♂️ Training
```bash
# Train model with synthetic data (works offline)
make train

# Train with custom parameters
PYTHONPATH=/home/runner/work/AI-projects/AI-projects/ImageLearner python src/train_synthetic.py --epochs 3 --batch_size 64 --lr 0.01
```

### 📊 Performance Metrics
```bash
# Generate performance report
make performance
```

### 🔄 Full CI Pipeline
```bash
# Run complete pipeline: format, lint, test, train, performance
make fmt && make lint && make test && make train && make performance
```

## Output Files

- `outputs/best.pt` - Trained model weights
- `outputs/performance_metrics.json` - Performance metrics in JSON format

## Key Features

✅ **No Internet Required**: Uses synthetic data for training  
✅ **Fast Execution**: Optimized for quick iteration  
✅ **Comprehensive Testing**: Both MNIST and CIFAR-10 model architectures  
✅ **Performance Monitoring**: Detailed metrics collection  
✅ **CI/CD Ready**: All commands work in automated environments  

## Architecture Support

- **MNIST**: 1-channel, 28x28 images
- **CIFAR-10**: 3-channel, 32x32 images  
- **Custom**: Configurable input channels and classes

## Performance Baseline

| Model | Inference Time | Model Size | Parameters |
|-------|---------------|------------|------------|
| MNIST | ~0.33ms | 1.6MB | 421K |
| CIFAR-10 | ~0.40ms | 2.1MB | 545K |

*Note: Metrics measured on CPU, synthetic data used for testing*