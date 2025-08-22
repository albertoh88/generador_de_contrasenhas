# 🛡️ Generador de Contraseñas Seguras  

Un generador de contraseñas desarrollado en **Python con Tkinter**, que permite crear claves seguras y personalizadas de manera sencilla.  

---

## ✨ Características  

- ✅ Interfaz gráfica amigable con **Tkinter**.  
- ✅ Permite incluir/excluir:  
  - Letras mayúsculas  
  - Letras minúsculas  
  - Números  
  - Caracteres especiales  
- ✅ Control de **longitud mínima (8 caracteres)**.  
- ✅ Generación aleatoria usando la librería **`secrets`** (segura para criptografía).  
- ✅ Botón para **copiar al portapapeles** con `pyperclip`.  

---

## 🚀 Requisitos  

Antes de ejecutar el programa asegúrate de tener instalado:  

- [Python 3.8+](https://www.python.org/downloads/)  
- Librerías necesarias:  
  - tkinter (incluido por defecto en Python)  
  - pyperclip 

Instalación de dependencias adicionales:  

```bash
pip install pyperclip
```
---

## ▶️ Ejecución

Clona el repositorio y ejecuta el script:

```bash
python generador_contraseñas.py
```

Se abrirá una ventana gráfica donde podrás:

- Seleccionar las opciones de tu contraseña.
- Ajustar la longitud.
- Generar y copiar con un clic.

---

## 📸 Captura de pantalla (ejemplo)

![Generador de contraseñas](https://github.com/albertoh88/generador_de_contrasenhas/blob/main/generador_de_contrasenhas.png)

---

## 💡 Ideas de mejora

- Guardar historial de contraseñas generadas.
- Añadir un medidor de "fortaleza" de la contraseña.
- Exportar las contraseñas a un archivo cifrado.
- Portar la aplicación a un ejecutable (.exe) para usuarios sin Python.
