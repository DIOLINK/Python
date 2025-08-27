# Ejercicios Python

Este proyecto contiene la transcripción de programas TypeScript a Python, incluyendo una variedad de ejercicios de programación.

## Programas Incluidos

1. **HowOldAreYou** - Verifica si una persona es mayor o menor de edad
2. **ValidateStorePass** - Valida contraseñas almacenadas
3. **Divide** - Realiza divisiones entre dos números
4. **UnivenOrPair** - Determina si un número es par o impar
5. **AgeTaxAction** - Calcula impuestos basados en edad e ingresos mensuales
6. **SumNumber** - Suma números consecutivos desde 1 hasta un valor dado
7. **SumAllNum** - Suma todos los números positivos ingresados

## Requisitos

- Python 3.6 o superior

## Ejecución

### Ejecutar el menú principal (recomendado)
```bash
python3 Ejers.py
```

### Ejecutar programas individuales
```bash
# Verificar edad
python3 HowOldAreYou.py

# Validar contraseña
python3 ValidateStorePass.py

# División de números
python3 Divide.py

# Verificar par/impar
python3 UnivenOrPair.py

# Cálculo de impuestos
python3 AgeTaxAction.py

# Suma de números consecutivos
python3 SumNumber.py

# Suma de todos los números
python3 SumAllNum.py
```

## Estructura del Proyecto

```
class/
├── Ejers.py              # Menú principal
├── HowOldAreYou.py       # Verificación de edad
├── ValidateStorePass.py  # Validación de contraseñas
├── Divide.py            # División de números
├── UnivenOrPair.py      # Verificación par/impar
├── AgeTaxAction.py      # Cálculo de impuestos
├── SumNumber.py         # Suma de números consecutivos
├── SumAllNum.py         # Suma de todos los números
├── ProgramUtil.py       # Clase utilitaria base
└── README.md           # Este archivo
```

## Uso

1. Ejecuta `python3 Ejers.py` para iniciar el menú principal
2. Selecciona el número del programa que deseas ejecutar
3. Sigue las instrucciones en pantalla para cada programa
4. Selecciona 0 para salir

## Características

- **Python 3**: Código moderno y legible
- **Modular**: Cada programa es una clase independiente
- **Interactivo**: Interfaz de consola con menú principal
- **Reutilizable**: Clase base `ProgramUtil` para funcionalidad común
- **Manejo de errores**: Validación de entrada y excepciones

## Funcionalidades por Programa

### HowOldAreYou
- Valida edad entre 0 y 150 años
- Determina si es mayor o menor de 18 años
- Manejo de errores para entradas inválidas

### ValidateStorePass
- Valida contraseñas contra una lista predefinida
- Comparación case-insensitive
- Bucle hasta encontrar contraseña correcta

### Divide
- División de dos números con validación
- Previene división por cero
- Opción de continuar o salir

### UnivenOrPair
- Determina si un número es par o impar
- Validación de entrada numérica
- Opción de continuar o salir

### AgeTaxAction
- Calcula edad a partir de fecha de nacimiento
- Ingreso de ingresos mensuales
- Determina si debe tributar (ingresos > 1,000,000)

### SumNumber
- Suma números consecutivos desde 1 hasta N
- Validación de números positivos
- Salida con cero

### SumAllNum
- Suma todos los números positivos ingresados
- Salida con número negativo
- Acumulador de suma

## Ejemplos de Uso

```bash
# Ejecutar menú principal
python3 Ejers.py

# Ejecutar programa específico
python3 HowOldAreYou.py
```

## Notas Técnicas

- Todos los programas usan `input()` para entrada del usuario
- Manejo de excepciones con `try/except` para entradas inválidas
- Uso de `datetime` para cálculos de fechas en AgeTaxAction
- Herencia de clases para reutilización de código
