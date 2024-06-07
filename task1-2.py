class Recipe:
    def __init__(self, name_file):
        self.file_cook_book = name_file
        self.cook_book = {}

# Функция по первому заданию
    def getRecipe(self):
        with open(self.file_cook_book, 'r', encoding="utf-8") as f:
            for line in f:
                dish_name = line.strip()
                quantity = int(f.readline())
                temp = []
                for i in range(quantity):
                    ingr = f.readline().split(' | ')
                    ingredients = {'ingredient_name' : ingr[0].strip(), 'quantity': int(ingr[1]), 'measure': ingr[2].strip()}
                    temp.append(ingredients)
                    self.cook_book[dish_name] = temp
                f.readline()
            return self.cook_book

# Функция по второму заданию
    def get_shop_list_by_dishes(self, dishes, person_count):
        c_book = self.getRecipe()
        out = {}
        for dish in dishes:
            if c_book[dish]:
                for q in c_book[dish]:
                    out[q['ingredient_name']] = {'measure': q['measure'], 'quantity': q['quantity'] * person_count}
        return out


# Проверки работы функций

check = Recipe('recipes.txt')

print(check.getRecipe()) # Проверка первого задания
print(check.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)) # Проверка второго задания
