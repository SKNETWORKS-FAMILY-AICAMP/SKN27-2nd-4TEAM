## 목표
- **Docker(Postgres) + DBeaver**로 DB 환경 구성
- **모델 학습**: XGBoost / LightGBM / RandomForest / Logistic Regression / MLP
- 학습된 모델을 **`model/artifacts/`에 파일로 저장**
- **Streamlit**에서 DB 연결 + 예측 확인

---

# 프로젝트 구조 가이드

SKN27-2nd-4TEAM/
├── data/                     # 원본 데이터 (dataset.xlsx)
├── doc/                      # 기획서, WBS, 요구사항 정의서 등 문서
├── FYR/                      # For Your Reference (참고 자료)
├── models/                   # 학습 완료된 모델 저장 (.pkl)
├── src/                      # 소스 코드 메인
│   ├── modeling              # 모델링
│   └── pipeline/             # 공통 전처리 모듈화 (Python Scripts)
│       ├── seed.py           # 재현성을 위한 set_seed()
│       ├── missing_value.py  # 결측치 처리 로직
│       ├── outlier_control.py # 이상치 변환(Log, Clip) 로직
│       └── features.py       # 파생 변수 생성
└── requirements.txt          # 설치 필요한 라이브러리 목록

---

## 0) 사전 준비
- Python **3.11**
- Docker Desktop
- DBeaver

---

## 1) Python 가상환경 & 패키지 설치 (Windows PowerShell)
프로젝트 루트에서 실행:

```bash
uv venv .venv --python 3.11
.\.venv\Scripts\Activate.ps1
uv pip install -r requirements.txt
uv pip install -e .
```

