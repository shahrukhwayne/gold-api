## Gold Investment API

Gold Investment API is an interactive project built for the **Simplify Money Software Engineering Internship**. It allows users to ask questions about gold investment, respond to prompts, and make gold purchases, all tracked in a SQLite database. The API is built using **FastAPI** and hosted on **Render** for easy public testing.

---

## Deployment Link
Test the live API here:  
[https://gold-api.onrender.com](https://gold-api.onrender.com)

---

## Project Description
This API simulates a conversational workflow where users can inquire about gold investments, respond to guidance prompts, and make purchases. The main features include:

- Asking questions about gold investments.
- Receiving AI-like guidance.
- Confirming purchases via responses.
- Saving purchase information in a database.
- Tracking conversation state per user in memory.

---

## API Workflow & Usage

## 1. Check API Status
- **Endpoint:** `/`  
- **Method:** `GET`  
- **Description:** Verify if the API is running.  
- **Response Example:**
```json
{
  "message": "Gold Investment API is running 🚀"
}
```
## 2. Ask About Gold
- **Endpoint:** `/ask`
- **Method:** `POST`

**Request Body Example:**
```json
{
  "user_id": "shahrukh123",
  "question": "Should I invest in gold?"
}
```
**Response:**
```json
{
  "answer": "Gold is a safe long-term investment. 📈",
  "nudge": "Do you want to purchase digital gold now? (yes/no)"
}
```
## 3. Respond to Prompt ##

- **Endpoint:** `/respond`

- **Method:** `POST`

***Request Body Example:***
```json
{
  "user_id": "shahrukh123",
  "response": "yes"
}
```

***Response Example (yes):***
```json
{
  "message": "Great! Redirecting you to gold purchase API... 🚀"
}
```

***Response Example (no):***
```json
{
  "message": "No problem 👍. Let me know if you change your mind."
}
```


***Users must respond "yes" to proceed with purchase.***

##4. Purchase Gold##

- **Endpoint:** `/purchase`

- **Method:** `POST`

**Request Body Example:**
```json
{
  "user_id": "shahrukh123",
  "amount": 15000
}
```


**Response Example:**
```json
{
  "message": "Gold purchase successful for shahrukh123, amount = 15000 INR 🚀"
}
```


# Running Locally

**1.Clone the repo:**

`git clone https://github.com/shahrukhwayne/gold-api`

**2.Navigate to project folder:**

`cd gold-api`

**3.Install dependencies:**

```
pip install -r requirements.txt
# OR if using Poetry:
poetry install
```


**4.Start the server:**

`uvicorn main:app --reload`


**5.Open API in browser or Postman:**

`http://127.0.0.1:8000`

# Project Structure
```
gold-api/
│
├─ main.py           # FastAPI app with all endpoints
├─ gold.db           # SQLite database
├─ requirements.txt  # Dependencies
└─ README.md         # This file
```

# Approach

- Built a conversational workflow simulating AI guidance on gold investments.

- Used SQLite to save user purchases.

- Implemented three main endpoints: ask → respond → purchase.

- Hosted on Render for easy public access.

- Code is modular for maintainability and scalability.

# Challenges / Notes

- Initial deployment failed due to missing requirements.txt; resolved by placing it in the root directory.

- Ensured user consent before saving purchases.

- Tested all endpoints extensively using Postman.

# Author
- **Author:** **Mohd Shahrukh**
- **Internship**: **Simplify Money - Software Engineering Intern (AI track).**
- **GitHub:** `https://github.com/shahrukhwayne`
