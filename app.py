from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnosis', methods=['GET', 'POST'])
def diagnosis():
    result = None
    if request.method == 'POST':
        answers = [int(request.form.get(f'q{i}', 0)) for i in range(1, 11)]
        age = int(request.form.get('months', 0))
        score = sum(answers)
        if score > 5 and age < 36:
            result = "High likelihood of ASD"
        else:
            result = "Low likelihood of ASD"
    return render_template('diagnosis.html', result=result)

@app.route('/therapy', methods=['GET', 'POST'])
def therapy():
    confirmation = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        therapy_type = request.form.get('therapy')
        time = request.form.get('time')
        confirmation = {'email': email}
    return render_template('therapy.html', confirmation=confirmation)

@app.route('/funds', methods=['GET', 'POST'])
def funds():
    confirmation = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        amount = request.form.get('amount')
        message = request.form.get('message')
        confirmation = {'email': email}
    return render_template('funds.html', confirmation=confirmation)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
