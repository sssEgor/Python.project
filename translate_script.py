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

# Загрузка данных из Excel файла
excel_file = r'C:\Users\user\Desktop\translations.xlsx'
df = pd.read_excel(excel_file)

# Преобразование в PHP-совместимый массив
php_serialized_data = convert_to_php_array(df)

# Вывод сериализованных данных
print(php_serialized_data.decode('utf-8'))
