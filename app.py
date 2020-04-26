import random
from flask import Flask, render_template
from algodspy.bubble_sort import BubbleSort
from algodspy.insertion_sort import InsertionSort
from algodspy.heap_sort import HeapSort
from algodspy.quick_sort import QuickSort
from algodspy.radix_sort import RadixSort
from algodspy.selection_sort import SelectionSort


app = Flask(__name__)

sortings = {
    'data': [],
    'data_str': '',
    'sortings': [
        {'name': 'Сортировка пузырьком', 'sorter': BubbleSort()},
        {'name': 'Сортировка вставками', 'sorter': InsertionSort()},
        {'name': 'Пирамидальная сортировка', 'sorter': HeapSort()},
        {'name': 'Быстрая сортировка', 'sorter': QuickSort()},
        {'name': 'Поразрядная сортировка', 'sorter': RadixSort()},
        {'name': 'Сортировка выбором', 'sorter': SelectionSort()},
    ]
}

def generate_data():
    return [random.randint(-10, 10) for _ in range(10)]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data-structures/')
def data_structures():
    return render_template('data-structures.html')

@app.route('/sortings/')
def sorting():
    data = generate_data()
    sortings['data'] = data
    sortings['data_str'] = ' '.join([str(x) for x in data])
    for sorting in sortings['sortings']:
        sorting['result'] = ' '.join([str(x) for x in sorting['sorter'].sort(data)])
    return render_template('sorting.html', context=sortings)

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)