# API-REST-with-Flask

Uma API REST simples escrita em **Python**, utilizando o framework **Flask**.  
Este projeto serve como exemplo ou ponto de partida para construir APIs pequenas e modulares.

---

## 🔍 Visão Geral

- Linguagem: **Python**
- Framework web: **Flask**
- Estrutura modular (separando `models`, rotas, etc.)
- Inclui testes básicos
- Gerenciamento de dependências via `requirements.txt`

---

## 📁 Estrutura do Projeto

```
API-REST-with-Flask/
│
├── app.py
├── models/
│   └── … (arquivos de modelo, por exemplo, definição de entidades, ORM, etc.)
├── requirements.txt
├── tests.py
└── .gitignore
```

**Descrição rápida dos principais arquivos:**

- **app.py** — aplicação Flask principal, definição de rotas e inicialização  
- **models/** — modelos de dados e lógica do domínio  
- **tests.py** — testes automatizados  
- **requirements.txt** — dependências do projeto  

---

## 🚀 Como começar / Instalação

### Pré-requisitos

- Python **3.x** instalado  
- (Opcional) Ambiente virtual — `venv`, `virtualenv` ou `conda`

### Passos iniciais

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/MiguelOlivieira/API-REST-with-Flask.git
   cd API-REST-with-Flask
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```


4. **Execute a aplicação:**
   ```bash
   flask run
   ```
   Ou:
   ```bash
   python app.py
   ```

5. **Acesse a API:**  
   `http://localhost:5000`

---

## 🧩 Rotas / Endpoints


| Método | Rota           | Descrição                   |
|--------|----------------|-----------------------------|
| GET    | `/tasks`       | Lista todas as tasks        |
| GET    | `/tasks/<id>`  | Recupera uma task por ID    |
| POST   | `/tasks`       | Cria uma nova task          |
| PUT    | `/tasks/<id>`  | Atualiza uma task existente |
| DELETE | `/tasks/<id>`  | Remove uma task por ID      |

**Exemplo de requisição:**

```bash
curl -X POST http://localhost:5000/tasks      -H "Content-Type: application/json"      -d '{"title": "Exemplo", "description": "descrição"}'
```

---

## ✅ Testes

Execute os testes automatizados com:

```bash
pytest tests.py
```

Ou:

```bash
python -m unittest discover
```

Verifique se todos os casos principais (sucesso, falha, entradas inválidas) estão cobertos.

---

## 🧮 Dependências

As dependências estão listadas em `requirements.txt`.  
Pacotes comuns esperados:

- **Flask**  
- **Werkzeug**  
- **pytest** (ou outro ORM)  
- **requests** ou **unittest**

---

## 📝 Licença

Este projeto está licenciado sob a **MIT License**.  
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Sinta-se à vontade para abrir *issues* ou *pull requests* com dúvidas, sugestões ou melhorias.

---
