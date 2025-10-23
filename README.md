# 🎬 Movie Recommender System (MRS)

A smart and interactive **Movie Recommendation System** built with [Streamlit](https://streamlit.io/).  
This app helps users discover new movies similar to the ones they already love — using a combination of **content-based similarity** and **precomputed feature embeddings** from the TMDB dataset.

---

## 🌐 Live Demo

🎥 **Try it now:**  
👉 [Movie Recommender System (MRS)](https://mrs-fyo8.onrender.com/)

---

## 🧠 Overview

The Movie Recommender System (MRS) leverages the TMDB 5000 Movies and Credits datasets to find similar movies based on features like:

- **Genres**
- **Keywords**
- **Cast & Crew**
- **Overview Text Similarity**

The recommendation engine precomputes movie similarity scores using NLP and vectorization techniques (such as TF-IDF or cosine similarity). These results are serialized into a `.pkl` file for fast runtime predictions in Streamlit.

---

## ✨ Features

- 🔍 **Search any movie** and get top recommended titles instantly.  
- ⚡ **Fast inference** via pre-computed similarity matrix.  
- 🎨 **Beautiful UI** powered by Streamlit.  
- 🧩 **Reusable backend** (can be integrated with Flask or FastAPI if needed).  
- 🖼️ Custom favicon & page title (`static/assets/icon.svg`).  

---

## 🗂️ Project Structure

```
mrs/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── movies_dict.pkl             # Serialized movie data dictionary
├── similarity.pkl              # Precomputed similarity matrix (if used)
├── tmdb_5000_movies.csv        # TMDB Movies dataset
├── tmdb_5000_credits.csv       # TMDB Credits dataset
├── static/
│   └── assets/
│       └── icon.svg            # Custom SVG icon
├── .gitattributes
├── .gitignore
└── README.md                   # Project documentation (this file)
```

---

## ⚙️ Installation & Setup

Follow these steps to get started locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/coreDaemon/mrs.git
cd mrs
```

### 2️⃣ Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate     # For Linux/macOS
# OR
venv\Scripts\activate        # For Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
streamlit run app.py
```

Now open your browser and navigate to [http://localhost:8501](http://localhost:8501) 🎉

---

## 🧩 How It Works

1. **Load Data**  
   - Datasets: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`  
   - Merge and clean relevant columns.

2. **Feature Engineering**  
   - Combine genres, cast, crew, and keywords into a single “tags” column.  
   - Use text vectorization (e.g., CountVectorizer / TF-IDF).

3. **Similarity Computation**  
   - Compute pairwise similarity using cosine similarity.  
   - Store results in `similarity.pkl`.

4. **User Interaction**  
   - User selects a movie from dropdown.  
   - App fetches top similar movies and displays them.

5. **UI Customization**
   ```python
   st.set_page_config(
       page_title="Movie Recommender",
       page_icon="static/assets/icon.svg",
       layout="wide"
   )
   ```

---

## 🧾 Example Usage

When you launch the app:

1. Select or search for a movie (e.g., *Inception*).  
2. The app displays the top 5 most similar movies.  
3. Optionally, it also shows posters of the movies.

---

## 🧠 Future Improvements

- 🤖 Add collaborative filtering (user-based or hybrid recommender).
- 🎭 Display movie posters and details via TMDB API.
- 💾 Integrate database storage for user preferences.
- 🔍 Include genre and keyword filters.
- ☁️ Deploy publicly via Streamlit Cloud or Render.
- 🧪 Add unit tests and GitHub Actions for CI/CD.

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **Backend / Logic** | Python |
| **Data Processing** | Pandas, NumPy, Scikit-learn |
| **Serialization** | Pickle |
| **Visualization** | Streamlit Components |
| **Data Source** | TMDB (The Movie Database) |

---

## 📦 Requirements

Typical dependencies (in `requirements.txt`):
```
streamlit
pandas
numpy
scikit-learn
```

(You can expand this list if you use other libraries.)

---

## 🤝 Contributing

Contributions are welcome!  

To contribute:
1. Fork this repository  
2. Create a new branch:  
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit:  
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your fork:  
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request.

---

## 📜 License

This project is open-source under the **MIT License**.  
Feel free to use, modify, and distribute as you like.

---

## 🙏 Acknowledgements

- [The Movie Database (TMDB)](https://www.themoviedb.org/) for the dataset.  
- [Streamlit](https://streamlit.io/) for the UI framework.  
- [Scikit-learn](https://scikit-learn.org/) for similarity computations.  
- Inspiration from open datasets and ML community tutorials.

---

## 🎉 Screenshots (Optional)

You can include screenshots by saving images under `static/screenshots/` and embedding them here:

```markdown
![Home Page](static/screenshots/home.png)
![Recommendations](static/screenshots/recommendations.png)
```

---

## 💬 Author

**coreDaemon**  
GitHub: [@coreDaemon](https://github.com/coreDaemon)  
Project Link: [https://github.com/coreDaemon/mrs](https://github.com/coreDaemon/mrs)

---

> “Good movies inspire us — great recommendations help us find them.”
