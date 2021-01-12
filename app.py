from flask import Flask, render_template, request 

app = Flask(__name__) #создаем объект Flask, передаем имя активного модуля

@app.route('/') 
def hello() -> str:
	return 'Hello world from Flask!'   
   
@app.route('/search',  methods=['POST']) #добавили метод POST
def search()->'html':
    letters = set(request.form['letters'])
    word = request.form ['phrase'] 
    found = letters.intersection(set(word.lower()))# добавили lower(), чтобы не учитывать регистр
    title = 'Вы ввели следующие данные:'
    result = str(found)
    return render_template('results.html',
        the_title = title,
        the_phrase = word,
        the_letters = letters,
        the_results = result,
        )

@app.route('/entry') 
def entry()->'html':
	return render_template('entry.html',
        the_title='ПРИВЕТСТВУЕМ ВАС НА САЙТЕ, ВЫПОЛНЯЮЩЕМ ПОИСК БУКВ В СТРОКАХ!')
    
app.run(debug = True)