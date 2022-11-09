from flask import Flask, render_template, url_for, request, flash,redirect
import os
import obrabotka

app = Flask(__name__)
app.config["SECRET_KEY"] = 'IPDJFGHBOLKFSKLGNSLAWEJFPOSDJFGOB'

@app.route('/' , methods=['GET', 'POST'])
@app.route('/home' , methods=['GET', 'POST'])
def index():
    obrabotka.clearing_folder()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Файл не выбран')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        file = request.files['file']
        file.save(os.path.join('static/upload',file.filename))
        flash('Загружено')
        return redirect('/result')
    return render_template('main.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    pred,path,digit_cls = obrabotka.get_info(obrabotka.predproc())
    
    # pred = 1
    return render_template('result.html', data= pred,path = path, digit_cls = digit_cls )

@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return "User page " + name +" - " + str(id) 

if __name__ == "__main__":
    app.run(debug=True)