# 🔐 Gerador de Senhas Seguras 3000

Um script em Python que gera opções de senhas fortes e aleatórias, com validação de tamanho mínimo e uso de biblioteca criptograficamente segura.

## 🚀 Funcionalidades

* **Validação de Entrada:** Não aceita senhas com menos de 8 caracteres, pedindo um novo valor até que o tamanho seja válido (loop `while`).
* **Sorteio Seguro:** Usa o módulo `secrets`, próprio para dados sensíveis como senhas, em vez do `random`, que é previsível e não recomendado para segurança.
* **Composição Forte:** Combina letras maiúsculas, minúsculas, números e símbolos usando o módulo `string`.
* **3 Opções de Senha:** Gera três senhas diferentes para o usuário escolher, usando loops aninhados (`for` dentro de `for`).
* **Experiência de Uso:** Mensagens com pausas usando o módulo `time`, simulando carregamento.

## 🛠️ Tecnologias Utilizadas

* Python 3 (`secrets`, `string`, `time`)
* Git & GitHub

## 🏁 Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório:

```bash
git clone https://github.com/cahponto/gerador-senhas-python.git
```

3. Acesse a pasta do projeto:

```bash
cd gerador-senhas-python
```

4. Execute o gerador:

```bash
python gerador.py
```

## 🗺️ Próximos Passos

* Perguntar se o usuário gostou das opções e gerar novas caso não tenha gostado.