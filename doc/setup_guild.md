## 목표
- **Docker(Postgres) + DBeaver**로 DB 환경 구성
- **모델 학습**: XGBoost / LightGBM / RandomForest / Logistic Regression / MLP
- 학습된 모델을 **`model/artifacts/`에 파일로 저장**
- **Streamlit**에서 DB 연결 + 예측(추후 확장) 확인

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
