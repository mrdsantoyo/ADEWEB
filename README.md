# ADEWEB / Monster-Lawyer

**Monster-Lawyer** provides backups and employee file generation based on the company's needs. Securing employee files prevents short-term employment lawsuits.

<!-- #"""# Prudentia -->


**Plataforma de Gestión de Recursos Humanos**

Monster-Lawyer es una plataforma web orientada a empresas que buscan centralizar y optimizar la gestión de recursos humanos. Diseñada con una arquitectura escalable, modular y adaptable, permite administrar desde un pequeño número de clientes hasta una red nacional, ofreciendo una experiencia personalizada para cada organización.

---

## 🚀 Características principales

- 🔐 Gestión de usuarios con roles: Administrador, Recursos Humanos y Superusuario.
- 🧩 Módulos personalizables por cliente.
- 📊 Dashboard administrativo y operativo.
- 🗂️ Control y visualización de información de empleados.
- 🧠 Arquitectura escalable pensada para crecer con tus necesidades.
- 🇲🇽 Cumplimiento con la Ley Federal del Trabajo y del Seguro Social en México.

---

## 🧱 Tecnología utilizada

- Backend: **Django** (Python)
- Frontend: Próximamente <!---#(React, Vue u otra tecnología frontend moderna)--->
- Base de datos: *PostgreSQL / SQLite* (según entorno)
- Control de versiones: (*Git + GitHub*)

---

## 🧠 Enfoque pedagógico y técnico

Este proyecto también cumple una doble función:
1. Servir como sistema funcional para gestión de RRHH y el sistema de gestión.
2. Educar al personal de RRHH respecto al mantenimiento y control del personal y sus expedientes con la finalidad de evitar juicios laborales

---
<!---├── static/         # Archivos estáticos (CSS, JS, imágenes)-->


## ⚙️ Estructura del proyecto (inicial)

```
adeweb/
├── adeweb/             # Configuración general del proyecto
├── usuarios/           # App para gestión de usuarios y autenticación
├── documentos/         # App para gestión de empleados
├── templates/          # Plantillas HTML
├── README.md       
├── LICENCE             # Licencia MIT
└── requirements.txt    # Instalación de dependencias 
...
..
.

```
---

## 🔧 Instalación rápida

```bash
git clone https://github.com/mrdsantoyo/ADEWEB.git
cd adeweb
python -m venv venv
source ./venv//Scripts//Activate.ps1 #En Linux: venv/bin/activate 
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📌 Roadmap

- [x] Análisis de requerimientos
- [x] Diseño modular inicial
- [x] Implementación de base de datos
- [ ] Módulo de autenticación
- [ ] Panel de administración
- [ ] Personalización por cliente
- [ ] Módulos adicionales: (*control documental, documentos, asistencia, etc.*)

---

## 🧑‍💻 Autor

Desarrollado por Daniel Santoyo ([@mrdsantoyo](https://github.com/mrdsantoyo)). Daniel Santoyo (@mrdsantoyo)

Contacto: danielsa00@gmail.com | LinkedIn: www.linkedin.com/in/daniel-santoyo00

---

## 📄 Licencia


**Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.**

