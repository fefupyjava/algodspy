from flask import Flask
from algodspy.selection_sort import SelectionSort


app = Flask(__name__)

@app.route('/')
def index():
    string = '''<h1>Алгоритмы и структуры данных на пальцах</h1>
    <p><a href="/selection-sort">Сортировка выбором</a></p>
    '''
    return string

@app.route('/selection-sort/')
def selection_sort():
    data = [1, 4, 7, 8, 10, 3, 5, 4]
    sorter = SelectionSort()
    data_sorted = sorter.sort(data)
    string = f'<div>Массив для сортировки выбором: {data}</div>'
    string += f'<div>Отсортированный массив: {data_sorted}</div>'
    string += f'<div><a href="/">На главную</a></div>'
    return string


if __name__ == '__main__':
    app.run(threaded=True, port=5000)