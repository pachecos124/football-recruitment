import player_status
import random
import time
#This is the file for the sports career
print("This is the sports career")

class FootballCareer:
    def __init__(self, player):
        self.player = player
        self.division = None
        self.score = 0
        self.games_played = 0
        self.career_path = []

    def choose_position(self):
        print("\nPICK YOUR POSITION")
        print("1. Quarterback")
        print("2. Wide Receiver")
        print("3. Linebacker")
        print("4. Defensive Back")
        
        while True:
            choice = input("Enter your position choice (1-4): ")
            if choice in ['1', '2', '3', '4']:
                positions = {
                    '1': 'Quarterback',
                    '2': 'Wide Receiver',
                    '3': 'Linebacker',
                    '4': 'Defensive Back'
                }
                self.player.set_postiton(positions[choice])
                print(f"You have chosen to be a {self.player.get_postiton()}")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def choose_division(self):
        print("\nChoose your starting division:")
        print("1. Division 1")
        print("2. Division 2")
        print("3. Division 3")
        
        while True:
            choice = input("Enter your division choice (1-3): ")
            if choice in ['1', '2', '3']:
                divisions = {
                    '1': 'D1',
                    '2': 'D2',
                    '3': 'D3'
                }
                self.division = divisions[choice]
                print(f"You will start in {self.division}")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    def play_game(self, scenario, options):
        print(f"\n{scenario}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        while True:
            choice = input("Enter your choice (1-3): ")
            if choice in ['1', '2', '3']:
                return int(choice)
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    def calculate_score(self, choice, correct_answers):
        if choice in correct_answers:
            self.score += 25
            print("Great decision! +25 points")
        else:
            print("Not the best choice, but you'll learn from it.")

    def check_transfer_opportunity(self):
        if self.division in ['D2', 'D3'] and self.score >= 80:
            print("\nImpressive performance! You have the opportunity to transfer to a D1 school!")
            print("1. University of Texas")
            print("2. Alabama Crimson Tide")
            print("3. Stay in current division")
            
            choice = input("Would you like to transfer? (1-3): ")
            if choice in ['1', '2']:
                self.division = 'D1'
                print("Congratulations! You're now playing in Division 1!")
                return True
        return False

    def check_nfl_opportunity(self):
        if self.division == 'D1' and self.score >= 85:
            print("\nOutstanding performance! You've caught the attention of NFL scouts!")
            print("1. Dallas Cowboys")
            print("2. New England Patriots")
            print("3. Kansas City Chiefs")
            
            choice = input("Would you like to enter the NFL draft? (1-3): ")
            if choice in ['1', '2', '3']:
                print("Congratulations! You've made it to the NFL!")
                return True
        return False

    def start_career(self):
        print("Welcome to your Football Career!")
        self.choose_position()
        self.choose_division()
        
        # High School Games
        print("\n=== HIGH SCHOOL CAREER ===")
        scenarios = [
            {
                "description": "First game of the season...",
                "options": ["Option 1", "Option 2", "Option 3"],
                "correct": [1, 2]
            },
            # Add more scenarios here
        ]
        
        for scenario in scenarios:
            choice = self.play_game(scenario["description"], scenario["options"])
            self.calculate_score(choice, scenario["correct"])
            time.sleep(2)
        
        if self.check_transfer_opportunity():
            # College Games
            print("\n=== COLLEGE CAREER ===")
            # Add college scenarios here
            
            if self.check_nfl_opportunity():
                # NFL Game
                print("\n=== NFL CAREER ===")
                # Add NFL scenario here
        
        print("\n=== CAREER SUMMARY ===")
        print(f"Final Score: {self.score}")
        print(f"Games Played: {self.games_played}")
        print(f"Final Division: {self.division}")
        print("Thanks for playing!")

# Start the game
name = input("Enter your name: ")
player = player_status.player(name)
career = FootballCareer(player)
career.start_career()
