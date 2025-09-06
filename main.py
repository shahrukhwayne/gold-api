import sqlite3
from fastapi import FastAPI, Request

app = FastAPI()

conn = sqlite3.connect("gold.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    amount REAL,
    status TEXT
)
""")

conn.commit()

# In-memory conversation store
conversations = {}

@app.get("/")
def home():
    return {"message": "Gold Investment API is running 🚀"}

@app.post("/ask")
async def ask_user(request: Request):
    data = await request.json()
    user_id = data.get("user_id", "default")  # user id lena zaroori hai
    question = data.get("question", "").lower()

    if "gold" in question:
        conversations[user_id] = "asked_about_gold"  # memory save ho rahi hai
        return {
            "answer": "Gold is a safe long-term investment. 📈",
            "nudge": "Do you want to purchase digital gold now? (yes/no)"
        }
    else:
        conversations[user_id] = "other"
        return {"answer": "I can only answer about gold investments."}

@app.post("/respond")
async def respond_user(request: Request):
    data = await request.json()
    user_id = data.get("user_id", "default")
    user_response = data.get("response", "").lower()

    # check memory
    if conversations.get(user_id) == "asked_about_gold":
        if user_response in ["yes", "y"]:
            conversations[user_id] = "buying_gold"
            return {"message": "Great! Redirecting you to gold purchase API... 🚀"}
        else:
            conversations[user_id] = "not_buying"
            return {"message": "No problem 👍. Let me know if you change your mind."}
    else:
        return {"message": "Please ask about gold investment first."}
    

@app.post("/purchase")
async def purchase_gold(request: Request):
    data = await request.json()
    user_id = data.get("user_id", "default")
    amount = data.get("amount", 10)  # default 10 INR

    # ✅ Check user consent first
    if conversations.get(user_id) != "buying_gold":
        return {"error": "Please confirm purchase first by saying yes."}

    # Save to DB
    cursor.execute(
        "INSERT INTO purchases (user_id, amount, status) VALUES (?, ?, ?)",
        (user_id, amount, "success")
    )
    conn.commit()

    # Update memory (optional)
    conversations[user_id] = "purchased"

    return {"message": f"Gold purchase successful for {user_id}, amount = {amount} INR 🚀"}
