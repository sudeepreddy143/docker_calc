# 📌 Command Pattern Calculator with REPL, Plugins & Docker

## 📖 Overview
This project implements an **interactive calculator CLI** with:
- ✅ **Command Pattern**
- ✅ **REPL (Read-Eval-Print Loop)**
- ✅ **Dynamic Plugin Loading**
- ✅ **Command Execution Logging (SQLite)**
- ✅ **Docker Support (Devops)**
- ✅ **Multiprocessing**
- ✅ **Structured Logging**
- ✅ **CI/CD with GitHub Actions**

It allows **dynamic command registration**, **logging command history**, and **running inside Docker**.

---

## 🚀 Quick Start

 Setup Virtual Environment (Optional, Recommended)

 ```sh
 python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

 Install Dependencies

```sh
pip install -r requirements.txt
```

Run the Application

```sh
python -m app.repl
```

📌 Running in Docker

🛠 Build & Run

```sh
docker build -t calc_app .
docker run -it --rm calc_app
```

📌 Available Commands
🔹 Basic Commands
Command	Example	Result
add	||
subtract

🔹 Plugin Commands
Command	Example	Result
power ||
square

🔹 Utility Commands
Command	Description
menu	||
history	||
exit	


📌 Running Tests
```sh
pytest tests/
```
