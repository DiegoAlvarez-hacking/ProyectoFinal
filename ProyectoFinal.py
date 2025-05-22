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
