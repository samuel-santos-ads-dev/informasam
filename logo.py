
import system_info
import colors


LOGOS = {
    "debian": [
        "       .-::::-.",
        "     .'  .--.  '.",
        "    /  .'    '.  \\",
        "   |  |  .--.  |  |",
        "    \\  '.____.' /",
        "     '._      _.'",
        "        DEBIAN"
    ],

    "ubuntu": [
        "       .-======-.",
        "     .'  o    o  '.",
        "    /  .--------.  \\",
        "   | o |        | o |",
        "    \\  '--------'  /",
        "     '.  o    o  .'",
        "        UBUNTU"
    ],

    "fedora": [
        "       .--------.",
        "       |  _____ |",
        "       | |  ____|",
        "       | | |____",
        "       | |_____ |",
        "       |_______|",
        "        FEDORA"
    ],

    "arch": [
        "          /\\",
        "         /  \\",
        "        / /\\ \\",
        "       / /  \\ \\",
        "      / /____\\ \\",
        "     /__________\\",
        "         ARCH"
    ],

    "archlinux": [
        "          /\\",
        "         /  \\",
        "        / /\\ \\",
        "       / /  \\ \\",
        "      / /____\\ \\",
        "     /__________\\",
        "         ARCH"
    ],

    "linuxmint": [
        "      .--------.",
        "      |        |",
        "      | |\\  /| |",
        "      | | \\/ | |",
        "      | |    | |",
        "      | '----' |",
        "       LINUX MINT"
    ],

    "pop": [
        "     ____________",
        "    |  ________  |",
        "    | |        | |",
        "    | |  ____  | |",
        "    | | |    | | |",
        "    | |______| | |",
        "       POP!_OS"
    ],

    "biglinux": [
        "      .--------.",
        "     /  ______  \\",
        "    |  |      |  |",
        "    |  |      |  |",
        "    |  |______|  |",
        "     \\__________/",
        "       BIGLINUX"
    ],

    "zorin": [
        "      __________",
        "     /  ______  \\",
        "    |  /      \\  |",
        "    | |  ____  | |",
        "    |  \\______/  |",
        "     \\__________/",
        "       ZORIN OS"
    ],

    "kali": [
        "        /\\",
        "       /  \\___",
        "      /  _    \\",
        "     |  / \\   |",
        "      \\ \\_/  /",
        "       \\____/",
        "      KALI LINUX"
    ],

    "opensuse": [
        "      .--------.",
        "     /  .----.  \\",
        "    |  /      \\  |",
        "    | |  o  o  | |",
        "     \\ \\______/ /",
        "      '--------'",
        "       openSUSE"
    ]
}


CORES_LOGOS = {
    "debian": [colors.vermelho],
    "ubuntu": [colors.amarelo, colors.branco],
    "fedora": [colors.azul, colors.branco],
    "arch": [colors.ciano],
    "archlinux": [colors.ciano],
    "linuxmint": [colors.verde],
    "pop": [colors.azul, colors.ciano],
    "biglinux": [colors.azul, colors.amarelo],
    "zorin": [colors.azul, colors.ciano],
    "kali": [colors.azul, colors.branco],
    "opensuse": [colors.verde]
}


ALIASES = {
    "pop_os": "pop",
    "pop-os": "pop",
    "opensuse-leap": "opensuse",
    "opensuse-tumbleweed": "opensuse"
}


def obter_identificador():
    identificador = system_info.id_distro()
    return ALIASES.get(identificador, identificador)


def exibir_logo():
    identificador = obter_identificador()

    return LOGOS.get(
        identificador,
        [
            "      .--------.",
            "      |  LINUX |",
            "      '--------'",
            "           >_"
        ]
    )


def colorir_linha(linha, indice):
    identificador = obter_identificador()
    paleta = CORES_LOGOS.get(identificador, [colors.branco])
    cor = paleta[indice % len(paleta)]

    return cor + linha + colors.reset
