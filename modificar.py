from Pacientes_Constante import Pacientes_constantes

# Carga los datos iniciales de los pacientes
pacientes = Pacientes_constantes()

informacion_pacientes = {}
def registro_pacientes (): 
    print("----------GESTOR DE INFORMACION DE LOS PACIENTES----------------- ")

    identificacion = input(" Por favor digite ID sin puntos ni comas => ")
    if identificacion == Pacientes_constantes :
     print ("El paciente se encuentra registrado ")
    else :
        identificacion  not in  pacientes.keys()
        print("-------------Paciente nuevo, por favor ingrese los siguientes datos------------------")
        
       # identificacion  not in  pacientes.keys()

    nombre = input("Por favor digite nombre completo => ")
    edad = -1 
    while edad < 0 or edad > 120:
        try:
            edad =  int(input("Por favor digite edad (Entre 0 y 120)=> "))
            if edad < 0 or edad > 120:
                raise ValueError   
        except ValueError:
            print ("-------------ATENCION : Edad fuera de rango, por favor ingrese una edad valida-------------")

    diagnostico = input("Por favor digite diagnostico => ")
    historial = input(" Consultar historial de paciente ") 
    # Manejar el historial como una lista no cmo un str
    
    pacientes[identificacion] = {
        "nombre": nombre,
        "edad": edad,
        "diagnostico": diagnostico,
        "historial": historial
    }

registro_pacientes ()


    #print (f" Paciente registrado con el siguente ID: {identificacion}")
print(pacientes)

print("---------- DATOS INGRESADOS CON EXITO -----------------------------")