# Energy Guard ⚡️

O **Energy Guard** é um sistema CLI (Command Line Interface) desenvolvido em Python puro (sem bibliotecas externas) para ajudar famílias e empresas a gerenciar, calcular as contas e otimizar o consumo de energia elétrica de seus equipamentos.

## 🚀 Funcionalidades

### 👤 Painel do Usuário
- **Adicionar/Remover Equipamentos:** Controle exatamente o que você tem em casa (TVs, Geladeiras, Ar Condicionado, etc).
- **Ver Meu Consumo:** Visualize instantaneamente o gasto em Watts (instantâneo) e a projeção em kWh mensal!
- **Solicitar Novos Itens:** Não encontrou o seu equipamento no sistema? Envie uma notificação diretamente para os Administradores!

### ⚙️ Painel do Administrador
- **Gestão de Usuários:** Crie novas contas validando o CEP e senha forte, liste, apague contas (e seu histórico) e promova outros usuários a Administradores do sistema.
- **Gestão de Catálogo (Dinâmico):** Adicione ou remova equipamentos base do banco de dados para todos os moradores em tempo real.
- **Visualizar Solicitações:** Leia e apague solicitações de inclusão de novos equipamentos feitas pelos moradores da casa.
- **Relatórios Gerenciais:** Veja quem é o "ranking" de maior gastador do sistema e a contagem global de tudo que está conectado à rede elétrica.

---

## 🛠 Estrutura do Projeto

A arquitetura do projeto foi desenvolvida para ser robusta e dividida em camadas lógicas (MVC):

```text
energy_guard/
├── main.py                 # Ponto de Entrada / Interface principal do Terminal
├── database/               # Camada de Dados (NoSQL JSON-based)
│   ├── base_equipment.json # Catálogo global de equipamentos (Editável via Admin)
│   ├── equipment.json      # Relação de equipamentos possuídos pelos usuários
│   ├── users.json          # Perfis de acesso, senhas e endereços
│   ├── requests.json       # Solicitações pendentes dos usuários
│   └── json_handler.py     # Controlador de E/S dos arquivos persistentes
├── services/               # Camada de Controller / Lógica de Negócios 
│   ├── auth_service.py     # Controlador de Login Autenticado
│   ├── admin_service.py    # Funcionalidades exclusivas da Direção
│   └── user_service.py     # Cadastro de posse e requisições
└── utils/                  # Camada Utilitária / Ferramentas de Suporte
    ├── calculator.py       # Algoritmos de Conversão (Watts -> kWh)
    ├── validators.py       # Regex Patterns (E-mail, CEP Brasileiro e Senha Forte)
    └── limpeza_tela.py     # Multi-platform Console Clear (Windows/Mac/Linux)
```

---

## 💻 Como Executar

**Pré-requisitos:** O software requer apenas a instalação do **Python 3**. Nenhuma biblioteca externa (`pip install`) é necessária! O código é nativo e interativo, rodando de forma unificada no **Windows, Mac OS e Linux**.

1. Faça o download desta pasta.
2. Abra o seu Terminal / Prompt de Comando e navegue até a raiz do projeto (onde está o `main.py`).
   ```bash
   cd caminho/para/A-Pasta/energy_guard
   ```
3. Inicie o sistema chamando o arquivo de execução:
   ```bash
   python main.py
   ```
   *(Dependendo do sistema ou da versão instalada, utilize `python3 main.py`)*

---

### 🔑 Primeiros Passos
Por padrão, caso seja um clone novo do repositório, faça login com o usuário mestre (Raiz) para realizar o setup da sua empresa/residência:
- **E-mail:** `admin@gmail.com`
- **Senha:** `admin`

*(A partir deste login temporário, você pode criar e promover novos administradores com senhas mais avançadas).*

---
✅ **Nota sobre Persistência**: Ao longo do uso, não se preocupe em desligar o terminal. A arquitetura de Data Management garante que cada alteração será salva nos arquivos do diretório `/database` perfeitamente em string codificada (`utf-8`). Guardou, tá guardado!
