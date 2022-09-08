'''
Cricket game using random library

'''
import random
import fancyText

op_score = 0
pl_score = 0
play = True
no_deliveries = 6

def check_valid(n):
   
    if (n in range(1, 7) and n%1 == 0):
        return True
    else:
        print("Invalid input!")
        return False


def toss():

    select = input('Odd or even?(o/e) ')
    Player_toss = int(input('Enter the number : '))
    if check_valid(Player_toss):
        Opp_toss = random.randint(1, 6)
        fancyText.fancyPrint(Player_toss, Opp_toss)
        result = (Player_toss + Opp_toss) % 2

        if(result == 0 and select == 'e') or (result != 0 and select == 'o'):

            choice = input('You Win!! Do you want to bat or field?(b/f)')

        else:

            no = random.randint(1, 2)

            if no == 1:

                print('You loose!! Your opponent chose to bat!')
                choice = 'f'
            else:

                print('You loose!! Your opponent chose to field!')
                choice = 'b'
        return choice

############################################################# MAIN #############################################################

print(fancyText.banner)
while play:
    c = toss()
    if c == 'b':
        i = 0
        while(i<no_deliveries):

            player_inp = int(input(str(i+1) + '/6 Enter Number : '))
            if check_valid(player_inp):
                computer_inp = random.randint(1, 6)
                fancyText.fancyPrint(player_inp, computer_inp)
                if player_inp == computer_inp:

                    print('OUT!!')
                    break

                else:
                    pl_score += player_inp
                
                i += 1


        print('Your scored ', pl_score, 'runs!! ',
            'Your opponents target is :', (pl_score+1))  # display summary
        i = 0
        while(i<no_deliveries):

            player_inp = int(input(str(i+1) + '/6 Enter Number : '))
            if check_valid(player_inp):
                computer_inp = random.randint(1, 6)
                fancyText.fancyPrint(player_inp, computer_inp)
                if player_inp == computer_inp:

                    print('OUT!!')
                    break

                else:
                    op_score += computer_inp


                if op_score > pl_score:
                    break

            i += 1

    elif c == 'f':
        i = 0
        while(i<no_deliveries):

            player_inp = int(input(str(i+1) + '/6 Enter Number : '))
            if check_valid(player_inp):
                computer_inp = random.randint(1, 6)
                fancyText.fancyPrint(player_inp, computer_inp)
                if player_inp == computer_inp:

                    print('OUT!!')
                    break

                else:
                    op_score += computer_inp

                i += 1

        print('Your opponent scored ', op_score,
            'runs!! ', 'Your target is :', (op_score+1))
        i = 0
        while(i<no_deliveries):

            player_inp = int(input(str(i+1) + '/6 Enter Number : '))
            if check_valid(player_inp):
                computer_inp = random.randint(1, 6)
                fancyText.fancyPrint(player_inp, computer_inp)
                fancyText.fancyPrint(player_inp, computer_inp)

                if player_inp == computer_inp:

                    print('OUT!!')
                    break

                else:

                    pl_score = pl_score + player_inp

                if pl_score > op_score:
                    break
                i += 1

    if op_score == pl_score:
        print('Its a tie!!')

    elif op_score > pl_score:
        print('You Loose!!')

    else:
        print('You win!!')
    if input("Do you want to play again?(y/n): ") == 'n':
        play = False

