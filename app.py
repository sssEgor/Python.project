from flask import Flask, render_template, request
import os

app = Flask(__name__)

import pandas as pd
import phpserialize

def convert_to_php_array(df):
    php_array = {}

    for index, row in df.iterrows():
        key = row['Key']
        lang = row['Language']
        translation = row['Value']

        if key not in php_array:
            php_array[key] = {}

        php_array[key][lang] = translation

    return phpserialize.dumps(php_array)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Обработка загруженного файла
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        df = pd.read_excel(uploaded_file)
        php_serialized_data = convert_to_php_array(df)
        return php_serialized_data.decode('utf-8')

if __name__ == '__main__':
    app.run(debug=True)

