🌎 Idiomas / Languages:  

[Español](README.md) | [English](README.en.md)

---

# 🛡️ Gerador de Senhas Seguras

Um gerador de senhas desenvolvido em **Python com Tkinter**, que permite criar senhas seguras e personalizadas de forma simples.

---

## ✨ Características

- ✅ Interface gráfica amigável com Tkinter.
- ✅ Permite incluir/excluir:
  - Letras maiúsculas
  - Letras minúsculas
  - Números
  - Caracteres especiais
- ✅ Controle de comprimento mínimo (8 caracteres).
- ✅ Geração aleatória usando a biblioteca **`secrets`** (segura para criptografia).
- ✅ Botão para copiar para a área de transferência com **pyperclip**.

---

## 🚀 Requisitos

- [Python 3.8+](https://www.python.org/downloads/)  
- Bibliotecas necessárias:  
  - tkinter (incluso por padrão no Python)  
  - pyperclip
    
- Recomenda-se criar um ambiente virtual para instalar as dependências sem afetar o seu sistema:

```bash
python -m venv .venv          #Criar o ambiente virtual
```

## 🛠️ Ativar o ambiente virtual

Windows
```bash
.venv\Scripts\activate
```

Linux/macOS
```bash
source .venv/bin/activate
```

Instalar dependências
```bash
pip install -r requirements.txt
```

---

## ▶️ Execução
Clone o repositório e execute o script:

```bash
python generador_contraseñas.py
```

Você verá uma janela gráfica onde poderá:

- Selecionar as opções da senha.
- Ajustar o comprimento.
- Gerar e copiar com um clique.

---

## 📸 Captura de tela (exemplo)

![Gerador de senhas](https://github.com/albertoh88/generador_de_contrasenhas/blob/main/generador_de_contrasenhas.png)

---

## 💡 Ideias de melhoria

- Salvar histórico de senhas geradas.
- Adicionar um medidor de "força" da senha.
- Exportar senhas para um arquivo criptografado.
- Criar um executável (.exe) para usuários sem Python.
