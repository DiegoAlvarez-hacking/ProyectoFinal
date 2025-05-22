# Arreglo que cumple como "Base de datos"
empleados = {
    '001': {'nombre': 'Diego Alvarez', 'saldo_vacaciones': 15},
    '002': {'nombre': 'Jhoannes Jurado', 'saldo_vacaciones': 20},
    '003': {'nombre': 'Cesar Soto', 'saldo_vacaciones': 20},
    # Agregar más empleados según sea necesario
}

# Credenciales de acceso al sistema
usuario_permitido = "recursoshumanos"
contraseña_admin = "admin123"

# Función para mostrar el saldo actual de vacaciones de un empleado
def saldo_vacaciones_empleado(codigo_empleado):
    if codigo_empleado in empleados:
        return f"Saldo actual de vacaciones para {empleados[codigo_empleado]['nombre']}: {empleados[codigo_empleado]['saldo_vacaciones']} días."
    else:
        return "Empleado no encontrado."
# Función para solicitar vacaciones
def solicitar_vacaciones(codigo_empleado, dias_solicitados):
    if codigo_empleado in empleados:
        saldo_actual = empleados[codigo_empleado]['saldo_vacaciones']

        if saldo_actual >= dias_solicitados:
            empleados[codigo_empleado]['saldo_vacaciones'] -= dias_solicitados
            return f"Solicitud de vacaciones aprobada para {empleados[codigo_empleado]['nombre']}. Saldo restante: {empleados[codigo_empleado]['saldo_vacaciones']} días."
        else:
            return f"No hay suficientes días de vacaciones disponibles para {empleados[codigo_empleado]['nombre']}."
    else:
        return "Empleado no encontrado."

# Función para agregar un nuevo empleado
def agregar_empleado(codigo_empleado, nombre, saldo_vacaciones, contraseña):
    if contraseña == contraseña_admin:
        if codigo_empleado not in empleados:
            empleados[codigo_empleado] = {'nombre': nombre, 'saldo_vacaciones': saldo_vacaciones}
            return f"Nuevo empleado {nombre} agregado con éxito."
        else:
            return "El empleado ya existe. Utilice otro código."
    else:
        return "Contraseña incorrecta. No tiene permisos para agregar nuevos empleados."

# Bienvenida e inicio de sesión
print("Bienvenido al Sistema de Gestión de Vacaciones de Vendomática")
print("-------------------------------------------------------------")
intentos = 3
while intentos > 0:
    usuario = input("Nombre de usuario: ").lower()
    contraseña = input("Contraseña: ")

    if usuario == usuario_permitido and contraseña == contraseña_admin:
        print("Autenticación exitosa. Bienvenido al sistema.\n")
        break
    else:
        intentos -= 1
        print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
        if intentos == 0:
            print("Acceso denegado. Cerrando el sistema.")
            exit()

# Menú interactivo
while True:
    print("\nMenú:")
    print("1. Consultar saldo de vacaciones de un empleado ")
    print("2. Solicitar vacaciones ")
    print("3. Agregar nuevo empleado (requiere contraseña de administrador) ")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        while True:
            codigo_empleado = input("Ingrese el código del empleado (o 'regresar' para volver al menú principal): ")
            if codigo_empleado.lower() == 'regresar':
                break
            print(saldo_vacaciones_empleado(codigo_empleado))

    elif opcion == '2':
        while True:
            codigo_empleado = input("Ingrese el código del empleado (o 'regresar' para volver al menú principal): ")
            if codigo_empleado.lower() == 'regresar':
                break
            try:
                dias_solicitados = int(input("Ingrese la cantidad de días de vacaciones solicitados: "))
                print(solicitar_vacaciones(codigo_empleado, dias_solicitados))
            except ValueError:
                print("Por favor ingrese un número válido de días.")

    elif opcion == '3':
        while True:
            contraseña = input("Ingrese la contraseña de administrador (o 'regresar' para volver al menú principal): ")
            if contraseña.lower() == 'regresar':
                break
            nuevo_codigo = input("Ingrese el código del nuevo empleado: ")
            nuevo_nombre = input("Ingrese el nombre del nuevo empleado: ")
            try:
                nuevo_saldo_vacaciones = int(input("Ingrese el saldo de vacaciones del nuevo empleado: "))
                print(agregar_empleado(nuevo_codigo, nuevo_nombre, nuevo_saldo_vacaciones, contraseña))
            except ValueError:
                print("Por favor ingrese un número válido para el saldo de vacaciones.")

    elif opcion == '4':
        print("Saliendo del sistema de Vendomática. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")