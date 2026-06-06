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
                "title": "2026학년도 수강신청 안내",
                "category": "학사",
                "date": "2026-06-01",
                "url": "https://plus.cnu.ac.kr"
            },
            {
                "title": "국가장학금 신청 안내",
                "category": "장학",
                "date": "2026-05-30",
                "url": "https://plus.cnu.ac.kr"
            }
        ]
    }
