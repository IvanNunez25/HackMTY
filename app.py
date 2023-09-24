from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import sqlite3

app = Flask(__name__)

# Conectar a la base de datos SQLite
conn = sqlite3.connect('banorte_database.db')
cursor = conn.cursor()

# Cargar opiniones desde la base de datos
cursor.execute("SELECT fondo, caracteristicas FROM fondo_de_inversion")
caracteristicas = cursor.fetchall()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    # Obtener la consulta del usuario
    query = request.form['query']
    #query = 'una'

    # Asegurarse de que la consulta no esté vacía
    if not query:
        return render_template('index.html', query='', recommended_movies=[])

    # Crear una lista de opiniones como texto plano
    caracteristicas_texto = [caracteris[1] for caracteris in caracteristicas]

    # Crear una matriz TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(caracteristicas_texto)

    # Calcular similitud coseno entre la consulta y las opiniones
    cosine_sim = linear_kernel(tfidf_vectorizer.transform([query]), tfidf_matrix)

    # Obtener las películas recomendadas basadas en la similitud
    sim_scores = list(enumerate(cosine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    recommended_fund = []

    for i, score in sim_scores:
        if score > 0.0:
            recommended_fund.append(caracteristicas[i][0])

    return render_template('index.html', query=query, recommended_movies=recommended_fund)

if __name__ == '__main__':
    app.run(debug=True)




