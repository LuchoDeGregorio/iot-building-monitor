from supabase import create_client

url = "https://anwwqipwfcfycravtxvb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFud3dxaXB3ZmNmeWNyYXZ0eHZiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMwNjI5NjMsImV4cCI6MjA4ODYzODk2M30.BPAYx_hbNI2sSQhUC_BhenQ5Yce0fAsXc33Cpmyn_JM"

supabase = create_client(url, key)

response = supabase.table("sensor_data").select("*").limit(5).execute()

print(response)