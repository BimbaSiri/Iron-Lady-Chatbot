from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# --- Detailed FAQs ---
faqs = {
    "programs": """Iron Lady offers transformative leadership programs designed for women, including:
- Leadership Essentials Program
- 100 Board Members Program
- Master of Business Warfare
- LinkedIn Masterclass
- Champions Program
- Executive Presence Masterclass
These programs empower women to fast-track their careers and break barriers.""",

    "duration": """Program durations vary:
- Leadership Essentials Program: 2 days
- Master of Business Warfare: 2 days
- LinkedIn Masterclass: 2 days
- 100 Board Members Program: 6 weeks
- Champions Program: Ongoing with community support""",

    "online": "All Iron Lady programs are conducted online, offering flexibility and accessibility.",

    "certificates": "Yes, participants receive certificates upon successful completion of the programs.",

    "mentors": """Programs are led by experienced mentors and coaches including:
- Rajesh Bhat – Founder and Director
- Suvarna Hegde – Founder & CEO
- Simon Newman – Ex-CEO of Aviva Singapore
- Sridhar Sambandam – Ex-CEO of Bajaj Auto""",

    "age": "There is no specific age limit; programs are tailored for women who want to fast-track their careers or grow their businesses.",

    "cost": "Program costs vary. Some programs have promotional discounts; e.g., Master of Business Warfare is currently ₹129 (original ₹499).",

    "registration": "You can register through the official Iron Lady website by selecting your program and completing registration."
}

# --- Home route ---
@app.route('/')
def index():
    return render_template('index.html')


# --- Chatbot route ---
@app.route('/get', methods=['POST'])
def get_bot_response():
    user_msg = request.form.get('msg').lower()

    # First, try to answer from FAQs
    for key in faqs:
        if key in user_msg:
            return faqs[key]

    # If not in FAQs, try scraping official website (fallback)
    try:
        url = "https://www.ironlady.in"  # official Iron Lady website
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = " ".join([p.get_text() for p in paragraphs])

        # Simple keyword match in website content
        for word in user_msg.split():
            if word.lower() in content.lower():
                return content[:500] + "..."  # return first 500 chars
    except Exception as e:
        print("Error fetching from website:", e)

    return "Sorry, I don't have an answer for that. Please check the official Iron Lady website."


if __name__ == "__main__":
    app.run(debug=True)
