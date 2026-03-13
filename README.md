Edificio Inteligente

Sistema IoT para monitoreo y gestión inteligente de recursos en edificios, desarrollado con ESP32, base de datos en la nube y visualización de datos mediante una aplicación en Python.

El proyecto permite monitorear variables clave del edificio y generar alertas automáticas, facilitando la toma de decisiones y la gestión del mantenimiento.

Objetivo del proyecto:

Desarrollar una plataforma IoT capaz de:

 - Monitorear variables del edificio en tiempo real

- Detectar eventos relevantes (ruido, nivel de tanque, temperatura)

- Almacenar datos en la nube

- Visualizar información mediante un dashboard

- Generar alertas automáticas por Telegram

- Este proyecto busca ser la base para un sistema escalable de automatización de edificios.

Arquitectura del sistema:

El sistema está compuesto por cuatro componentes principales:

1) Sensores

Capturan información del entorno y del sistema hidráulico del edificio.

Sensores utilizados:

- Sensor de nivel de tanque

- Sensor de temperatura

- Sensor de ruido LM393

2) Microcontrolador

Se utiliza un ESP32, encargado de:

- Leer los sensores

- Procesar los datos

- Enviar información por WiFi a la base de datos

3) Base de datos en la nube

Se utiliza Supabase para:

- Almacenar los datos de los sensores

- Registrar eventos del sistema

- Servir los datos al dashboard

4) Visualización y monitoreo

Aplicación desarrollada en Python utilizando Streamlit para:

- Visualizar variables del sistema

- Monitorear el estado del tanque

- Analizar datos recolectados por los sensores

5) Sistema de alertas

El sistema incluye notificaciones automáticas mediante Telegram.

Cuando el nivel del tanque cae por debajo de un umbral configurado, el sistema envía una alerta para advertir que el tanque necesita recarga.

Esto permite actuar rápidamente ante posibles problemas en el suministro de agua.
----------------------------------------------------------------------------------------------------------------------------
Ejemplo de datos enviados

El ESP32 envía datos estructurados en formato JSON:
{
  "device_id": "edificio_01",
  "nivel_tanque": 70,
  "temperatura": 24.5,
  "ruido": 1
}
-----------------------------------------------------------------------------------------------------------------------------------------
Tecnologías utilizadas:

*Hardware

- ESP32 ; Sensor de ruido LM393 ; Sensores de nivel ; Sensores de temperatura

*Software

- Arduino IDE ; Python ; Streamlit ; Supabase ; Telegram Bot API ; Visual Studio Code ; Git / GitHub
-----------------------------------------------------------------------------------------------------------------------------------------
Dashboard

El dashboard permite:

- Visualizar variables del sistema

- Monitorear el nivel del tanque

- Observar eventos detectados por sensores

- Analizar datos históricos
-----------------------------------------------------------------------------------------------------------------------------------------
Posibles ampliaciones del sistema

El proyecto puede ampliarse con:

- Control automático de válvulas

- Medición de consumo de agua

- Detección de fugas

- Monitoreo energético

- Integración con sistemas de mantenimiento predictivo

- Machine Learning para detección de anomalías
