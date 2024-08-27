from datetime import datetime

def exibir_menu():
    return input("\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[ed] Extrato Detalhado\n[q] Sair\n=> ")

def registrar_movimentacao(tipo, valor):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{data_hora} - {tipo}: R$ {valor:.2f}\n"

def mostrar_saldo(valor, saldo, tipo):
    print(f"{tipo} de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {saldo:.2f}\n")

def ler_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido! Por favor, insira um número válido.")

def realizar_deposito(saldo, extrato):
    valor = ler_valor("Informe o valor do depósito: ")
    if valor > 0:
        saldo += valor
        extrato += registrar_movimentacao("Depósito", valor)
        mostrar_saldo(valor, saldo, "Depósito")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def realizar_saque(saldo, extrato, saques, limite, LIMITE_SAQUES):
    valor = ler_valor("Informe o valor do saque: ")
    if valor <= 0 or valor > saldo or valor > limite or saques >= LIMITE_SAQUES:
        print("Operação falhou! Verifique os valores e tente novamente.")
    else:
        saldo -= valor
        extrato += registrar_movimentacao("Saque", valor)
        mostrar_saldo(valor, saldo, "Saque")
        saques += 1
    return saldo, extrato, saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================\n"
          f"{extrato if extrato else 'Não foram realizadas movimentações.'}"
          f"\nSaldo: R$ {saldo:.2f}\n==========================================")

def exibir_extrato_detalhado(saldo, extrato):
    print("\n=========== EXTRATO DETALHADO ===========")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    status_saldo = "positivo" if saldo >= 0 else "negativo"
    print(f"\nSaldo: R$ {saldo:.2f} ({status_saldo})")
    print("==========================================")

def main():
    saldo, extrato, saques = 0.0, "", 0
    LIMITE_SAQUES, limite = 3, 500.0
    
    while (opcao := exibir_menu()) != "q":
        if opcao == "d":
            saldo, extrato = realizar_deposito(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, saques = realizar_saque(saldo, extrato, saques, limite, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "ed":
            exibir_extrato_detalhado(saldo, extrato)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()