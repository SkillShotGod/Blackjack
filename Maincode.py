import random
import os
from time import sleep
import sys

class blackjack:
    def __init__(self):
        self.acecount=[0,0]
        self.handsum=[0,0]
        self.hand=[[],[]]
        self.turn=0
        self.pot=0
        self.bank=0
        self.bet=-1
        self.value={
            'A': 11,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'k': 10
        }
        self.occurence={
            'A': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            '10': 0,
            'J': 0,
            'Q': 0,
            'k': 0
        }
        
    def occurencecheck(self):
        if self.occurence.get(self.card)==4:
            self.revealcard()
        else:
            self.occurence[self.card]+=1
        
    def revealcard(self):
        self.card=random.choice(list(self.value.keys()))
        self.occurencecheck()
        if self.card=='A':
            self.acecount[self.turn]+=1
        self.card_value=self.value[self.card]
        self.handsum[self.turn]+=self.card_value
        self.hand[self.turn].append(self.card)
        
    
    def tostate_qd(self):
        print("Dealer's hand= ",self.hand[0])
        print("and value = ",self.handsum[0])
        print("Player's hand= ",self.hand[1])
        print("and value = ",self.handsum[1])
        if self.turn==1:
            if self.handsum[self.turn]==21:
                print("Player wins the hand ")
                self.bank+=self.pot
            elif self.handsum[self.turn]>21:
                print("Dealer wins the hand ")
            
        elif self.turn==0:
            if (self.handsum[self.turn]==21) or ((self.handsum[0]>self.handsum[1]) and (self.handsum[self.turn]<21)):
                print("Dealer wins the hand ")
            elif self.handsum[self.turn]>21:
                print("Player wins the hand ")
                self.bank+=self.pot
            else:
                print("Its a tie ")
                self.bank+=self.bet
            
            
        self.pot=0
        self.handsum=[0,0]
        self.acecount=[0,0]
        self.hand=[[],[]]
        sleep(2)
        os.system('cls')
        self.starthand()
    
    def initialcheck(self):
        if (self.handsum[1]==21):
            self.pot=(self.bet*2)+self.bet//2
            self.tostate_qd()
            
    def acecheck(self):
        if 'A' in self.hand[self.turn] and (self.acecount[self.turn]>0):
            self.handsum[self.turn]-=10
            self.acecount[self.turn]-=1
            if self.turn==1:
                self.choice()
            elif self.turn==0:
                self.dealerplay()
                
    def hit(self):
        self.revealcard()
        if int(self.handsum[self.turn])<21 and self.turn==1:
            self.choice()
        elif int(self.handsum[self.turn])>=21:
            self.acecheck()
            self.tostate_qd()

    
    def dealerplay(self):
        self.turn=0
        if self.handsum[0]==21:
            self.tostate_qd()
        while (self.handsum[0]<self.handsum[1]):
            self.hit()
            print("Dealer's hand= ", self.hand[0])
            if (self.handsum[0]>=self.handsum[1]):
                self.tostate_qd()
        self.tostate_qd()
                
    def stand(self):
        print("Dealer's hand", self.hand[0])
        self.dealerplay()
            
    def choice(self):
        print("Current hand is ", self.hand[self.turn])
        print("Total value of hand is ", self.handsum[self.turn])
        hitStand=int(input("Input 1 for Hit and 0 for Stand \n"))
        if hitStand==1:
            self.hit()
        elif hitStand==0:
            self.stand()
        else:
            print("Enter correct choice pepega ")
            self.choice()

    

        
            
    def betcheck(self):
        self.validbet=1
        print("Remember, place bet as 0 to to quit the game \n")
        while self.validbet:
            print("Bank amount= ",self.bank)
            self.bet=int(input("Place a valid bet "))
            if self.bet==0:
                print("You leave the table with $",self.bank)
                sys.exit("Thank you for playing") 
            elif self.bet<=self.bank and self.bet>0:
                self.bank-=self.bet
                self.validbet=0
            else:
                if self.bet>bank:
                    print("Can not place bet more than available bank \n")
                print("Bet was not a valid bet \n")
                sleep(2)
                os.system('cls')
        self.pot=self.bet*2
        
        
    def startgame(self,money):
        self.bank=money
        self.starthand()
        
    def reset_occurence(self):
        self.occurence={
            'A': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            '10': 0,
            'J': 0,
            'Q': 0,
            'k': 0
        }
        
    def starthand(self):
        self.reset_occurence()
        self.betcheck()
        self.turn=0
        self.revealcard()
        print("Dealer's hand= ", self.hand[0])
        self.turn=1
        self.revealcard()
        self.revealcard()
        print("Player's hand= ", self.hand[1])
        self.initialcheck()
        self.turn=0
        self.revealcard()

        self.turn=1
        self.choice()


