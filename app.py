# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import socket
from datetime import datetime

app = FastAPI()

WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast?latitude=23.8103&longitude=90.4125&current_weather=true"

class WeatherData(BaseModel):
    temperature: str
    temp_unit: str

class ResponseModel(BaseModel):
    hostname: str
    datetime: str
    version: str
    weather: dict

@app.get("/api/hello", response_model=ResponseModel)
async def hello():
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(WEATHER_API_URL, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            temperature = str(data["current_weather"]["temperature"])
            temp_unit = "c"  # Celsius assumed by open-meteo API

    except Exception as e:
        # fallback if weather API call fails
        temperature = "N/A"
        temp_unit = "N/A"

    hostname = socket.gethostname()
    now_str = datetime.utcnow().strftime("%y%m%d%H%M")

    return {
        "hostname": hostname,
        "datetime": now_str,
        "version": "1.0",
        "weather": {
            "dhaka": {
                "temperature": temperature,
                "temp_unit": temp_unit
            }
        }
    }

@app.get("/api/health")
async def health_check():
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(WEATHER_API_URL, timeout=5)
            resp.raise_for_status()
    except Exception:
        raise HTTPException(status_code=503, detail="Weather API unreachable")

    return {"status": "healthy"}

