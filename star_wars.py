class Jedi:
    def __init__(self, name, attack, ls_color):
        self.name = name
        self.attack = attack
        self.ls_color = ls_color
        self.weapon = "Lightsaber"
        self.health = 100

    def __str__(self):
        new_line = '\n'
        return f'"Jedi Name: " {self.name} {new_line}"Attack: "{str(self.attack)}{new_line}"Light-Saber Color: "{self.ls_color}{new_line}"Weapon "{self.weapon}{new_line}"Health: "{str(self.health)}'


nysha = Jedi("Nyshell", 15, "Green")
chris = Jedi("Chris", 17, "Red")


print(nysha)