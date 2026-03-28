## 목표
- **Docker(Postgres) + DBeaver**로 DB 환경 구성
- **모델 학습**: XGBoost / LightGBM / RandomForest / Logistic Regression / MLP
- 학습된 모델을 **`model/artifacts/`에 파일로 저장**
- **Streamlit**에서 DB 연결 + 예측 확인

---

# 프로젝트 구조 가이드

## app/

* Streamlit UI 코드
* 사용자 입력 및 예측 결과 시각화 담당

---

## src/

### db/

* DB 연결 코드
* SQLAlchemy engine 관리

### feature/

* 파생 변수 생성
* feature engineering 로직

### missing_value/

* 결측치 처리 로직

### pipeline/

* 데이터 전처리 흐름 정의
* feature + missing_value를 순서대로 실행

---

## models/

* 학습된 모델 저장 (.pkl, joblib)
* 예: lgbm_v1.pkl

---

## data/

* 원본 데이터 및 전처리 데이터

---

## doc/

* 기획서, 요구사항 정의서, WBS 등 프로젝트 문서

---

## .env

* 실제 환경 변수 (비공개, git 제외)

## .env.example

* 환경 변수 템플릿 (공유용)

---

## docker-compose.yml

* Postgres 및 서비스 컨테이너 설정

---

## requirements.txt

* 프로젝트 의존성 관리


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
pip install -r requirements.txt
```

