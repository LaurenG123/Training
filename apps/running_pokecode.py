#training proof stuff
import requests
import random
import csv

#kivy stuff
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.uix.image import Image

class RootWidget(BoxLayout):
    #use kwargs since not sure with libraries about input numbers
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = dp(10)
        self.padding = dp(10)

        self.image = Image(source='/Users/laurengorst/Desktop/Pokemon-Symbol.png',size =(500,500))

        #  input Pokémon names
        self.pokemon1_name_input = TextInput(hint_text='Enter Pokémon 1 Name')
        self.pokemon2_name_input = TextInput(hint_text='Enter Pokémon 2 Name')

        # Start battle button
        self.start_battle_button = Button(text='Start Pokémon Battle', on_press=self.start_pokemon_battle)

        # scroll log for battle result
        self.battle_result_scrollview = ScrollView(size_hint=(1, None), size=(500, 500))
        self.battle_result_label = Label(text='', size_hint_y=None, valign='top')
        self.battle_result_label.bind(texture_size=self.battle_result_label.setter('size'))
        self.battle_result_label.markup = True  # Enable markup
        self.battle_result_scrollview.add_widget(self.battle_result_label)

        self.battle_log = []


        # app layout
        self.add_widget(self.image)
        self.add_widget(self.pokemon1_name_input)
        self.add_widget(self.pokemon2_name_input)
        self.add_widget(self.start_battle_button)
        self.add_widget(self.battle_result_scrollview)


    def save_battle_log_to_csv(self, battle_log_text):

        csv_file_path = "pokemon_battle_log.csv"

        try:
            with open(csv_file_path, "a") as csv_file:
                csv_file.write(battle_log_text + "\n")
        except Exception as e:
            print(f"Error saving battle log to CSV: {str(e)}")

    def fetch_pokemon_data(self, pokemon_name):

        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
            response = requests.get(url)

            if response.status_code == 200:
                pokemon_data = response.json()

                # get abilities from the Pokemon data
                abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
                abilities_str = ", ".join(abilities)

                # get health (HP) from base_experience data
                health = pokemon_data['base_experience']

                # show abilities and HP in the battle log AT THE BEGINNING
                self.battle_result_label.text += f"Abilities of {pokemon_name}: {abilities_str}\n"
                self.battle_result_label.text += f"HP of {pokemon_name}: {health}\n"

                return pokemon_data
            else:
                self.battle_result_label.text += f"Error: Unable to fetch data for {pokemon_name}. Status code: {response.status_code}\n"
                return None

        except Exception as e:
            self.battle_result_label.text += f"An error occurred: {str(e)}\n"
            return None

#for the popup so we don't have to scroll forever if its a long battle
    def show_winner_popup(self, winner_name):

        content = BoxLayout(orientation='vertical')
        winner_label = Label(text=f"{winner_name} wins!", font_size=50)
        close_button = Button(text="Close", size_hint=(None, None), size=(150, 50))
        content.add_widget(winner_label)
        content.add_widget(close_button)

        popup = Popup(title="Pokemon champion.....", content=content, size_hint=(None, None), size=(500, 500))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

# this is just the warm up ring, pokemon and stats introduced after input actual battle starts later...
    def start_pokemon_battle(self, instance):
        pokemon1_name = self.pokemon1_name_input.text
        pokemon2_name = self.pokemon2_name_input.text

        # get the Pokémon data
        pokemon1_data = self.fetch_pokemon_data(pokemon1_name)
        pokemon2_data = self.fetch_pokemon_data(pokemon2_name)
        self.save_battle_log_to_csv("NEW BATTLE")
        if pokemon1_data and pokemon2_data:
            # set initial HP values (base experience from api)
            pokemon1_data['hp'] = pokemon1_data['base_experience']
            pokemon2_data['hp'] = pokemon2_data['base_experience']

            # clear previous battle result in app only
            self.battle_result_label.text = ""

            # start the battle...
            self.pokemon_battle(pokemon1_data, pokemon2_data)

#result that is printed as the end of the game scroll thing and in popup
    def display_result_message(self, winner_name):
        message = f"[color=ff0000][size=32]{winner_name} wins![/size][/color]\n"
        self.battle_result_label.text += message
        self.show_winner_popup(winner_name)

# actual battle proceedings (the actual game)
    def pokemon_battle(self, pokemon1, pokemon2):
        self.battle_result_label.text += f"A wild {pokemon1['name']} appeared!\n"
        self.battle_result_label.text += f"A wild {pokemon2['name']} appeared!\n"
        self.fetch_and_display_abilities(pokemon1, pokemon2)
        self.battle_result_label.text += \
            f"{pokemon1['name']} starts with {pokemon1['hp']} health based on his experience\n"

        self.battle_result_label.text += \
            f"{pokemon2['name']} starts with {pokemon2['hp']} health based on his experience \n"
        self.battle_result_label.text += f"START BATTLE!\n"


        while pokemon1['hp'] > 0 and pokemon2['hp'] > 0:
            # calculate damage
            damage = random.randint(1, 10)
            battle_log_entry = f"{pokemon1['name']} attacks {pokemon2['name']} for {damage} damage!"
            self.battle_result_label.text += battle_log_entry + "\n"

            # save the battle log entry to the CSV file
            self.save_battle_log_to_csv(battle_log_entry)
            # minus damage from opponent
            pokemon2['hp'] -= damage

            # take turns
            pokemon1, pokemon2 = pokemon2, pokemon1

            #  current status
            self.battle_result_label.text += f"{pokemon1['name']} has {pokemon1['hp']} HP left.\n"
            self.battle_result_label.text += f"{pokemon2['name']} has {pokemon2['hp']} HP left.\n"

        if pokemon1['hp'] <= 0:
            self.display_result_message(pokemon2['name'])
        else:
            self.display_result_message(pokemon1['name'])


#meh could be simplified but basically retrieving corresponding pokemon infor from api
    def fetch_and_display_abilities(self, pokemon1, pokemon2):
        abilities1 = [ability['ability']['name'] for ability in pokemon1['abilities']]
        abilities2 = [ability['ability']['name'] for ability in pokemon2['abilities']]
        abilities1_str = ", ".join(abilities1)
        abilities2_str = ", ".join(abilities2)

        self.battle_result_label.text += f"[color=ff0000][size=50][b]{pokemon1['name']} Abilities:[/b] {abilities1_str}[/size][/color]\n"
        self.battle_result_label.text += f"[color=ff0000][size=50][b]{pokemon2['name']} Abilities:[/b] {abilities2_str}[/size][/color]\n"

class PokemonBattleApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    PokemonBattleApp().run()
