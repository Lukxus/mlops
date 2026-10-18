# Benchmark de CPU versus CUDA

Foi criado o notebook 03-benchmark-cpu-vs-cuda.ipynb para treinar a mesma rede neural com os mesmos dados na CPU e na GPU.

Resultado de uma execução:

| dispositivo | tempo | throughput |
|---|---:|---:|
| CPU | 5,13 s | 62.355 exemplos/s |
| RTX 5070 CUDA | 1,15 s | 277.605 exemplos/s |

A aceleração observada foi aproximadamente:

    5,13 / 1,15 = 4,45x

Esse valor não é uma propriedade fixa da placa. Ele depende de:

- tamanho da rede;
- quantidade de dados;
- tamanho do batch;
- número de épocas;
- transferência de dados entre CPU e GPU;
- precisão numérica;
- versão do PyTorch e driver.

O notebook usa sincronização CUDA para medir a conclusão das operações. Isso é necessário porque chamadas CUDA podem ser assíncronas.

Em modelos pequenos, a GPU pode ser mais lenta por causa do custo de inicialização e transferência. Em workloads maiores e paralelos, a GPU tende a apresentar vantagem maior.

## Fonte principal

Documentação oficial do PyTorch sobre CUDA: https://docs.pytorch.org/docs/stable/cuda.html

