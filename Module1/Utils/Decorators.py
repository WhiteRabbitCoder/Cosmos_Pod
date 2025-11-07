COLORS = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "reset": "\033[0m",
}

def color(text: str, name: str) -> str:
    #Devuelve text envuelto con el color indicado (name: red/green/yellow/...).
    return f"{COLORS.get(name, COLORS['reset'])}{text}{COLORS['reset']}"
