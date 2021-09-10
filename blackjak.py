# -*- coding: utf-8 -*-
import random


FACES = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']


class Card:
    def __init__(self, face, suit):
        assert face in FACES and suit in SUITS 
        self.face = face
        self.suit = suit

    def __str__(self):
        article = 'a '
        if self.face in [8, 'Ace']:
            article = 'an '
        return (article + str(self.face) + ' of ' + self.suit)

    def value(self):
        if type(self.face) == int:
            return self.face
        if self.face == 'Ace':
                  return 11
        return 10


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                self.cards.append(Card(face, suit))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
    
    
class Person:
    def __init__(self):
        self.hand = []
        self.num_card = 2
        self.value = 0
        self.card = None
    
    def start(self):
        deck = Deck()
        self.card = deck.draw()
        self.hand.append(self.card)

    def print_total(self):
        self.value = 0
        for self.card in self.hand:
            self.value += self.card.value()
            
    def sum_card(self):
        return self.value
        
        
class User(Person):
    def __init__(self):
        super().__init__()                # super()로 기반 클래스의 __init__ 메서드 호출
    
    def start(self):
        print('유저에게 카드 나눠주는중..')
        super().start()
        print(f'뽑은카드 : {self.card}')

    def print_total(self):
        super().print_total()
        print('유저의 현재 카드 리스트', end=' -> ')
        for i in self.hand:
            print(f'[{i}]', end=',')
        print('\n유저의 총 카드 합계 :', self.value)
        
        
class Dealar(Person):
    def __init__(self):
        super().__init__()        
    
    def start(self):
        print('딜러에게 카드 나눠주는중..')
        super().start()  
    
    def print_total(self):
        super().print_total()
        

def ask_yesno(prompt):
    while True:
        user_input = input(prompt)

        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('please input y or n')

            
def blackjack():
    print('BlackJack 게임시작')
    print()
    
    dealer = Dealar()
    player = User()
    
    for _ in range(2):
        dealer.start()
        player.start()
    
    player.print_total()
    dealer.print_total()
    
    while player.sum_card() < 21:
        if not ask_yesno("Would you like another card? (y/n) "):
            break
            
        player.start()
        player.print_total()
        if player.sum_card() > 21:
            break
        dealer.start()
        dealer.print_total()
        
        if dealer.sum_card() > 21:
            break
    
    if player.sum_card() > 21:
        print(f'YOU LOST!!!!!!. Dealer WIN!!!!! \nYour CARD TOTAL -> {player.sum_card()}, Dealer CARD TOTAL -> {dealer.sum_card()}')
        return -1
    
    if dealer.sum_card() > 21:
        print(f'YOU WIN!!!!!!. Dealer LOST!!!!! \nYour CARD TOTAL -> {player.sum_card()}, Dealer CARD TOTAL -> {dealer.sum_card()}')
        return -1
    
    if dealer.sum_card() > player.sum_card() :
        print(f'YOU LOSE!!!! \nYour CARD TOTAL -> {player.sum_card()}, Dealer CARD TOTAL -> {dealer.sum_card()}')
    
    elif dealer.sum_card() < player.sum_card():
        print(f'YOU WIN!!!!!!. \nYour CARD TOTAL -> {player.sum_card()}, Dealer CARD TOTAL -> {dealer.sum_card()}')

    else:
        print(f'무승부입니다!!!!!!!!!!!')
        
        
if __name__ == "__main__":
    blackjack()
