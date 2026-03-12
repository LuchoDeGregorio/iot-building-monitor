import streamlit as st
import pandas as pd
from supabase import create_client
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import requests

TOKEN = "8584675746:AAFgKS-AltFuBy0lONgy_mJaz0agNED9KDo"
CHAT_ID = "8620998433"

def enviar_alerta(mensaje):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": mensaje
    }

    requests.post(url, data=data)

st.set_page_config(page_title="Monitoreo Edificios", layout="wide")

st.title("Sistema de Monitoreo Inteligente")

st_autorefresh(interval=10000, key="refresh")

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)

response = supabase.table("sensor_data") \
    .select("*") \
    .order("created_at", desc=True) \
    .limit(500) \
    .execute()

data = pd.DataFrame(response.data)

if not data.empty:

    data["created_at"] = pd.to_datetime(data["created_at"])
    data = data.sort_values("created_at")

    devices = data["device_id"].unique()

    device_selected = st.selectbox(
        "Seleccionar edificio/dispositivo",
        devices
    )

    data_device = data[data["device_id"] == device_selected]

    ultimo = data_device.iloc[-1]

    temperatura = ultimo["temperatura"]
    nivel = ultimo["nivel_tanque"]
    corriente = ultimo["corriente"]

    st.subheader("Alertas del sistema")

    alerta = False

    if nivel < 30:
        st.warning("⚠ Nivel de tanque bajo")
        enviar_alerta(f"⚠ ALERTA\nNivel de tanque bajo: {nivel}%")
        alerta = True

    if temperatura > 40:
        st.warning("⚠ Temperatura alta en sala de máquinas")
        enviar_alerta(f"⚠ ALERTA\nTemperatura alta: {temperatura}°C")
        alerta = True

    if corriente > 1:
        st.info("⚡ Bomba en funcionamiento")

    if not alerta:
        st.success("✅ Sistema funcionando normalmente")

    col1, col2, col3 = st.columns(3)

    col1.metric("Temperatura", f"{temperatura:.2f} °C")
    col2.metric("Nivel tanque", f"{nivel} %")
    col3.metric("Corriente bomba", f"{corriente} A")

    st.divider()

    ahora = datetime.now(ultimo["created_at"].tzinfo)
    diferencia = ahora - ultimo["created_at"]

    if diferencia.total_seconds() < 120:
        st.success("🟢 Sistema ONLINE")
    else:
        st.error("🔴 Sistema OFFLINE")

    st.divider()

    st.subheader("Nivel de tanque")
    st.progress(int(nivel))

    st.divider()

    st.subheader("Histórico de temperatura")

    st.line_chart(
        data_device.set_index("created_at")["temperatura"]
    )

    #enviar_alerta("Prueba de alerta desde el sistema IoT")

else:
    st.warning("No hay datos todavía")