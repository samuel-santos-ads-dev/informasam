import logo
import system_info

def main():
    print("Bem vindo ao InformaSam!")
    logo.exibir_logo()
    print(system_info.sistema_operacional())
    print(system_info.distro())
    print(system_info.kernel())
    print(system_info.nome_maquina())
    print(system_info.arquitetura())
    print(system_info.processador())
    print(round(system_info.memoria_total(), 2))
    print(round(system_info.memoria_disponivel(), 2))
    print(round(system_info.memoria_utilizada(), 2))
    print(system_info.nucleos_cpu())
    print(system_info.threads_cpu())
    print(round(system_info.frequencia_cpu(), 2))

if(__name__ == "__main__"):
    main()