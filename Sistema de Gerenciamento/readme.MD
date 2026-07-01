# Estrutura do projeto

```
clinica/
paciente.py              # Superclasse
paciente_particular.py   # Subclasse
paciente_convenio.py     # Subclasse
main.py                  # Ponto de entrada / demonstração de uso
```

Todos os arquivos devem estar na mesma pasta para os imports funcionarem.

# Como executar

```bash
cd clinica
python3 main.py
```

Isso roda a função `main()`, que cria um paciente de cada tipo e testa todos os métodos.

# Classes do sistema

# 1. Paciente (superclasse)

Base do sistema. Básicamente o cadastro que qualquer paciente precisa ter. 

Atributos (todos "privados", prefixo `_`):

 `_nome` (str) - nome completo do paciente
 `_data_nascimento` (str) - data no formato "DD/MM/AAAA"
 `_cpf` (str) - CPF do paciente
 `_telefone` (str) - número de contato
 `_tipo_sanguineo` (str) - ex: "A+", "O-"
 `_numero_prontuario` (str) - identificador único na clínica

Cada atributo tem uma `@property` correspondente (ex: `paciente.nome`), pra não precisar acessar o atributo direto.

Métodos:

- `registrar_atendimento(tipo="Consulta", custo=0.0)`
  Mostra uma mensagem dizendo que o paciente passou por um atendimento. Os parâmetros têm valor padrão, então dá pra chamar de jeitos diferentes:
  ```python
  paciente.registrar_atendimento()
  paciente.registrar_atendimento("Exame")
  paciente.registrar_atendimento("Exame", 150.0)
  ```

 `exibir_informacoes(detalhado=False)`
   False -> mostra só nome, prontuário e tipo sanguíneo
   True -> mostra os 6 atributos

# 2. PacienteParticular (subclasse)

Herda de Paciente (`from paciente import Paciente`). É o paciente que a qual realiza os pagamentos de forma direta para o sistema.

```python
class PacienteParticular(Paciente):
    def __init__(self, ..., forma_pagamento, desconto_fidelidade=0.0):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        ...
```

Atributos adicionais:

 `_forma_pagamento` (str) - ex: "Cartão", "Pix", "Dinheiro"
 `_desconto_fidelidade` (float) - ex: 0.10 = 10% de desconto

Métodos:

 `calcular_valor_final(valor_consulta, taxa_urgencia=0.0)`
  Soma a taxa de urgência (se tiver) ao valor da consulta, aplica o desconto de fidelidade e retorna o valor final:
  ```python
  paciente.calcular_valor_final(200.0)
  paciente.calcular_valor_final(200.0, 50.0)
  ```

 `exibir_informacoes(detalhado=False)`
  Chama `super().exibir_informacoes(detalhado)` e depois acrescenta forma de pagamento e desconto de fidelidade quando detalhado=True.

# 3. PacienteConvenio (subclasse)

Herda de Paciente. Paciente atendido via plano de saúde.

Atributos adicionais:

 `_nome_convenio` (str)  ex: "Unimed", "Amil"
 `_numero_carteirinha` (str) = número da carteirinha do convênio

Métodos:

 `registrar_autorizacao(procedimento, valor_glosa=0.0)`
  Mostra o procedimento autorizado pelo convênio e o valor da glosa (0 quando não tem glosa):
  ```python
  paciente.registrar_autorizacao("Ressonância")
  paciente.registrar_autorizacao("Consulta", 35.0)
  ```

 `exibir_informacoes(detalhado=False)`
  Mesmo esquema da outra subclasse: chama `super()` e acrescenta convênio e número da carteirinha.

# 4. main.py

Importa as duas subclasses e demonstra:

1 - Criação de um PacienteParticular e um PacienteConvenio
2 - Exibição resumida e completa (detalhado=False / True)
3 - Registro de atendimentos
4 - Cálculo de valor final (particular) e autorização de procedimento (convênio)
5 - Polimorfismo: uma lista `pacientes = [paciente1, paciente2]` percorrida em loop, chamando `exibir_informacoes()`

