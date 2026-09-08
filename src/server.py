import os
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="msg-relay-node2", description="AS Cloud High-Availability Standby Live Messaging Relay Node 2", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

START_TIME = time.time()

@app.get("/")
def root():
    return {
        "service": "msg-relay-node2",
        "status": "online",
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "cluster": "AS-Cloud-Messages",
        "restart_cycle": "5h-managed"
    }

@app.get("/health")
def health():
    return {"status": "ok", "service": "msg-relay-node2", "timestamp": time.time()}
