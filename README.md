# Iron-Lady-Chatbot
Iron-Lady-Chatbot is a web-based chatbot application designed to provide information about Iron Lady's leadership programs for women. Users can ask FAQs about programs, duration, certificates, mentors, and more. The chatbot interface is clean, mobile-friendly, and interactive.

## Features
- **Responsive Design:** The chatbot interface works seamlessly across desktop, tablet, and mobile devices.
- **Interactive Chat:** Users can type questions and receive answers instantly from the chatbot.
- **Typing Animation:** Shows a subtle typing animation to mimic real-time interaction.
- **FAQs Covered:** Includes program details, duration, online/offline mode, certificates, mentors, and cost.
- **Custom Watermark & Background:** Features a stylish Iron Lady watermark and a professional background image.
- **Backend API:** Developed using Flask to handle user queries and return responses.
- **Easy Extensibility:** FAQs are stored in Python dictionaries and can be easily updated or expanded.

## Technologies Used
### Frontend:
- **HTML5 & CSS3:** For structuring and styling the chatbot interface.
- **JavaScript:** For interactive chat behavior and animations.

### Backend:
- **Python & Flask:** For handling backend requests and serving chatbot responses.
- **Requests (Optional):** To fetch data from external APIs if extended.

## Installation and Setup
To run Iron-Lady-Chatbot locally, follow these steps:

### Clone the Repository
```bash
git clone https://github.com/BimbaSiri/Iron-Lady-Chatbot.git
cd Iron-Lady-Chatbot

Install Dependencies

Make sure you have Python installed. Then install Flask (and Requests if using APIs):
pip install Flask
pip install requests
Create Environment File
Inside the project folder, create a .env file and add your own OpenAI API key:

env
Copy code
OPENAI_API_KEY=your_api_key_here
⚠️ Do not share your .env file or API key publicly.

Run the Application
python app.py

Access the Chatbot

Open your browser and visit:
http://127.0.0.1:5000

Project Structure

Iron-Lady-Chatbot/
│
├── app.py              # Flask backend
├── templates/
│   └── index.html      # Main HTML file
├── static/
│   ├── css/
│   │   └── style.css   # Stylesheet for the chatbot
│   └── images/
│       ├── ironlady.jpg       # Background image
│       ├── before_chatting.png # Screenshot before chatting
│       └── after_chatting.png  # Screenshot after chatting
└── README.md           # Project documentation

## Screenshots

### Before Chatting
![Before Chatting](static/images/screenshot_before.png)

### After Chatting
![After Chatting](static/images/screenshot_after.png)


Future Enhancements
Integrate real-time AI-based responses using OpenAI or other NLP APIs.

Add multi-language support.

Include user authentication to save chat history.

Enhance UI/UX with advanced animations and themes.