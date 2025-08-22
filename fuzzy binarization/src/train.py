# src/train.py
import argparse
import torch
from torch import nn
from torch.optim import AdamW
from tqdm import tqdm

from models.fuzzy_cnn import FuzzyCNN
from data import get_loaders, set_random_seeds

def accuracy(logits, targets):
    with torch.no_grad():
        preds = logits.argmax(dim=1)
        correct = (preds == targets).sum().item()
        return correct / targets.size(0)

def train_one_epoch(model, loader, criterion, optimizer, device):
    model.train()
    epoch_loss, epoch_acc, n = 0.0, 0.0, 0
    for x, y in tqdm(loader, desc="Train", leave=False):
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
    return epoch_loss / n, epoch_acc / n

def main():
    parser = argparse.ArgumentParser(description="FuzzyBinarization — train FuzzyCNN")
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--batch_size", type=int, default=128)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    set_random_seeds(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    train_loader = get_loaders(args.batch_size, train=True)
    val_loader = get_loaders(args.batch_size, train=False)

    model = FuzzyCNN(in_channels=1, num_classes=2, dropout=0.3).to(device)
    optimizer = AdamW(model.parameters(), lr=args.lr)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(1, args.epochs + 1):
        tr_loss, tr_acc = train_one_epoch(model, train_loader, criterion, optimizer, device)
        print(f"[Epoch {epoch}/{args.epochs}] train_loss={tr_loss:.4f} train_acc={tr_acc:.4f}")

if __name__ == "__main__":
    main()