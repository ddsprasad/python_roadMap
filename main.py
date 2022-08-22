# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class GetPlayer:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        return f"This player can run {self.name}"

    def print_hi(self):
        # Use a breakpoint in the code line below to debug your script.
        return f'Hi, {self.name}'  # Press Ctrl+F8 to toggle the breakpoint.

    def desc(self):
        return f'Player Name: {self.name} \n Player Age: {self.age} \n Player Gender: {self.gender}'

    def older_player(self,*args):
        return f'oldest player among them is : {max(args)}'




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    player_1 = GetPlayer('tony', 22, 'male')
    player_2 = GetPlayer('genus', 23, 'male')
    player_3 = GetPlayer('gita', 23, 'female')

    print(player_1.desc())
    print(player_1.older_player(player_1.age,player_2.age,player_3.age))
    # print(player_1.name)
    # print(player_1.run())
    # print(player_1.print_hi())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/