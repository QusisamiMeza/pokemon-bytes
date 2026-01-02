# POKEMON BYTES

Trabajo grupal desarrollado en la materia de Introducción al Desarrollo de Software

---

**Pokémon Bytes** es un proyecto full stack que combina un **backend en FastAPI** y un **frontend en Svelte** para gestionar y visualizar información relacionada con Pokemones.

El repositorio está organizado como un monorepo, donde frontend y backend conviven en un mismo proyecto pero se ejecutan de forma independiente.

---

## Estructura y flujo del proyecto

```text
.
├── back/    # Backend (FastAPI + SQLAlchemy + Alembic)
├── front/   # Frontend (Svelte + Vite)
└── README.md

```
El flujo del proyecto sigue los siguientes pasos generales:
1. Levantar el backend
2. Levantar el frontend
3. Consumir la API desde la interfaz web

Cada parte se ejecuta por separado desde su respectiva carpeta.


### Backend

El backend está desarrollado con FastAPI y utiliza SQLAlchemy junto con Alembic para las migraciones de base de datos.

- Instrucciones completas en:

```
back/README_BACKEND.md
```

### Frontend

El frontend está desarrollado con Svelte y se comunica con la API provista por el backend.

- Instrucciones completas en:

```
front/README_FRONTEND.md
```
---

## Objetivos alcanzados

- Desarrollo de un backend que expone una API REST, respetando contratos de comunicación claros entre cliente y servidor.

- Implementación de un frontend web que consume la API y presenta la información de manera clara e interactiva.

- Uso de estructuras de datos y modelos para representar la información del dominio.

- Manejo de persistencia de datos mediante una base de datos y migraciones.

- Separación de responsabilidades entre frontend y backend, promoviendo una arquitectura modular y mantenible.

- Aplicación de buenas prácticas de desarrollo de software, incluyendo:

    - Organización del código.

    - Reutilización de componentes.

    - Claridad y legibilidad.

    - Uso de control de versiones con Git.

- Configuración de entornos de desarrollo reproducibles mediante el uso de entornos virtuales y gestión de dependencias.

- Desarrollo orientado a pruebas, incorporando tests automatizados para validar el funcionamiento del sistema.

