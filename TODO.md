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

### 🤗 10. HuggingFace (Local - No API Key) - ✅ COMPLETADO (v0.55.0 - v0.104.0)

#### Text NLP (10 steps - v0.55.0 a v0.64.0)
- ✅ `HFTextClassificationStep` (v0.55.0): Text classification (BERT)
- ✅ `HFSentimentAnalysisStep` (v0.56.0): Sentiment analysis (DistilBERT)
- ✅ `HFZeroShotClassificationStep` (v0.57.0): Zero-shot classification (BART)
- ✅ `HFNerStep` (v0.58.0): Named Entity Recognition (BERT-NER)
- ✅ `HFFillMaskStep` (v0.59.0): Fill masked tokens (BERT)
- ✅ `HFQuestionAnsweringStep` (v0.60.0): QA based on context (BERT-SQuAD)
- ✅ `HFSummarizationStep` (v0.61.0): Text summarization (BART-CNN)
- ✅ `HFTranslationStep` (v0.62.0): Translate text (T5)
- ✅ `HFTextGenerationStep` (v0.63.0): Generate text (GPT-2)
- ✅ `HFConversationalStep` (v0.64.0): Chat with memory (BlenderBot)

#### Text/Embeddings (10 steps - v0.65.0 a v0.74.0)
- ✅ `HFText2TextGenerationStep` (v0.65.0): Text-to-text (T5)
- ✅ `HFMultipleChoiceStep` (v0.66.0): Multiple choice QA (RoBERTa)
- ✅ `HFTableQuestionAnsweringStep` (v0.67.0): QA on tables (TAPAS)
- ✅ `HFFeatureExtractionStep` (v0.68.0): Extract embeddings (BERT)
- ✅ `HFSentenceEmbeddingsStep` (v0.69.0): Sentence embeddings (sentence-transformers)
- ✅ `HFSentenceSimilarityStep` (v0.70.0): Semantic similarity
- ✅ `HFRerankingStep` (v0.71.0): Rerank docs for RAG
- ✅ `HFSemanticSearchStep` (v0.72.0): Semantic search
- ✅ `HFDocumentQuestionAnsweringStep` (v0.73.0): QA on document images
- ✅ `HFLanguageIdentificationStep` (v0.74.0): Detect language

#### Audio/Speech (8 steps - v0.75.0 a v0.82.0)
- ✅ `HFAutomaticSpeechRecognitionStep` (v0.75.0): Transcribe audio (Whisper)
- ✅ `HFAudioClassificationStep` (v0.76.0): Classify audio
- ✅ `HFTextToSpeechStep` (v0.77.0): Text to speech (ESPnet)
- ✅ `HFVoiceActivityDetectionStep` (v0.78.0): Detect voice
- ✅ `HFAudioToAudioStep` (v0.79.0): Denoising
- ✅ `HFAudioEmotionRecognitionStep` (v0.80.0): Emotion in speech
- ✅ `HFSpeechToSpeechStep` (v0.81.0): Voice conversion
- ✅ `HFSpeakerDiarizationStep` (v0.82.0): Who spoke when

#### Vision (15 steps - v0.83.0 a v0.97.0)
- ✅ `HFImageClassificationStep` (v0.83.0): Classify images (ViT)
- ✅ `HFObjectDetectionStep` (v0.84.0): Detect objects (DETR)
- ✅ `HFImageSegmentationStep` (v0.85.0): Semantic segmentation (SegFormer)
- ✅ `HFImageToTextStep` (v0.86.0): Image captioning (BLIP)
- ✅ `HFVisualQuestionAnsweringStep` (v0.87.0): VQA on images
- ✅ `HFZeroShotImageClassificationStep` (v0.88.0): Zero-shot image classification (CLIP)
- ✅ `HFDepthEstimationStep` (v0.89.0): Depth estimation (DPT)
- ✅ `HFImageToImageStep` (v0.90.0): Image transformation (Swin2SR)
- ✅ `HFInpaintingStep` (v0.91.0): Inpainting
- ✅ `HFImageColorizationStep` (v0.92.0): Colorize B&W images
- ✅ `HFImageSuperResolutionStep` (v0.93.0): Super resolution
- ✅ `HFImageStyleTransferStep` (v0.94.0): Style transfer
- ✅ `HFOcrStep` (v0.95.0): OCR (TrOCR)
- ✅ `HFFaceDetectionStep` (v0.96.0): Face detection
- ✅ `HFImageBackgroundRemovalStep` (v0.97.0): Remove backgrounds

#### Video & Multimodal (7 steps - v0.98.0 a v0.104.0)
- ✅ `HFVideoClassificationStep` (v0.98.0): Classify video
- ✅ `HFVideoFrameInterpolationStep` (v0.99.0): Interpolate frames
- ✅ `HFDocumentVisualQuestionAnsweringStep` (v0.100.0): VQA on document images
- ✅ `HFImageTextToTextStep` (v0.101.0): Multimodal image+text (BLIP2)
- ✅ `HFAnyToAnyStep` (v0.102.0): Any-to-any multimodal models
- ✅ `HFTableDetectionStep` (v0.103.0): Detect tables in documents
- ✅ `HFTableDetectionStep` (v0.104.0): Detect tables in documents

---

## 📊 Resumen Total

**Total Steps Completados**: **100+ steps** en 10 packs
- 50+ steps en packs tradicionales (Redis, Connectivity, Security, etc.)
- 50 steps en HuggingFace pack (v0.55.0 - v0.104.0)

**PyPI**: https://pypi.org/project/wpipe-steps/
**Última versión**: v0.104.0 (50 HuggingFace steps locales, sin API key)

**Características HuggingFace Pack:**
- ✅ 100% local (no requiere internet después de descarga)
- ✅ Sin API key requerida
- ✅ Modelos descargados una vez y cacheados
- ✅ Soporta CPU y GPU (`device="cpu"` o `device="cuda"`)
- ✅ Usa `transformers.pipeline()` con `local_files_only=True`
- ✅ Incluye Text, Audio, Vision, Video y Multimodal
