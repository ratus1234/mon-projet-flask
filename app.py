from flask import Flask, render_template, request, session, redirect, url_for
from random import randint, choice

app = Flask(__name__)
app.secret_key = 'secret_key'

def generate_calculation():
    """Génère un calcul aléatoire."""
    a, b = randint(1, 10), randint(1, 10)
    op = choice(['+', '-', '*'])
    expression = f"{a} {op} {b}"
    result = eval(expression)
    return expression, result

@app.route("/")
def home():
    return "Hello, Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

'''@app.route('/')
#def home():
#    """Page d'accueil avec bouton de démarrage."""
#    session.clear()
#    return render_template('index.html')
'''
@app.route('/play', methods=['GET', 'POST'])
def play():
    """Affiche un calcul et vérifie les réponses."""
    if 'score' not in session:
        session['score'] = 0
        session['count'] = 0
    
    if request.method == 'POST':
        user_answer = request.form.get('answer', '')
        correct_answer = request.form.get('correct', '')

        if user_answer.isdigit() and int(user_answer) == int(correct_answer):
            session['score'] += 1
        
        session['count'] += 1

    if session['count'] >= 10:
        score = session['score']
        return render_template('result.html', score=score)

    question, correct = generate_calculation()
    return render_template('game.html', question=question, correct=correct)

if __name__ == '__main__':
    app.run(debug=True)

