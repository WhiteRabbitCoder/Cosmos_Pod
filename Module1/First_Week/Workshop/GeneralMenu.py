"""
Menú general para el taller de la primera semana del módulo 1 en Cosmos Pod.
Incluye opciones para ejecutar diferentes ejercicios y prácticas.
"""

while True:
    print("\n\n1. Menu del primer nivel del taller")
    print("2. Menu del segundo nivel del taller")
    print("3. Menu del tercer nivel del taller")
    print("4. Menu del cuarto nivel del taller")
    print("5. Menu del quinto nivel del taller")
    print("0. Salir")
    choice = input("Selecciona una opción: ")
    match choice:
        case "1":
            from Cosmos_Pod.Module1.First_Week.Workshop.Level1 import level_one_menu
        case "2":
            from Cosmos_Pod.Module1.First_Week.Workshop.Level2 import level_two_menu
        case "3":
            from Cosmos_Pod.Module1.First_Week.Workshop.Level3 import level_three_menu
        case "4":
            from Cosmos_Pod.Module1.First_Week.Workshop.Level4 import level_four_menu
        case "5":
            from Cosmos_Pod.Module1.First_Week.Workshop.Level5 import level_five_menu
        case "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Intenta de nuevo.")
