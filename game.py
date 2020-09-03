import sys
sys.path.append("/home/patrick/Desktop/Draft/BlackJack/")
from Deck_File.deck import Deck
from Play_File.player import Player

class Game:
    def __init__(self):
        pass

    def game_start(self):
        playing = True
        
        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_turn = Player()
            self.dealer_turn= Player(dealer=True)

            for i in range(2):
                self.player_turn.add_card(self.deck.deal())
                self.dealer_turn.add_card(self.deck.deal())
            print("===============")
            print("             ||")
            print("Player's turn:")
            print("    =====    ")
            self.player_turn.show()
            print("             ||")
            print("==============")
            print( )
            print("===============")
            print("             ||")
            print("Dealer's turn:")
            print("    =====    ")
            self.dealer_turn.show()
            print("             ||")
            print("==============")
            
            game_over = False

            while not game_over:
                player_wins, dealer_wins = self.the_results()
                if player_wins or dealer_wins:
                    game_over = True
                    self.show_blackjack_results(player_wins , dealer_wins)
                    continue

                choice = input("\n You wanna?: [Stay/ Exit] ").lower()
                while choice not in ["s", "e", "Stay", "exit"]:
                    choice = input("\n Please enter 'Stay' or 'exit' (or S/E) ").lower()
                if choice in ['Stay', 's']:
                    self.player_turn.add_card(self.deck.deal())
                    self.player_turn.show()
                    if self.player_is_over():
                        print("\n Sorry, it is not your day!")
                        game_over = True
                else:
                    player_turn_value = self.player_turn.result()
                    dealer_turn_value = self.dealer_turn.result()

                    print("\n You've got")
                    print("\n Player result:", player_turn_value)
                    print("\n Dealer's result:", dealer_turn_value)

                    if player_turn_value > dealer_turn_value:
                        print("\n You Win!")
                    elif player_turn_value == dealer_turn_value:
                        print("\n Tie!")
                    else:
                        print("\n Dealer Wins!")
                    game_over = True
            
            again = input("\n Dou you want to play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("\n Please enter Y or N ")
            if again.lower() == "n":
                print("\n Thanks for playing, Hope you enjoyed the BLACKJACK!")
                playing = False
            else:
                game_over = False

    def player_is_over(self):
        return self.player_turn.result() > 21

    def the_results(self):
        player = False
        dealer = False
        if self.player_turn.result() == 21:
            player = True
        if self.dealer_turn.result() == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_wins , dealer_wins):
        if player_wins and dealer_wins:
            print("Both players have 21! It is a Draw no one wins!")

        elif player_wins :
            print("You have 21! You win!")

        elif dealer_wins:
            print("Dealer has 21! Dealer wins!")
    
    def game_quit(self):
        exit()

if __name__ == "__main__":
    g = Game() 

    menu = 0
    print ("Choose an option")
    print("-------------------------------")
    Menu = int(input("""1.JOUER 2.RIGOLER 3.QUITTER :"""))

    if Menu == 1:
        print ('Vous allez commencer !!')
        print()
        print()
        print()
        print("----------------------------------------------------------------------------")
        print()
        print("			     $	B L A C K J A C K	$			                           ")
        print()
        print("----------------------------------------------------------------------------")
        g.game_start()
        print()
        print("----------------------------------------------------------------------------")
        print()
        print("       ~~~~~ THE GAME IS DOWN, IT IS FRIDAY, LET'S GO DANCING  ~~~~~        ")
        print()
        print("----------------------------------------------------------------------------")

    
    if Menu == 2:
        print("-------------------------------")
        print('Impossible la POO ne nous fait pas rire !!')

    else:
        print("-------------------------------")
        print("CIAO...Not Interested in BlackJack, I'd rather go To Tinder")


 
    

