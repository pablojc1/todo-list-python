# ============================================
#   GERENCIADOR DE TAREFAS - Todo List CLI
#   Projeto de portfólio em Python puro
# ============================================

ARQUIVO = "tarefas.txt"


# ---------- FUNÇÕES ----------

def adicionar_tarefa(tarefa):
    """Adiciona uma nova tarefa no arquivo."""
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[ ] {tarefa}\n")
    print(f"\n✓ Tarefa '{tarefa}' adicionada com sucesso!")


def listar_tarefas():
    """Lê e exibe todas as tarefas numeradas."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            tarefas = arquivo.readlines()

        if not tarefas:
            print("\nNenhuma tarefa cadastrada ainda.")
            return []

        print("\n--- Suas tarefas ---")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"  {i}. {tarefa.strip()}")
        print()

        return tarefas

    except FileNotFoundError:
        print("\nNenhuma tarefa ainda. Adicione a primeira!")
        return []


def concluir_tarefa(numero):
    """Marca a tarefa do número informado como concluída."""
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        tarefas = arquivo.readlines()

    if numero < 1 or numero > len(tarefas):
        print("\nNúmero inválido. Tente novamente.")
        return

    if "[X]" in tarefas[numero - 1]:
        print("\nEssa tarefa já está concluída!")
        return

    tarefas[numero - 1] = tarefas[numero - 1].replace("[ ]", "[X]")

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(tarefas)

    print(f"\n✓ Tarefa {numero} marcada como concluída!")


def deletar_tarefa(numero):
    """Remove a tarefa do número informado."""
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        tarefas = arquivo.readlines()

    if numero < 1 or numero > len(tarefas):
        print("\nNúmero inválido. Tente novamente.")
        return

    removida = tarefas.pop(numero - 1)

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(tarefas)

    print(f"\n✓ Tarefa removida: {removida.strip()}")


# ---------- MENU PRINCIPAL ----------

def menu():
    """Loop principal do programa."""
    print("\n====================================")
    print("   GERENCIADOR DE TAREFAS - CLI")
    print("====================================")

    while True:
        print("\nO que você quer fazer?")
        print("  1. Adicionar tarefa")
        print("  2. Listar tarefas")
        print("  3. Concluir tarefa")
        print("  4. Deletar tarefa")
        print("  5. Sair")

        opcao = input("\nEscolha uma opção (1-5): ").strip()

        if opcao == "1":
            tarefa = input("Digite a tarefa: ").strip()
            if tarefa:
                adicionar_tarefa(tarefa)
            else:
                print("Tarefa não pode ser vazia.")

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            tarefas = listar_tarefas()
            if tarefas:
                try:
                    n = int(input("Número da tarefa concluída: "))
                    concluir_tarefa(n)
                except ValueError:
                    print("Digite um número válido.")

        elif opcao == "4":
            tarefas = listar_tarefas()
            if tarefas:
                try:
                    n = int(input("Número da tarefa a deletar: "))
                    deletar_tarefa(n)
                except ValueError:
                    print("Digite um número válido.")

        elif opcao == "5":
            print("\nAté mais! Continue estudando Python. 🚀\n")
            break

        else:
            print("\nOpção inválida. Digite um número de 1 a 5.")


# ---------- PONTO DE ENTRADA ----------

if __name__ == "__main__":
    menu()
