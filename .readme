# 💰 FastAPI Wallet

A simple financial transaction tracking service built with FastAPI and PostgreSQL.

---

## 🚀 Features

- Add income and expense transactions
- Filter transactions by type
- Sort transactions by date
- Get balance reports
- Get detailed reports grouped by minute (date + time)

---

## 🛠 Tech Stack

- **FastAPI** – API framework
- **SQLAlchemy (async)** – ORM
- **PostgreSQL** – Database
- **Alembic** – DB migrations
- **Pydantic v2** – Data validation
- **Uvicorn** – ASGI server

---

## 📦 Installation

```bash
git clone https://github.com/your-username/fastapi-wallet.git
cd fastapi-wallet
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Update your database credentials in `db/database.py`:

```python
DATABASE_URL = "postgresql+asyncpg://<username>:<password>@localhost:5432/<database>"
```

---

## 📋 Database Migrations

```bash
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

---

## ▶️ Run the App

```bash
uvicorn main:app --reload
```

Access it at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 API Endpoints

### `/transactions/`

- `POST /` → Create new transaction
- `GET /` → List transactions with optional filters

### `/reports/`

- `GET /balance/` → Get total income, expense, and balance
- `GET /detailed/` → Get detailed report grouped by minute

---

## 🧪 Testing (Coming Soon)

---

## 📄 License

MIT License