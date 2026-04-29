# WPipe Steps - TODO List

## ✅ Completed Packs

### 🌐 1. Conectividad y APIs (Web Master Pack) - ✅ COMPLETADO (v0.35.0)

- ✅ `HttpRequestStep`: REST client con reintentos automáticos
- ✅ `GraphQLQueryStep`: Ejecutor de queries/mutations GraphQL
- ✅ `WebhookTriggerStep`: Notificador de webhooks
- ✅ `SftpTransferStep`: Transferencia segura de archivos (upload/download)
- ✅ `RSSParserStep`: Parser de feeds RSS/Atom
- ✅ `OAuth2AuthStep`: Gestor automático de tokens OAuth2

### 📊 2. Bases de Datos (Persistence Layer) - ✅ COMPLETADO (v0.34.0 - Redis, v0.36.0 - Resto)

- ✅ `Redis Steps`: Completo con wredis (bitmaps, hash, sets, sorted sets, streams, pub/sub, queue, geo, hyperloglog, transactions, pipeline, cache) - sync/async. Publicado en PyPI v0.23.0-v0.34.0
- ✅ `MySQLQueryStep`: Ejecución de scripts en MySQL (v0.36.0)
- ✅ `MongoInsertStep`: Inserción de documentos NoSQL (v0.36.0)
- ✅ `SQLiteAuditStep`: Volcado de logs locales (v0.36.0)
- ✅ `ClickHouseBulkStep`: Inserción masiva para analítica (v0.36.0)
- ✅ `CassandraWriteStep`: Persistencia en bases de datos distribuidas (v0.36.0)

### 🛡️ 3. Ciberseguridad (Cyber-Wisrovi Pack) - ✅ COMPLETADO (v0.37.0)

- ✅ `Fail2BanCheckStep`: Verificar si una IP está bloqueada
- ✅ `NmapScanStep`: Escaneo rápido de puertos de un objetivo
- ✅ `ShodanSearchStep`: Buscar vulnerabilidades en Shodan
- ✅ `HashGeneratorStep`: Creación de hashes (SHA256, MD5) para archivos
- ✅ `VaultSecretsStep`: Recuperar credenciales de HashiCorp Vault
- ✅ `WafFilterStep`: Limpieza de strings contra inyecciones SQL/XSS básica

### ☁️ 4. Infraestructura y Cloud - ✅ COMPLETADO (v0.38.0)

- ✅ `S3UploadStep`: Subida de archivos a AWS S3
- ✅ `DockerContainerStep`: Levantar o detener un contenedor específico
- ✅ `KubernetesPodCheckStep`: Monitorear el estado de un pod
- ✅ `TerraformApplyStep`: Ejecutar cambios de infraestructura
- ✅ `ProxmoxVMStep`: Control de máquinas virtuales en Proxmox
- ✅ `DigitalOceanDropletStep`: Gestión de droplets mediante API

### 📧 5. Notificaciones y Redes Sociales (Communication) - ✅ COMPLETADO (v0.49.0)

- ✅ `TelegramNotifyStep`: Enviar mensajes/alertas vía Telegram
- ✅ `SlackAlertStep`: Notificaciones a canales de equipo
- ✅ `DiscordBotStep`: Envío de embeds a servidores de Discord
- ✅ `SendGridMailStep`: Envío de correos transaccionales masivos
- ✅ `TwilioSmsStep`: Envío de SMS para alertas críticas
- ✅ `TwitterPostStep`: Publicación automática de actualizaciones

### 📁 6. Procesamiento de Archivos (Data Wrangling) - ✅ COMPLETADO (v0.50.0)

- ✅ `CsvToJsonStep`: Conversión rápida de formatos de datos
- ✅ `PdfGeneratorStep`: Crear reportes en PDF a partir de templates
- ✅ `ExcelParseStep`: Lectura de datos de archivos .xlsx pesados
- ✅ `ImageResizerStep`: Optimización de imágenes para web
- ✅ `ZipCompressorStep`: Comprimir carpetas de logs o backups
- ✅ `TextTranslatorStep`: Integración con Google/DeepL Translate

### 🎙️ 7. Multimedia (Audio/Video Suite) - ✅ COMPLETADO (v0.51.0)

- ✅ `AudioNormalizerStep`: Normalizar el volumen de un archivo
- ✅ `WhisperTranscribeStep`: Transcripción de audio a texto (IA)
- ✅ `AudioNoiseReductionStep`: Limpieza de ruido de fondo
- ✅ `TtsGenerateStep`: Texto a voz con voces naturales
- ✅ `VideoFrameExtractStep`: Sacar capturas de un archivo de video

### 🤖 8. Inteligencia Artificial y Lógica - ✅ COMPLETADO (v0.52.0)

- ✅ `OpenAiPromptStep`: Consultas directas a GPT-4/o1
- ✅ `HuggingFaceInferenceStep`: Uso de modelos de ML de código abierto
- ✅ `AnomalousDataStep`: Detección de outliers en un set de datos
- ✅ `SentimentAnalysisStep`: Análisis de tono en comentarios de usuarios

### ⚙️ 9. Sistema y Utilidades - ✅ COMPLETADO (v0.53.0)

- ✅ `CpuMonitorStep`: Obtener carga del sistema antes de procesos pesados
- ✅ `ShellExecStep`: Ejecución controlada de comandos Bash/PowerShell
- ✅ `CronSchedulerStep`: Programar la siguiente ejecución del pipeline
- ✅ `DiskSpaceCheckStep`: Alerta si queda poco espacio para el proceso
- ✅ `HealthCheckStep`: Ping a una lista de servicios críticos

---

## 🤗 HuggingFace Tasks - Potential Steps (30-50 ideas)

HuggingFace ofrece cientos de modelos y tareas. Aquí hay una lista de tareas que se pueden convertir en steps:

### Text Generation & LLMs
1. `HFTextGenerationStep`: Generación de texto con modelos como GPT-2, Llama, Mistral
2. `HFChatCompletionStep`: Chat interactivo con soporte para tool-calling
3. `HFTextToTextGenerationStep`: Tareas de texto a texto (T5, BART)
4. `HFCodeGenerationStep`: Generación de código con modelos especializados
5. `HFTextSummarizationStep`: Resumir textos largos automáticamente
6. `HFQuestionAnsweringStep`: Responder preguntas basadas en un contexto
7. `HFTableQuestionAnsweringStep`: Responder preguntas de tablas/datos estructurados
8. `HFConversationalStep`: Mantener conversaciones con memoria de contexto
9. `HFMultipleChoiceStep`: Selección múltiple basada en contexto
10. `HFTextParaphrasingStep`: Reformular oraciones manteniendo el significado

### Text Classification & Analysis
11. `HFSentimentAnalysisStep`: Análisis de sentimientos (ya existe, mejorar)
12. `HFZeroShotClassificationStep`: Clasificación sin entrenamiento previo
13. `HFTextClassificationStep`: Clasificación general de texto
14. `HFTokenClassificationStep`: NER (Named Entity Recognition)
15. `HFFillMaskStep`: Completar máscaras en texto (BERT-style)
16. `HFDocumentQuestionAnsweringStep`: QA en documentos complejos
17. `HFLanguageIdentificationStep`: Detectar idioma de un texto
18. `HFReadabilityAssessmentStep`: Evaluar complejidad de lectura

### Embeddings & Semantic Search
19. `HFFeatureExtractionStep`: Generar embeddings (vectorización de texto)
20. `HFSentenceSimilarityStep`: Calcular similitud entre oraciones
21. `HFSentenceEmbeddingsStep`: Embeddings de oraciones completas
22. `HFRerankingStep`: Reordenar documentos por relevancia (RAG)
23. `HFTextToSpeechStep`: Convertir texto a voz (TTS)
24. `HFSemanticSearchStep`: Búsqueda semántica en bases de datos

### Audio & Speech
25. `HFAutomaticSpeechRecognitionStep`: Transcribir audio a texto (ASR)
26. `HFAudioClassificationStep`: Clasificar audio (música, ruido, voz)
27. `HFVoiceActivityDetectionStep`: Detectar presencia de voz en audio
28. `HFAudioToAudioStep`: Procesamiento de audio (denoising, etc.)
29. `HFSpeechToSpeechStep`: Conversión de voz (estilo transfer)

### Image & Vision
30. `HFImageClassificationStep`: Clasificar imágenes en categorías
31. `HFObjectDetectionStep`: Detectar objetos en imágenes
32. `HFImageSegmentationStep`: Segmentación semántica/instancia
33. `HFImageToTextStep`: Generar descripciones de imágenes (Image Captioning)
34. `HFVisualQuestionAnsweringStep`: Responder preguntas sobre imágenes
35. `HFZeroShotImageClassificationStep`: Clasificar imágenes sin entrenar
36. `HFDepthEstimationStep`: Estimar profundidad de una imagen
37. `HFImageToImageStep`: Transformación de imágenes (estilo, super-res)
38. `HFInpaintingStep`: Rellenar áreas faltantes en imágenes
39. `HFImageColorizationStep`: Colorizar imágenes en blanco y negro

### Video
40. `HFTextToVideoStep`: Generar videos a partir de texto
41. `HFVideoClassificationStep`: Clasificar contenido de videos
42. `HFVideoFrameInterpolationStep`: Interpolar frames en videos

### Multimodal
43. `HFDocumentVisualQuestionAnsweringStep`: QA en documentos con imágenes
44. `HFImageTextToTextStep`: Tareas multimodales (imagen + texto → texto)
45. `HFAnyToAnyStep`: Modelos que aceptan múltiples tipos de entrada

### Specialized Tasks
46. `HFTranslationStep`: Traducción automática (ya existe base)
47. `HFTabularDataClassificationStep`: Clasificación de datos tabulares
48. `HFTimeSeriesForecastingStep`: Predicción de series temporales
49. `HFAnomalyDetectionStep`: Detección de anomalías en datos
50. `HFReinforcementLearningStep`: Inferencia de modelos RL

---

## 🚀 Next Steps

Para expandir con HuggingFace:
1. Elegir las tareas más demandadas (text generation, embeddings, image classification)
2. Crear un nuevo pack: `wpipe_steps.huggingface` o `wpipe_steps.ml`
3. Usar `huggingface_hub.InferenceClient` para conectar con la API
4. Soportar múltiples providers (HF Inference, Together AI, Replicate, etc.)
5. Publicar versiones incrementales (v0.54.0, v0.55.0, etc.)

---

**Total Steps Completados**: 50+ steps en 9 packs
**PyPI**: https://pypi.org/project/wpipe-steps/
**Documentado en**: CHANGELOG.md (v0.23.0 - v0.53.0)
