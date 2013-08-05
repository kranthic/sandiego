__author__ = 'kranthi'


from flask import Flask, render_template, request
import storage

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form_status = ''
    show_form_status = False
    if request.method == 'POST':
        form_status = 'Form Submitted'
        show_form_status = True

        obj = storage.Parser_Form_Data()
        obj.file = request.files['recipe_file'].filename
        obj.parser = request.form['parser']
        obj.recipe = request.form['recipe']
        obj.status = 'Submitted'
        obj.title = request.form['recipe_title']
        obj.website = request.form['recipe_site']

        storage.store_parser_form_data(obj, request.files['recipe_file'].stream)


    return render_template('form.html', form_status=form_status, show_form_status=show_form_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)