from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "service": "CampusMate API",
        "status": "ok",
        "message": "충남대 AI 챗봇 연동 API 서버입니다."
    }

@app.get("/notices")
def get_notices():
    return {
        "notices": [
            {
                "title": "테스트 공지입니다",
                "category": "학사",
                "date": "2026-06-06",
                "url": "https://plus.cnu.ac.kr"
            }
        ]
    }