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

---

### Backend

El backend está desarrollado con FastAPI y utiliza SQLAlchemy junto con Alembic para las migraciones de base de datos.

- Instrucciones completas en:

```
back/README_BACKEND.md
```
---

### Frontend

El frontend está desarrollado con Svelte y se comunica con la API provista por el backend.

- Instrucciones completas en:

```
front/README_FRONTEND.md
```
---
