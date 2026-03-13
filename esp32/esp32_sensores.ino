#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <HTTPClient.h>

#include <OneWire.h>
#include <DallasTemperature.h>

#define SOUND_SENSOR 34

const char* ssid = "cargar datos wifi";
const char* password = "cargar datos wifi";

String supabaseUrl = "cargar datos base datos";
String supabaseKey = "cargar datos base datos;

#define ONE_WIRE_BUS 4

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

WiFiClientSecure client;

void setup() {

  Serial.begin(115200);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("WiFi conectado");

  client.setInsecure();

  sensors.begin();
}

void loop() {

  sensors.requestTemperatures();
  float temp = sensors.getTempCByIndex(0);

  Serial.print("Temperatura: ");
  Serial.println(temp);

  float nivel = random(60,90);
  float corriente = random(0,5);

  int sonido = analogRead(SOUND_SENSOR);

  Serial.println("----");
  Serial.print("Temp: ");
  Serial.println(temp);

  Serial.print("Nivel: ");
  Serial.println(nivel);

  Serial.print("Corriente: ");
  Serial.println(corriente);

  Serial.print("Nivel sonido: ");
  Serial.println(sonido);

  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient https;

    https.begin(client, supabaseUrl);

    https.addHeader("Content-Type", "application/json");
    https.addHeader("apikey", supabaseKey);
    https.addHeader("Authorization", "Bearer " + supabaseKey);

    String json = "{";
    json += "\"device_id\":\"edificio_01\",";
    json += "\"nivel_tanque\":" + String(nivel) + ",";
    json += "\"temperatura\":" + String(temp) + ",";
    json += "\"corriente\":" + String(corriente)+ ",";
    json += "\"ruido\":" + String(sonido);
    json += "}";

    int httpCode = https.POST(json);

    Serial.print("HTTP Response: ");
    Serial.println(httpCode);

    https.end();
  }

  delay(60000);
}