from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(200,400)
        self.power = randint(30, 50)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["other"]['official-artwork']["front_default"])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
        
        



    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}\nЗдоровье: {self.hp}\nАтака:{self.power}"
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,3)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"




        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}.\n"+\
                f"@{self.pokemon_trainer} нанёс {self.power} урона.\n"+\
                f"Здоровье @{enemy.pokemon_trainer} {enemy.hp}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
class Wizard(Pokemon):
    def info(self):
        return super().info() +"\nУ тебя покемон волшыбник"
    

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power= randint(5,15)
        self.power += super_power
        result= super().attack(enemy)
        self.power-=super_power
        return "была пременина супер сила\n"+result
    
    
pok_1=Fighter("123")
print(pok_1.info())
pok_2=Wizard("12334")
print(pok_2.info())
print(pok_1.attack(pok_2))
print(pok_1.attack(pok_2))
print(pok_1.attack(pok_2))
print(pok_1.attack(pok_2))
print(pok_1.attack(pok_2))
    



