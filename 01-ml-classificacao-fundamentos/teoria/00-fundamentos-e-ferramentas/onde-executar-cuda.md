# Onde executar código CUDA

O código CUDA deve ser executado dentro do ambiente virtual que possui PyTorch com suporte CUDA:

    C:\Users\luizs\Documents\Projetos\MLOPS\01-ml-classificacao-fundamentos\.venv\Scripts\python.exe

## 1. No notebook Jupyter

Abra:

    notebooks/01-primeiro-contato-ml-corporativo.ipynb

Crie uma célula e execute:

    import torch

    print("PyTorch:", torch.__version__)
    print("CUDA:", torch.version.cuda)
    print("Disponível:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))

Para executar uma operação na GPU:

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    x = torch.randn(2048, 2048, device=device)
    y = x @ x

    if device.type == "cuda":
        torch.cuda.synchronize()

    print(y.device)

A saída esperada é parecida com:

    cuda:0

No PyCharm, confirme que o kernel do notebook está usando o interpretador do projeto, terminado em:

    .venv/Scripts/python.exe

Depois de trocar a versão CPU pela versão CUDA, reinicie o kernel.

## 2. Em um arquivo Python pelo PyCharm

Crie ou use um arquivo como:

    aplicacao/00-fundamentos-e-ferramentas/07-pytorch/main.py

Conteúdo mínimo:

    import torch

    def main() -> None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        print("PyTorch:", torch.__version__)
        print("CUDA disponível:", torch.cuda.is_available())
        print("Dispositivo:", device)

        if device.type == "cuda":
            print("GPU:", torch.cuda.get_device_name(0))

        x = torch.randn(2048, 2048, device=device)
        y = x @ x

        if device.type == "cuda":
            torch.cuda.synchronize()

        print("Resultado criado em:", y.device)

    if __name__ == "__main__":
        main()

Na configuração Run/Debug do PyCharm:

- Interpreter: o Python dentro de .venv;
- Script path: o caminho completo de main.py;
- Working directory: a raiz 01-ml-classificacao-fundamentos.

## 3. No terminal PowerShell

Abra o terminal na raiz do projeto e execute diretamente o Python do .venv:

    .\.venv\Scripts\python.exe -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"

Ou ative o ambiente primeiro:

    .\.venv\Scripts\Activate.ps1
    python -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"

A saída esperada é:

    True
    NVIDIA GeForce RTX 5070

## 4. Onde colocar o tensor e o modelo?

O tensor e o modelo precisam estar no mesmo dispositivo:

    device = torch.device("cuda")

    X = X.to(device)
    model = model.to(device)

Durante o treinamento:

    for batch_X, batch_y in train_loader:
        batch_X = batch_X.to(device)
        batch_y = batch_y.to(device)

        logits = model(batch_X)
        loss = loss_function(logits, batch_y)

Se o modelo estiver na GPU e os dados na CPU, haverá erro de incompatibilidade de dispositivos.

## 5. CPU versus CUDA

Usar CUDA não significa obrigatoriamente que toda execução será mais rápida. A GPU costuma compensar quando:

- o modelo é maior;
- os batches são maiores;
- existem muitas operações paralelas;
- há muitas épocas;
- os tensores são grandes.

Para operações pequenas, o custo de preparar a GPU pode ser maior que o tempo economizado.

## Resumo

- Notebook: melhor para estudar e visualizar.
- main.py no PyCharm: melhor para organizar uma aplicação.
- PowerShell: melhor para validar rapidamente o ambiente.
- O código deve usar o .venv do projeto.
- Modelo e tensores precisam estar no mesmo device.

## Fonte principal

Documentação oficial do PyTorch sobre CUDA: https://docs.pytorch.org/docs/stable/cuda.html

