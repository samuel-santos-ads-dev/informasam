import os
import platform

def sistema_operacional():
    return platform.system()

def distro():
    return platform.freedesktop_os_release()["PRETTY_NAME"]

def id_distro():
    return platform.freedesktop_os_release().get("ID", "linux").lower()

def kernel():
    return platform.release()

def nome_maquina():
    return platform.node()

def arquitetura():
    return platform.machine()

def processador():
    #abrir o arquivo para leitura e fechar automaticamente
    with open("/proc/cpuinfo", "r") as arquivo:#dando apelido
        for linha in arquivo:#vasculha cada linha do arquivo
            if(linha.startswith("model name")):#verifica se começa com a chave
                #caindo na condição, separa a string pelo separador ":" e pega a segunda opção na lista(indice [1])
                return linha.split(":")[1].strip()
            
def memoria_total():
    with open("/proc/meminfo", "r") as arquivo:
        for linha in arquivo:
            if(linha.startswith("MemTotal")):
                memoria = linha.split()[1]
                return int(memoria) / 1024 / 1024

def memoria_disponivel():
    with open("/proc/meminfo", "r") as arquivo:
        for linha in arquivo:
            if(linha.startswith("MemAvailable")):
                memoria = linha.split()[1]
                return int(memoria) / 1024 / 1024

def memoria_utilizada():
    return memoria_total() - memoria_disponivel()

def nucleos_cpu():
    with open("/proc/cpuinfo", "r") as arquivo:
        for linha in arquivo:
            if(linha.startswith("cpu cores")):
                nucleos = linha.split(":")[1].strip()
                return int(nucleos)

def threads_cpu():
    return os.cpu_count()

def frequencia_cpu():
    with open("/proc/cpuinfo", "r") as arquivo:
        f_por_nucleo = list()
        for linha in arquivo:
            if(linha.startswith("cpu MHz")):
                f_por_nucleo.append(float(linha.split(":")[1].strip()))
        frequemhz = sum(f_por_nucleo) / len(f_por_nucleo)
        frequencia_ghz = frequemhz / 1000
    return frequencia_ghz
