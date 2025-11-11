from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

temario = [
    {"nivel": 1, "ciudad": "Bogotá", "pregunta": "¿Cuál es el sinónimo de 'feliz'?", "opciones": ["Triste", "Contento", "Lento"], "respuesta": "Contento"},
    {"nivel": 2, "ciudad": "Medellín", "pregunta": "¿Cuál es el antónimo de 'rápido'?", "opciones": ["Veloz", "Ligero", "Lento"], "respuesta": "Lento"},
    {"nivel": 3, "ciudad": "Cali", "pregunta": "¿Qué palabra es un sustantivo?", "opciones": ["Correr", "Mesa", "Alegre"], "respuesta": "Mesa"},
    {"nivel": 4, "ciudad": "Barranquilla", "pregunta": "¿Cuál es el verbo en la oración: 'El perro corre rápido'?", "opciones": ["Perro", "Corre", "Rápido"], "respuesta": "Corre"},
    {"nivel": 5, "ciudad": "Cartagena", "pregunta": "¿Qué palabra es un adjetivo?", "opciones": ["Azul", "Saltar", "Casa"], "respuesta": "Azul"},
    {"nivel": 6, "ciudad": "Bucaramanga", "pregunta": "¿Cuál es el plural de 'lápiz'?", "opciones": ["Lápices", "Lápizs", "Lápizes"], "respuesta": "Lápices"},
    {"nivel": 7, "ciudad": "Pereira", "pregunta": "¿Qué palabra es un verbo?", "opciones": ["Saltar", "Mesa", "Azul"], "respuesta": "Saltar"},
    {"nivel": 8, "ciudad": "Manizales", "pregunta": "¿Cuál es el diminutivo de 'flor'?", "opciones": ["Florecita", "Florita", "Florcita"], "respuesta": "Florcita"},
    {"nivel": 9, "ciudad": "Santa Marta", "pregunta": "¿Qué palabra es un pronombre?", "opciones": ["Ellos", "Casa", "Correr"], "respuesta": "Ellos"},
    {"nivel": 10, "ciudad": "Cúcuta", "pregunta": "¿Cuál es el aumentativo de 'perro'?", "opciones": ["Perrón", "Perrote", "Perrito"], "respuesta": "Perrote"},
]

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/pregunta/<int:nivel>', methods=['GET', 'POST'])
def pregunta(nivel):
    if nivel > len(temario):
        return render_template('fin.html')

    actual = temario[nivel - 1]

    if request.method == 'POST':
        respuesta_usuario = request.form.get('respuesta')
        if respuesta_usuario == actual["respuesta"]:
            return redirect(url_for('pregunta', nivel=nivel + 1))
        else:
            return render_template('pregunta.html', pregunta=actual, error=True)

    return render_template('pregunta.html', pregunta=actual, error=False)

@app.route('/fin')
def fin():
    return "<h1>🎉 ¡Felicidades! Has llegado a la meta, en esta ciudad està el tesoro literario </h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
