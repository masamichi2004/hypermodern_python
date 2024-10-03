from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

class CorsConfig():
    def __init__(self, app: FastAPI):
        self.app = app

    def apply(self):
        self.__cors_config()
        
    def __cors_config(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )