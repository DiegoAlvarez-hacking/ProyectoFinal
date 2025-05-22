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