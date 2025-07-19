
# 🐍 Culebrita

![Made by PanchoxGrande](https://img.shields.io/badge/Hecho%20por-PanchoxGrande-green?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-yellow)

> Versión retro del clásico Snake... directo en tu terminal, ¡con puntuación, emojis y adrenalina nostálgica! 🎮

---

## 🧠 ¿Qué hace?

**Culebrita** es un juego tipo *Snake* que corre completamente en tu **terminal**. No necesita interfaz gráfica, solo Python y muchas ganas de esquivar tu propia cola 🐍

### ✅ Características:
- Interfaz retro en consola usando `curses`
- Puntuación en tiempo real en pantalla
- Colisiones contra bordes y uno mismo = **Game Over**
- 🍎 La manzana nunca aparece sobre la culebra
- Verifica que la terminal tenga tamaño mínimo
- Totalmente multiplataforma: **Linux**, **macOS**, **Windows**

---

## 💾 Descargar

🔽 [Descargar ZIP del juego](https://github.com/panchoxgrande/culebrita/archive/refs/heads/main.zip)  


O clonalo con Git:

```bash
git clone https://github.com/panchoxgrande/culebrita.git
cd culebrita
````

---

## 💻 Instalación

### 🐧 Linux / macOS

1. Asegurate de tener Python 3.8 o superior:

```bash
python3 --version
```

2. Instala los requerimientos (opcional en Linux/macOS):

```bash
pip install -r requirements.txt
```

> En Linux y macOS `curses` ya viene incluido con Python, ¡todo listo!

---

### 🪟 Windows

1. Asegurate de tener Python 3.8 o superior:

```powershell
python --version
```

2. Instala las dependencias:

```powershell
pip install -r requirements.txt
```

> Esto instalará `windows-curses`, necesario para hacer funcionar `curses` en Windows.

---

## 🚀 Cómo ejecutar

Desde la raíz del proyecto:

```bash
python culebrita.py
```

✅ Aparecerá el juego en tu terminal. Usá las teclas de flechas para mover la serpiente.

---

## 🎮 Controles

* ➡️ ⬅️ ⬆️ ⬇️  Mover la culebra
* 🍎 Comer manzanas para sumar puntos
* 💥 Perdés si chocás con tu cuerpo o los bordes
* 🏁 Tu puntaje aparece arriba en pantalla

---

## 📦 Estructura del proyecto

```
culebrita/
├── culebrita.py          # Juego principal
├── requirements.txt      # Dependencias
└── README.md             # Este archivo
```

---

## 👨‍💻 Autor

**Francisco Carranza** — alias [PanchoxGrande](https://github.com/panchoxgrande)
🧠 Jefe de Tecnologías | 🛡️ Ciberseguridad | 👨‍👩‍👧‍👦 Padre de familia | 🎮 Gamer de consola y terminal

---

## ☕ ¿Te gustó?

Si disfrutaste esquivar colisiones con la culebra, ¡dejá una ⭐ en el repo!

Y si querés agregar dificultad, récords o sonido... ¡estás invitado a colaborar!

---

