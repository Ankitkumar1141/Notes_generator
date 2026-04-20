# 🚀 AI Notes Generator

An end-to-end AI-powered web application that generates structured study notes from PDF documents using **Mistral AI**, built with **Streamlit**, **MySQL**, and fully containerized using **Docker**.

---

## 📌 Features

* 🔐 User Authentication (Register & Login)
* 📄 Upload PDF files
* 🧠 Extract text from PDFs
* 🤖 Generate structured notes using Mistral AI
* 🗄️ MySQL database integration
* 🐳 Fully Dockerized (App + Database)
* 🧪 Modular architecture with testable components

---

## 🏗️ Project Structure

```
AI_NOTES/
│
├── src/
│   └── ai_notes_generator/
│       ├── __init__.py
│       ├── config.py          # Environment & configuration
│       ├── db.py              # Database connection
│       ├── auth_service.py    # Authentication logic
│       ├── pdf_utils.py       # PDF text extraction
│       ├── ai_service.py      # Mistral AI integration
│       └── main.py            # Streamlit app
│
├── test/                      # Test scripts
├── .env                       # Environment variables (not committed)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## ⚙️ Tech Stack

* **Frontend/UI**: Streamlit
* **Backend**: Python
* **Database**: MySQL
* **AI Model**: Mistral AI
* **Containerization**: Docker & Docker Compose

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
MISTRAL_API_KEY=your_mistral_api_key
DB_HOST=mysql
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=ai_notes
```

---

## 🐳 Running with Docker (Recommended)

### 🔹 Step 1: Build & Run

```bash
docker compose up --build
```

### 🔹 Step 2: Open App

```
http://localhost:8501
```

---

## 💻 Running Locally (Without Docker)

### 🔹 Step 1: Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 🔹 Step 2: Install dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

### 🔹 Step 3: Run MySQL

Ensure MySQL is running and database exists:

```sql
CREATE DATABASE ai_notes;
```

### 🔹 Step 4: Run app

```bash
streamlit run src/ai_notes_generator/main.py
```

---

## 🧪 Running Tests

```bash
python test/test_db_connection.py
python test/test_auth.py
python test/test_ai.py
```

---

## 🚀 Usage

1. Register a new user
2. Login with credentials
3. Upload a PDF file
4. Click **Generate Notes**
5. View AI-generated structured notes

---

## ⚠️ Known Limitations

* Passwords are stored in plain text (not suitable for production)
* No user session persistence beyond Streamlit session
* No note history storage (future enhancement)

---

## 🔮 Future Improvements

* 🔒 Add password hashing (bcrypt)
* 📝 Save generated notes to database
* 📊 Add user dashboard/history
* ⚡ Switch to FastAPI backend for scalability
* ☁️ Deploy to cloud (AWS / Render / Railway)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Your Name**

---

## ⭐ If you found this useful

Give this repo a ⭐ to support the project!
