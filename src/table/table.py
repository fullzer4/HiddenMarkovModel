class Table():
    def __init__(self) -> None:
        self.table = [] # tabuleiro tudo com 0 para vazio 1 para navio e x para lugar atingido
        self.ships = {
            "Porta-avioes": (1, 5), # quantidade e o espaco que ocupa
            "Navios-tanque": (2, 4),
            "Contratorpedeiros": (3, 3),
            "Submarinos": (4, 2)
        } # dentro desse objeto vai ter todos os navios
