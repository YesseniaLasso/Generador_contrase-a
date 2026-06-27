# 🔐 Generador Seguro de Contraseñas

**Proyecto Integrador Final — Lógica de Programación 1**
Universidad Internacional del Ecuador (UIDE) · Powered by Arizona State University®

---

## 👩‍💻 Integrante

| Nombre | Sección | Docente |
|--------|---------|---------|
| Yessenia Elizabeth Lasso Gordon | 1A | Lilian Marlene Aman Ramos |

---

## 🎯 Objetivo del sistema

Desarrollar un programa en Python que genere automáticamente contraseñas seguras y aleatorias, permitiendo al usuario configurar la longitud y los tipos de caracteres a incluir, como respuesta a la problemática de contraseñas débiles o predecibles en el entorno digital actual.

---

## 📋 Descripción de funcionalidades

El programa permite al usuario:

- **Ingresar la longitud** de la contraseña deseada (mínimo 8 caracteres)
- **Seleccionar los tipos de caracteres** a incluir:
  - Letras mayúsculas (A–Z)
  - Letras minúsculas (a–z)
  - Dígitos numéricos (0–9)
  - Símbolos especiales (!@#$%^&*)
- **Generar la contraseña** de forma aleatoria combinando los grupos seleccionados
- **Mostrar el resultado** en pantalla de forma clara
- **Validar los parámetros** ingresados, mostrando mensajes de advertencia si la configuración no es válida

---

## 🗂️ Estructura del repositorio

```
generador-contrasenas/
│
├── generador1.py              # Código principal del programa primera etapa
├── README.md                  # Este archivo
├── Video1.mp4                 # Video de código primera parte
├── Video2.mp4                 # Video de código completo
├── flujo_raptor.rap           # Diagrama de flujo elaborado en RAPTOR
├── Protecto_final.pdf         # Informe del desarrollo del programa
└── Generador2.py              # Código principal del programa etapa final

```

---

## ▶️ ¿Cómo ejecutar el programa?

**Requisitos:** tener Python 3 instalado en tu computadora.

1. Clona o descarga este repositorio
2. Abre una terminal en la carpeta del proyecto
3. Ejecuta el siguiente comando:

```bash
python generador.py
```

4. Sigue las instrucciones que aparecen en pantalla

---

## 🧠 Conceptos aplicados

| Unidad | Contenido | Aplicación en el proyecto |
|--------|-----------|--------------------------|
| Unidad 1 | Diagramas funcionales y arquitectura | Caso de uso, flujo en RAPTOR y diagrama de capas |
| Unidad 2 | Estructuras condicionales y repetitivas | `if/elif` para validar parámetros, `for` para generar la contraseña |
| Unidad 3 | Organización del código | Funciones con responsabilidad única y código estructurado |
| Unidad 4 | Herramientas de desarrollo | Control de versiones con GitHub y documentación con README |

---

## 🔄 Evolución del código

El programa pasó por dos versiones durante el desarrollo:

**Versión 1** — Los grupos de caracteres se almacenaban en variables de tipo `string`:
```python
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros    = "0123456789"
simbolos   = "!@#$%^&*"
```

**Versión 2 (mejorada)** — Al aprender el tema de Tuplas, el código fue refactorizado para usar esta estructura más organizada e inmutable:
```python
mayusculas = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
minusculas = tuple("abcdefghijklmnopqrstuvwxyz")
numeros    = tuple("0123456789")
simbolos   = tuple("!@#$%^&*")
```

---

## 📅 Fecha

27,Junio, 2026
