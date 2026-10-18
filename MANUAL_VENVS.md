# Manual de ambientes virtuais Python

Este manual define como criar, usar e reproduzir ambientes virtuais Python neste repositório.

## Convenção do projeto

Use um ambiente virtual por projeto, e não um ambiente por biblioteca ou por exercício.

Para o projeto de fundamentos de Machine Learning, o ambiente deve ficar em:

```text
01-ml-classificacao-fundamentos/.venv/
```

As pastas de exercícios compartilham esse ambiente porque fazem parte do mesmo projeto.

Nunca versione a pasta `.venv/`. Ela é local e pode ser recriada a partir do arquivo de dependências.

## Criar um ambiente no Windows PowerShell

Entre na raiz do projeto:

```powershell
cd C:\Users\luizs\Documents\Projetos\MLOPS\01-ml-classificacao-fundamentos
```

Crie e ative o ambiente:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Depois da ativação, o prompt normalmente exibirá `(.venv)`.

## Instalar dependências

Com o ambiente ativado:

```powershell
python -m pip install --upgrade pip
python -m pip install -r .\aplicacao\00-fundamentos-e-ferramentas\requirements.txt
```

Use `python -m pip` para garantir que o instalador pertence ao mesmo Python usado para executar os scripts.

## Confirmar o Python ativo

```powershell
python -c "import sys; print(sys.executable)"
python -m pip list
```

O caminho esperado deve conter:

```text
01-ml-classificacao-fundamentos\.venv\Scripts\python.exe
```

## Executar um exercício

```powershell
python .\aplicacao\00-fundamentos-e-ferramentas\01-python-para-ml\main.py
```

## Configurar o Jupyter

Dentro do ambiente virtual:

```powershell
python -m pip install ipykernel
python -m ipykernel install --user `
  --name ml-classificacao `
  --display-name "Python (ml-classificacao)"
```

No notebook, selecione o kernel `Python (ml-classificacao)`.

## Sair do ambiente

Execute:

```powershell
deactivate
```

## Recriar o ambiente em outra máquina

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r .\aplicacao\00-fundamentos-e-ferramentas\requirements.txt
```

O ambiente não é compartilhado pelo Git. O arquivo de dependências versionado é o que permite reinstalá-lo.

## Registrar versões exatas

Para salvar um snapshot das versões instaladas:

```powershell
python -m pip freeze > requirements-lock.txt
```

O `requirements.txt` deve continuar representando as dependências diretas do projeto. O `requirements-lock.txt` pode ser usado para reproduzir exatamente o ambiente:

```powershell
python -m pip install -r .\requirements-lock.txt
```

Não crie um ambiente separado para cada biblioteca. Crie outro ambiente quando houver outro projeto, conflito de versões ou requisitos específicos de execução.

## Problemas comuns

### O PowerShell bloqueia a ativação

Confira a política atual:

```powershell
Get-ExecutionPolicy -List
```

Como alternativa, execute diretamente o Python do ambiente:

```powershell
.\.venv\Scripts\python.exe .\caminho\para\main.py
```

### O notebook não encontra uma biblioteca

Confirme o interpretador ativo e se o notebook está usando o kernel `Python (ml-classificacao)`:

```powershell
python -c "import sys; print(sys.executable)"
```

### O ambiente ficou inconsistente

Recrie somente a pasta `.venv` do projeto:

```powershell
deactivate
Remove-Item -LiteralPath .\.venv -Recurse -Force
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r .\aplicacao\00-fundamentos-e-ferramentas\requirements.txt
```
