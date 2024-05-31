import tkinter as tk
class IceCreamStand:

    def __init__(self, n, t, o, flavors, location):
        self.name = n
        self.type = t
        self.flavors = flavors
        self.location = location
        self.open = o

    def display_info(self):
        print(f"Название кафе-мороженого: {self.name}")
        print(f"Тип кухни: {self.type}")
        print("Список сортов мороженого:")
        for flavor in self.flavors:
            print(flavor)
        print(f"Локация: {self.location}")
        print(f"Время работы: {self.open}")

    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
        print(f"Сорт мороженого '{new_flavor}' добавлен.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт мороженого '{flavor}' удален.")
        else:
            print(f"Этого сорта мороженого '{flavor}' нет.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт мороженого '{flavor}' есть.")
        else:
            print(f" '{flavor}' мороженое отсутствует.")

    def serve_ice_cream(self, type_of_ice_cream):
        print(f"Подаю {type_of_ice_cream} мороженое.")

res1 = IceCreamStand("Фортескью", "Кафе-мороженое", "работают с 10:00 до 23:00", ['пломбир', 'крем-брюле', 'шербет', 'фруктовый лёд'], "набережная Адмиралтейского канала, 17")
res1.display_info()
res1.add_flavor("шоколадное")
res1.remove_flavor("клубничное")
res1.check_flavor("ваниль")
res1.serve_ice_cream("Мороженое в рожке")
res1.serve_ice_cream("Мороженое в стаканчики")

class IceCreamStand:
    def __init__(self, master):
        self.master = master
        self.master.title("Ice Cream Stand")

        self.flavors = ['пломбир', 'крем-брюле', 'шербет', 'фруктовый лёд']
        self.selected_flavor = tk.StringVar(value=self.flavors[0])

        self.types = ["Мороженое в рожке", "Мороженое в стаканчики"]
        self.selected_type = tk.StringVar(value=self.types[0])

        self.flavor_label = tk.Label(master, text="Выберите сорт мороженого:")
        self.flavor_label.pack()

        self.flavor_option = tk.OptionMenu(master, self.selected_flavor, *self.flavors)
        self.flavor_option.pack()

        self.type_label = tk.Label(master, text="Выберите тип мороженого:")
        self.type_label.pack()

        self.type_option = tk.OptionMenu(master, self.selected_type, *self.types)
        self.type_option.pack()

        self.order_button = tk.Button(master, text="Заказать", command=self.place_order)
        self.order_button.pack()

    def place_order(self):
        flavor = self.selected_flavor.get()
        ice_cream_type = self.selected_type.get()
        message = f"Вы заказали {ice_cream_type.lower()}  со вкусом '{flavor}'. Спасибо за заказ!"
        order_confirmation = tk.Label(self.master, text=message)
        order_confirmation.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = IceCreamStand(root)
    root.mainloop()

