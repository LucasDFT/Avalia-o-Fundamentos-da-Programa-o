from paciente import Paciente


class PacienteParticular(Paciente):

    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo,
                 numero_prontuario, forma_pagamento, desconto_fidelidade=0.0):
        
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self._forma_pagamento = forma_pagamento
        self._desconto_fidelidade = desconto_fidelidade

    @property
    def forma_pagamento(self):
        return self._forma_pagamento

    @property
    def desconto_fidelidade(self):
        return self._desconto_fidelidade

    def calcular_valor_final(self, valor_consulta, taxa_urgencia=0.0):
                
        
        valor_total = valor_consulta + taxa_urgencia
        desconto = self._desconto_fidelidade * valor_consulta
        valor_final = valor_total - desconto

        print(f"Consulta: R$ {valor_consulta:.2f} | Taxa urgência: R$ {taxa_urgencia:.2f} "
              f"| Desconto fidelidade: R$ {desconto:.2f} | Valor final: R$ {valor_final:.2f}")
        return valor_final

    def exibir_informacoes(self, detalhado=False):
        
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Forma de Pagamento: {self._forma_pagamento}")
            print(f"Desconto de Fidelidade: {self._desconto_fidelidade * 100:.0f}%")
