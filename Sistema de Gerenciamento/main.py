from paciente_particular import PacienteParticular
from paciente_convenio import PacienteConvenio


def main():
    print("============================================================")
    print("PACIENTE PARTICULAR")
    print("============================================================")
    paciente1 = PacienteParticular(
        nome="Lucas da Fonseca Tavares",
        data_nascimento="22/11/8007",
        cpf="151.771.88-01",
        telefone="(21) 96614-8834",
        tipo_sanguineo="O+",
        numero_prontuario="P001",
        forma_pagamento="Cartão",
        desconto_fidelidade=0.10
    )
    print("\n-- Informações resumidas --")
    paciente1.exibir_informacoes()
    print("\n-- Informações detalhadas --")
    paciente1.exibir_informacoes(True)
    print("\n-- Atendimento e cálculo de valor --")
    paciente1.registrar_atendimento("Consulta de Rotina", 200.0)
    paciente1.calcular_valor_final(200.0)
    paciente1.calcular_valor_final(200.0, 50.0)

    print("\n" "============================================================")
    print("PACIENTE DO CONVÊNIO")
    print("=" * 60)
    paciente2 = PacienteConvenio(
        nome="Samuel Louven",
        data_nascimento="09/06/2006",
        cpf="167.76.42-08",
        telefone="(21) 98479-2370",
        tipo_sanguineo="A-",
        numero_prontuario="P002",
        nome_convenio="Unimed",
        numero_carteirinha="1222751"
    )
    print("\n-- Informações resumidas --")
    paciente2.exibir_informacoes()
    print("\n-- Informações detalhadas --")
    paciente2.exibir_informacoes(True)
    print("\n-- Atendimento e autorizações --")
    paciente2.registrar_atendimento("Exame de Sangue", 0.0)
    paciente2.registrar_autorizacao("Ressonância Magnética")
    paciente2.registrar_autorizacao("Consulta Cardiológica", 35.0)

    print("\n""============================================================")
    print("Informações dos pacientes em geral")
   
    print("============================================================")
    pacientes = [paciente1, paciente2]
    for p in pacientes:
        p.exibir_informacoes(True)
        print("----------------------------------------")


if __name__ == "__main__":
    main()

