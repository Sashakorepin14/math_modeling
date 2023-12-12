import random

def flower():
    flowers = ['Роза', 'Тюльпан', 'Лилия']
    colors = ['Красный', 'Желтый', 'Синий', 'Белый', 'Розовый']

    flower_colors = dict(zip(flowers, random.sample(colors, len(flowers))))
    return flower_colors
print(flower())