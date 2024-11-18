| **Sequencia**      | **Link**                                                           | **Descrição**                                                                              |
|-----------------   |-------------------                                                 |--------------------------------------------------------------------                        |
|1.0 - Módulo "OS"   | [1.0 Módulo "OS"](#manual-de-git--github-pratico-e-rápido)         |fornece funcionalidades para interagir com o sistema operacional.                           |
|-----------------   |-------------------                                                 |---------------------------------------------------------------------                       |


## 1.0 - Módulo "`os`" 

O módulo **`os`** fornece funcionalidades para interagir com o sistema operacional. Ele é usado para manipular arquivos, diretórios, variáveis de ambiente e gerenciar processos, de forma independente do sistema operacional.

### Principais funcionalidades do "`os`"
#### 1.1 Manipulação de arquivos e diretórios
- `os.mkdir(path)`: Cria um diretório.
- `os.rmdir(path)`: Remove um diretório vazio.
- `os.remove(file)`: Remove um arquivo.
- `os.rename(src, dst)`: Renomeia arquivos ou diretórios.
- `os.listdir(path)`: Lista arquivos e diretórios em um caminho.
#### 1.2 Trabalhar com caminhos
- `os.path.join(path1, path2)`: Combina caminhos de forma compatível com o SO.
- `os.path.exists(path)`: Verifica se um arquivo ou diretório existe.
- `os.path.isdir(path)`: Verifica se o caminho é um diretório.
- `os.path.isfile(path)`: Verifica se o caminho é um arquivo.

#### 1.3 Gerenciamento de processos
- `os.system(command)`: Executa comandos do sistema.
- `os.getpid()`: Obtém o ID do processo atual.

#### 1.4 Variáveis de ambiente
- `os.environ`: Acessa as variáveis de ambiente do sistema.
- `os.getenv(key, default=None)`: Obtém o valor de uma variável de ambiente.

#### 1.5 Mudança de diretório
- `os.getcwd()`: Obtém o diretório de trabalho atual.
- `os.chdir(path)`: Altera o diretório de trabalho atual.
### Exemplo simples
```python
import os
# Limpa o terminal (clear >> para Linux e Apple | cls >> para Windows)
os.system('cls')

# Cria um diretório
os.mkdir("meu_diretorio")

# Lista o conteúdo do diretório atual
print(os.listdir("."))

# Remove o diretório
os.rmdir("meu_diretorio")
```

