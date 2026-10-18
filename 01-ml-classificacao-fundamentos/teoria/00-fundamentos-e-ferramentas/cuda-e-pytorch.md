# CUDA e PyTorch

CUDA é a plataforma da NVIDIA que permite executar operações de computação paralela na GPU. No PyTorch, o fluxo usual é escolher um dispositivo e mover modelo e tensores para ele:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
batch_X = batch_X.to(device)
```

O ganho tende a aparecer em modelos maiores, lotes maiores e operações com muita multiplicação de matrizes. Para um dataset pequeno, o custo de inicializar a GPU e transferir dados pode superar o benefício.

O notebook `notebooks/01-primeiro-contato-ml-corporativo.ipynb` inclui um benchmark sintético que compara o tempo de um treino em CPU e CUDA quando a GPU estiver disponível.

## Estado atual do projeto

O ambiente atual reporta:

```text
torch = 2.14.1+cpu
torch.cuda.is_available() = False
```

Isso significa que o PyTorch instalado é CPU-only. A placa RTX 5070 não será utilizada até que seja instalado um build do PyTorch com CUDA compatível e o driver NVIDIA esteja adequado.

A instalação deve ser feita usando o comando gerado pelo seletor oficial do PyTorch para Windows, Python e a versão CUDA recomendada. Não se deve escolher um wheel CUDA arbitrariamente.

Fonte: https://pytorch.org/get-started/locally/
