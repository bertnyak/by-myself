import random

class Mag:
    def __init__(self):
        self.hp = 20
        self.normal_damage = 4
        self.fast_damage = 6
        self.fast_minus_hp = 2

    def attack(self, fast = False):
        if fast:
            if self.hp >= self.fast_minus_hp:
                self.hp -= self.fast_minus_hp
                return self.fast_damage
            return 0
        return self.normal_damage

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    def is_alive(self):
        return self.hp > 0


class Brother:
    def __init__(self):
        self.hp = 20
        self.damage = 5
        self.shield_hp = 2
        self.shield_damage = 3

    def attack(self, shield = False):
        if shield:
            if self.hp >= self.shield_hp:
                self.hp -= self.shield_hp
                return self.shield_damage
            return 0
        return self.damage

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    def is_alive(self):
        return self.hp > 0

brother = Brother()
mag = Mag()

print(f"Обычная атака мага {mag.attack()}")
print(f"Ускоренная атака мага {mag.attack(fast=True)}")
print(f"Осталось хп мага {mag.hp}")

print(f"Обычная атака Братьев {brother.attack()}")
print(f"Защитная атака {brother.attack(shield=True)}")
print(f"Осталось хп у братьев {brother.hp}")