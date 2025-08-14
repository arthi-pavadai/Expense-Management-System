# 💰 Expense Management System
This project is designed to record, manage, and analyze expenses, enabling users to identify spending patterns and make informed decisions to control costs.

The system is structured to efficiently add or update expense records and provides a comprehensive summary with visualizations for better financial insights.

## 🏗 Architecture

```plaintext
          ┌──────────────┐
          │   Streamlit  │  <-- Frontend UI
          └───────┬──────┘
                  │ HTTP Requests
                  ▼
          ┌──────────────┐
          │   FastAPI    │  <-- Backend API
          └───────┬──────┘
                  │ PyMySQL
                  ▼
          ┌──────────────┐
          │  SQL DB      │  <-- Data Storage
          └──────────────┘
```

✨ Features

📊 Interactive Dashboard for expense visualization

⚡ FastAPI backend for speedy and reliable API responses

🗄 SQL database for persistent storage

🧪 Pytest for automated testing

📜 Logging for error tracking and monitoring

##  Project Structure

<img width="143" height="247" alt="image" src="https://github.com/user-attachments/assets/aa336030-3fd0-4d1f-85dd-c229145206ee" />
