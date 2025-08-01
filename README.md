# 🎧 Moodify — A Mood-Based Music Recommender

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey)
![TextBlob](https://img.shields.io/badge/TextBlob-Sentiment-yellowgreen)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

Moodify is a mood-based music recommender that analyzes user input using sentiment analysis and suggests playlists accordingly. Built with Flask and TextBlob, it offers a simple API to detect emotional tone and map it to music genres.

---

## 🚀 Features

- 🔍 Sentiment analysis using TextBlob
- 🎶 Mood-to-music mapping
- 🧠 Simple Flask API
- 📦 Easy to extend with Spotify or YouTube APIs

---

## 🛠️ Installation


git clone https://github.com/BEASTROHO/Moodify-A-Mood-Based-Music-Recommender.git
cd Moodify-A-Mood-Based-Music-Recommender
pip install -r requirements.txt
python app.py
Here’s your full updated **README.md** with the MIT License section included at the bottom:





## 📡 API Usage

### Endpoint

```
POST /analyze
```

### Request

```json
{
  "text": "I feel relaxed and peaceful"
}
```

### Response

```json
{
  "mood": "Content"
}
```

---

## 🧪 Testing

```bash
curl -X POST http://127.0.0.1:5000/analyze \
-H "Content-Type: application/json" \
-d '{"text":"I feel energetic and joyful"}'
```

---

## 🧭 Roadmap

- [ ] 🎨 React frontend
- [ ] 🎧 Spotify API integration
- [ ] 🧠 ML-based mood classifier
- [ ] 📊 Dashboard for mood trends

---

## 📄 License

MIT License

Copyright (c) 2025 Roho

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

---

You can now paste this directly into your GitHub README editor [here](https://github.com/BEASTROHO/Moodify-A-Mood-Based-Music-Recommender/edit/main/README.md).

Want a `.gitignore` next or a mock playlist recommender based on the mood output?
