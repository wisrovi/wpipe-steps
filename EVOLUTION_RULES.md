# 📜 Reglas de Evolución de wpipe-steps

Este documento define el proceso estricto de desarrollo, versionamiento y publicación para la librería `wpipe-steps`. Estas reglas aseguran una evolución constante, documentada y profesional.

## 🚀 Ciclo de Desarrollo por Estado

Cada vez que se añada un nuevo **Estado (Step)**, se debe seguir este ciclo obligatorio:

1.  **Implementación Quirúrgica**: 
    *   Desarrollar el nuevo Step en su subpaquete correspondiente dentro de `wpipe_steps/`.
    *   Heredar obligatoriamente de `BaseStep`.
2.  **Espejo de Ejemplo**:
    *   Crear un script de ejemplo en la carpeta homóloga dentro de `examples/`.
    *   El ejemplo debe ser funcional y auto-explicativo.
3.  **Incremento de Versión Secuencial**:
    *   La versión se incrementará en el segundo dígito por cada nuevo estado.
    *   Secuencia: `0.1.0` (Base) -> `0.2.0` (Estado 1) -> `0.3.0` (Estado 2) ... -> `0.100.0`.
    *   Actualizar `pyproject.toml` y `setup.py`.
4.  **Actualización de Documentación**:
    *   Actualizar el `README.md` principal incluyendo el nuevo Step en las tablas de referencia.
    *   Añadir una breve descripción de su uso.
5.  **Publicación a PyPI**:
    *   Una vez cumplidos los pasos anteriores, se debe realizar la publicación oficial.

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

---
*Diseñado para mantener la excelencia técnica en cada iteración.*
