"""Regressão linear mínima com tensores e autograd em PyTorch."""

import torch


def main() -> None:
    torch.manual_seed(42)
    x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
    y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

    model = torch.nn.Linear(1, 1)
    loss_function = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.05)

    for _ in range(200):
        predictions = model(x)
        loss = loss_function(predictions, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print("Peso aprendido:", model.weight.item())
    print("Bias aprendido:", model.bias.item())
    print("Loss final:", loss.item())


if __name__ == "__main__":
    main()
