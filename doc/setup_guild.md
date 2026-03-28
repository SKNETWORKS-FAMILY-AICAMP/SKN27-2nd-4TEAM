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

---

## 2) 환경변수(.env) 준비
`.env`는 **커밋 금지**입니다. 예시는 `.env.example` 참고.
`.env.example`를 복사하여 이름을 `.env`로 변경

기본값(로컬에서 Streamlit 실행 기준):
- `DB_HOST=localhost`
- `DB_PORT=5432`
- `DB_NAME=churn_db`
- `DB_USER=user`
- `DB_PASSWORD=password`

---

## 3) Postgres 실행 (Docker)
```bash
docker compose up -d
docker compose ps
```
---

## 4) DBeaver 연결
새 연결 → PostgreSQL:
- **Host**: `db`
- **Port**: `5432`
- **Database**: `churn_db`
- **Username**: `user`
- **Password**: `password`

---

## 5) DB 연결 테스트 (Streamlit)
```bash
streamlit run app/streamlit_test.py
```

페이지에서
- **DB 핑(SELECT 1)**
- **버전 확인(SELECT version())**
- 임의 SQL 실행
을 통해 연결 여부를 확인합니다.

---

## 6) 모델 학습 & 저장
현재는 “파이프라인/저장 포맷”을 먼저 고정하기 위해 샘플 데이터셋으로 학습합니다.

```bash
python model/train_models.py --out model/artifacts
```
