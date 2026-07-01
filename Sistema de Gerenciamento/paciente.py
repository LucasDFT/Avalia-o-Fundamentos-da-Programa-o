class Paciente:

    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario):
        
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._telefone = telefone
        self._tipo_sanguineo = tipo_sanguineo
        self._numero_prontuario = numero_prontuario

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def telefone(self):
        return self._telefone

    @property
    def tipo_sanguineo(self):
        return self._tipo_sanguineo

    @property
    def numero_prontuario(self):
        return self._numero_prontuario

    
    def registrar_atendimento(self, tipo="Consulta", custo=0.0):
       
       
        print(f"{self._nome} passou por um atendimento do tipo '{tipo}', "
              f"com custo de R$ {custo:.2f}.")

    def exibir_informacoes(self, detalhado=False):
       
        if not detalhado:
            print(f"Nome: {self._nome} | Prontuário: {self._numero_prontuario} "
                  f"| Tipo Sanguíneo: {self._tipo_sanguineo}")
        else:
            print(f"Nome: {self._nome}")
            print(f"Data de Nascimento: {self._data_nascimento}")
            print(f"CPF: {self._cpf}")
            print(f"Telefone: {self._telefone}")
            print(f"Tipo Sanguíneo: {self._tipo_sanguineo}")
            print(f"Número do Prontuário: {self._numero_prontuario}")
