# 📜 Reglas de Evolución de wpipe-steps

Este documento define el proceso estricto de desarrollo, versionamiento y publicación para la librería `wpipe-steps`. Estas reglas aseguran una evolución constante, documentada y profesional.

## 🚀 Ciclo de Desarrollo por Estado

Cada vez que se añada un nuevo **Estado (Step)**, se debe seguir este ciclo obligatorio:

1.  **Implementación Quirúrgica**: 
    *   Desarrollar el nuevo Step en su subpaquete correspondiente dentro de `wpipe_steps/`.
    *   Heredar obligatoriamente de `BaseStep`.
    *   Asegurarse de que el nuevo Step sea compatible con el Factory Pattern.
    *   Asegurarse de que el nuevo Step sea compatible con el Type Hinting.
    *   Asegurarse de que el nuevo Step no use librerias que no sean de la suit, es decir, en lugar de usar redis usar wredis, en lugar de postgresql usar wpostgresql, etc.
2.  **Espejo de Ejemplo**:
    *   Crear un script de ejemplo en la carpeta homóloga dentro de `examples/`.
    *   El ejemplo debe ser funcional y auto-explicativo.
    *   Junto al ejemplo se debe crear un archivo `requirements.txt` con las dependencias necesarias para ejecutar el ejemplo.
    *   Junto al ejemplo se debe crear un archivo `README.md` con la descripción del ejemplo.
    *   Seguir estrictamente la sección 📝u Creación de Estados (Steps) para estructura de  
        Steps, incluyendo opcionalidad de timeouts y soporte para contextos Pydantic.
    *   Todos los ejemplos deben ser funcionales
3.  **Incremento de Versión Secuencial**:
    *   **REGLAS CLARAS**:
        - **UN NUEVO ESTADO = UN INCREMENTO EN EL SEGUNDO DÍGITO**
        - Ejemplo: Estado 1 → v0.55.0, Estado 2 → v0.56.0, ..., Estado 50 → v0.104.0
        - **PROHIBIDO** agrupar múltiples estados en una sola versión (ej: 7 estados en v0.57.0 es INCORRECTO)
        - Si se requiere hacer una actualización mayor (breaking change), incrementar el PRIMER dígito: v1.0.0
    *   Actualizar `pyproject.toml`, `setup.py`, `README.md` y `wpipe_steps/__init__.py`.
    *   **Ejemplo de secuencia correcta**:
        - `0.1.0` (Base) → `0.2.0` (Estado 1) → `0.3.0` (Estado 2) → ... → `0.500.0` (Estado 499)
4.  **Actualización de Documentación**:
    *   Actualizar el `README.md` principal incluyendo el nuevo Step en las tablas de referencia.
    *   Añadir una breve descripción de su uso.
5.  **Publicación a PyPI**:
    *   Una vez cumplidos los pasos anteriores, se debe realizar la publicación oficial.
6.  **Actualización de Changelog**:
    *   Actualizar el `CHANGELOG.md` con la nueva versión y los cambios realizados.
7.  **Commit**:
    *   Realizar un commit con todos los cambios realizadosn en perfecto ingles, iniciando con [FEATURE], [FIX], [CHORE], [DOCS], [TEST], [REFACTOR], [STYLE], [PERF], [BUILD], [CI], [UPGRADE], [DOWNGRADE], [MIGRATION], [BREAKING CHANGE].
8.  **Push**:
    *   Realizar un push a la rama `main`.

## 📂 Estructura de Carpetas Simétrica

La estructura de `examples/` debe ser siempre un reflejo fiel de `wpipe_steps/`:

```text
wpipe_steps/                            examples/
├── connectivity/           <──>        ├── connectivity/
├── database/               <──>        ├── database/
├── security/               <──>        ├── security/
└── ...                                 └── ...
```

## 🛠 Estándares de Código

-   **BaseStep**: Todo estado debe ser una clase que herede de `wpipe_steps.core.base.BaseStep`.
-   **Factory Pattern**: Se debe promover el uso de `.as_step()` para la integración en pipelines.
-   **Type Hinting**: Uso estricto de tipos para garantizar la robustez.
-   **No external libraries**: No se deben usar librerias que no sean de la suit, es decir, en lugar de usar redis usar wredis, en lugar de postgresql usar wpostgresql, etc.
-   **Docstrings-google**: Todo estado debe tener docstrings en formato google.


---
*Diseñado para mantener la excelencia técnica en cada iteración.*
