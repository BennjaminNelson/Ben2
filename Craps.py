import random


def play_craps():

    y_n = raw_input("Do you want to play craps??: ")

    bank = input("how much money you got?: ")
    winnings = 0

    while y_n == "yes":

        bet = input("How much is your bet?: ")

        if bet > bank:
            print("Bet to large guy.")
            continue

        else:
            pass_bet = raw_input("pass line or don't pass line: ")

            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            final_roll = roll1 + roll2

            if final_roll == (2, 3, 12):

                if pass_bet == "pass line":

                    bank -= bet
                    winnings -= bet

                    y_n = raw_input("You lost your Pass line bet!. You have " + str(bank) + "." + """
                    You rolled a 
                    """ + str(final_roll) + """
                     Do you want to play again.: 
                    """)

                else:

                    bank += bet
                    winnings += bet

                    y_n = raw_input("you won your Don't Pass line bet! You have " + str(bank) + "." + """
                    You rolled a 
                    """ + str(final_roll) + """
                     Do you wanna play again?: 
                     """)

            elif final_roll == (7, 11):

                if pass_bet == "pass line":

                    bank += bet
                    winnings += bet

                    y_n = raw_input("You won your Passline bet! You have " + str(bank) + ". with a" + str(final_roll) + """
                    Want to play again?: 
                     """)

                else:

                    bank -= bet
                    winnings -= bet

                    y_n = raw_input("You lost your Dont Pass line bet. You have " + str(bank) + ". You rolled a " + final_roll + """
                    Do you wanna play again?: 
                     """)

            else:

                type_bet = input("OOF nothing. You rolled a " + str(final_roll) + ". Want another bet?: ")
                # needs alot of work right here on types of betting. took out soft bets in meantime

                y_n2 = raw_input("do you want to roll again? (type roll): ")

                while y_n2 == 'roll':

                    soft_bet_wager = input("Your bank has " + str(bank) + ". How much do you want to bet: ")

                    if soft_bet_wager > bank:
                        print("Bet to large guy.")
                        continue

                    else:

                        roll3 = random.randint(1, 6)
                        roll4 = random.randint(1, 6)
                        final_roll2 = roll3 + roll4

                        if final_roll2 == 7:

                            bank -= bet
                            bank -= soft_bet_wager
                            winnings -= bet
                            winnings -= soft_bet_wager

                            y_n2 = raw_input("You lost. (big 7) you have " + str(bank) + "." + """
                             Do you want to play again?: 
                             """)


                        elif final_roll2 == soft_bet and pass_bet:

                            bank += bet
                            bank += soft_bet_wager
                            winnings += bet
                            winnings += soft_bet_wager

                            y_n2 = raw_input("You won your Pass bet and your soft bet!! You have " + str(bank) + """
                            You rolled a
                            """ + final_roll2 + """
                            Do you want to play again!?:  
                            """)

                        elif final_roll2 == soft_bet:

                            bank += soft_bet_wager
                            winnings += soft_bet_wager

                            y_n2 = raw_input("you won your soft bet!! You have " + str(bank) + "." + """"
                            You rolled a 
                            """ + final_roll2 + """
                            Do you want to roll again?: 
                            """)

                        else:

                            y_n2 = raw_input("OOF you rolled a " + str(final_roll2) + "." + """
                            Do you want to roll again?: 
                            """)

play_craps()




























