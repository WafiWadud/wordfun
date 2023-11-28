import random

# Create a deck with 51 cards, each letter appears at least once
deck = {chr(i): 1 for i in range(ord('A'), ord('Z')+1)}


def draw_cards(deck, num_cards):
    drawn_cards = {}
    for _ in range(num_cards):
        letter = random.choice(list(deck.keys()))
        drawn_cards[letter] = drawn_cards.get(letter, 0) + 1
        deck[letter] -= 1
    return drawn_cards


def score_word(word):
    return len(word) * 10


def check_word(word, drawn_cards):
    for letter in word:
        if letter not in drawn_cards:
            return False
    return True


def game_loop(deck, target_score):
    score = 0
    round_score = 300
    tries = 5
    while score < target_score:
        print(f"Your current score is {score}.")
        cards = draw_cards(deck, 5)
        for _ in range(tries):
            print("Cards: ", ''.join(cards.fromkeys()))
            word = input("Enter a word you can form with your cards: ")
            if not check_word(word, cards):
                print("Invalid word. Try again.")
                continue
            score += score_word(word)
            print(f"You scored {score_word(word)} points!")
            tries -= 1
            if tries == 0:
                print("Sorry, you ran out of tries. You lost the game.")
                break
        reroll = input("Do you want to reroll? (yes/no) ")
        if reroll.lower() == "yes":
            tries = 5
            continue
        elif score >= round_score:
            print(f"Congratulations! You reached the target score for this round!")
            round_score += 100
            # Replenish the deck
            deck = {chr(i): 1 for i in range(ord('A'), ord('Z')+1)}
        else:
            print("You win")
            break


deck = {chr(i): 1 for i in range(ord('A'), ord('Z')+1)}
target_score = 1000
game_loop(deck, target_score)
