import streamlit as st
import pandas as pd
from supabase import create_client
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# configuración página
st.set_page_config(page_title="Monitoreo Edificio", layout="wide")

st.title("Sistema de Monitoreo Inteligente")

# refresco automático
st_autorefresh(interval=10000, key="refresh")


url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

# conexión
#url = "SUPABASE_URL","https://anwwqipwfcfycravtxvb.supabase.co"
#key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFud3dxaXB3ZmNmeWNyYXZ0eHZiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMwNjI5NjMsImV4cCI6MjA4ODYzODk2M30.BPAYx_hbNI2sSQhUC_BhenQ5Yce0fAsXc33Cpmyn_JM"

supabase = create_client(url, key)

# obtener datos
response = supabase.table("sensor_data").select("*").order("created_at", desc=True).limit(200).execute()
st.write("Últimos datos recibidos:")
st.write(response.data[:5])

data = pd.DataFrame(response.data)

if not data.empty:

    data["created_at"] = pd.to_datetime(data["created_at"])
    data = data.sort_values("created_at")

    ultimo = data.iloc[-1]

    temperatura = ultimo["temperatura"]
    nivel = ultimo["nivel_tanque"]
    corriente = ultimo["corriente"]

    col1, col2, col3 = st.columns(3)

    # temperatura
    with col1:
        st.subheader("Temperatura sala máquinas")
        st.metric("Temperatura", f"{temperatura:.2f} °C")

    # tanque
    with col2:
        st.subheader("Nivel de tanque")
        st.progress(int(nivel))
        st.write(f"{nivel} %")

    # bomba
    with col3:
        st.subheader("Estado de bomba")

        if corriente > 1:
            st.success("BOMBA ENCENDIDA")
        else:
            st.info("BOMBA APAGADA")

        st.write(f"Corriente: {corriente} A")

    st.divider()

    # estado dispositivo
    ahora = datetime.now(ultimo["created_at"].tzinfo)
    diferencia = ahora - ultimo["created_at"]

    if diferencia.total_seconds() < 120:
        st.success("Dispositivo ONLINE")
    else:
        st.error("Dispositivo OFFLINE")

    st.write("Última actualización:", ultimo["created_at"])

    st.divider()

    st.subheader("Histórico de temperatura")

    st.line_chart(data.set_index("created_at")["temperatura"])

else:
    st.warning("No hay datos todavía")