# 🧮 Calculadora con Python y Tkinter

Una calculadora de escritorio sencilla construida con **Python**, usando **Tkinter** para la interfaz gráfica y **numexpr** para la evaluación de expresiones matemáticas.

---

## 📸 Vista general

La calculadora cuenta con una pantalla de entrada y botones para:
- Dígitos del 0 al 9
- Operaciones básicas: `+`, `-`, `*`, `/`
- Paréntesis: `(`, `)`
- Punto decimal `.`
- Borrar último carácter (`Del`)
- Limpiar toda la pantalla (`AC`)
- Calcular el resultado (`=`)

---

## 🚀 Requisitos

- Python 3.x
- [numexpr](https://numexpr.readthedocs.io/)

Instala la dependencia con:

```bash
pip install numexpr
```

> `tkinter` viene incluido por defecto con la mayoría de instalaciones de Python.

---

## ▶️ Cómo ejecutar

```bash
python calculadora.py
```

---

## 📁 Estructura del proyecto

```
calculadora/
│
├── calculadora.py   # Código fuente principal
└── README.md        # Este archivo
```

---

## ⚙️ Funcionamiento

| Función                  | Descripción                                                   |
|--------------------------|---------------------------------------------------------------|
| `expresion_matematica()` | Agrega un carácter a la pantalla; si hubo un resultado previo, reemplaza el contenido |
| `eliminar_caracter()`    | Borra el último carácter ingresado                           |
| `eliminar_todo()`        | Limpia completamente la pantalla                              |
| `resultado_operaciones()`| Evalúa la expresión usando `numexpr` y muestra el resultado  |

---

## 🛠️ Tecnologías

- **Tkinter** — GUI nativa de Python
- **ttk (themed widgets)** — Estilización de botones
- **numexpr** — Evaluación segura y eficiente de expresiones matemáticas

---

## 📝 Notas

- Si la expresión ingresada tiene un error de sintaxis, la calculadora muestra el mensaje `Error al calcular.`.
- Los botones `Del` y `AC` están resaltados en rojo para distinguirlos visualmente.

---

## 📄 Licencia

Este proyecto es de uso libre para fines educativos.
