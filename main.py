import matplotlib.pyplot as plt

data = {'Смартфон':251,'Компьютер':340,'Планшет':36,'Тв':10}

def percent(arr):
    return [i/sum(arr)*100 for i in arr]


def test_arr(arr):
    return  list(arr.keys()),list(arr.values())

def table (arr):
    if type(arr) != dict:
        raise TypeError
    index, values = test_arr(arr)
    plt.title('Analyze')
    plt.xlabel('Structure')
    plt.ylabel('Number')
    plt.bar(index,percent(values))
    plt.show()

if __name__ == '__main__':
    table(data)