from CardGamesModule import *

class player(object):
	def __init__(self,usedCards,user = False):
		self.hand = [pickRandomCard(usedCards)]
		usedCards.extend(self.hand)
		self.hand.extend([pickRandomCard(usedCards)])
		usedCards.extend(self.hand)
		if not user:
			self.visibleHand = self.hand[1:]
		self.In = True
		self.bust = False

	def stickOrTwist(self,user,usedCards):
		if self.In:
			if user:
				choice = pushChoice("Stick or Twist (or 'view' to see hands)? ",["stick","twist","view"])
				if choice == "view":
					print("\n################################################ Visible Hands")
					printCards(self.hand, 4, header = "\nThese are your cards")
					print("(worth %s)" % self.handVal)
					printCards(player2.visibleHand, 4, header = "\nThese are your opponents cards you have seen")
					print("(worth %s)" % getHandVal(player2.visibleHand))
					print("\n################################################\n\n\n")
					choice = pushChoice("Stick or Twist? ",["stick","twist"])
				if choice == "stick":
					self.In = False
					print("Your final hand total is %s\n" % self.handVal)
				elif choice == "twist":
					card = pickRandomCard(usedCards)
					printCards(card, header = "The dealer dealt you this card. ")
					self.hand.append(card)
					self.handVal += getHandVal([card],True)
					print("Your hand is now worth %s" % str(self.handVal))
					if self.handVal > 21:
						self.bust = True
			else:
				if getHandVal(self.hand) >= 16:
					print("The computer chose to stick")
					self.In = False
				else:
					print("The computer chose to twist")
					card = pickRandomCard(usedCards)
					printCards(card,header = "The dealer dealt the computer this card")
					self.hand.append(card)
					if getHandVal(self.hand) > 21:
						self.bust = True
					self.hand.append(card)
					self.handVal += getHandVal([card],True)
		

def getCardVal(card,user):
	cardVal = 0
	try:
		cardVal = int(getCardNo(card))
	except:
		cardVal = getCardNo(card)
		if cardVal in ["King","Queen","Jack"]:
			cardVal = 10
		if user and cardVal == "Ace":
			cardVal = int(pushChoice("You have an ace. Do you want it to be worth 1 or 11? ",["1","11"]))
	return cardVal

def getHandVal(hand,user = False):
	output = 0
	for card in hand:
		cardVal = getCardVal(card,user)
		if cardVal in ["ace","Ace"]:
			if int(output+11) > 21:
				output += 1
			else:
				output += 11
		else:
			output += cardVal
	return int(output)

pScore,cScore = 0,0
run = True
while run:
	usedCards = []
	player1 = player(usedCards,True)
	player2 = player(usedCards)
	printCards(player1.hand, 3, header = "This is your hand:")
	player1.handVal = getHandVal(player1.hand,True)
	player2.handVal = getHandVal(player2.hand)
	print("Your hand is worth",player1.handVal)
	printCards(player2.visibleHand, header = "These are your opponents face up cards")
	while not player1.bust and not player2.bust:
		if player1.In:
			player1.stickOrTwist(True,usedCards)
			if player1.bust:
				print("You have gone bust. The computer wins. Better luck next time! ")
				cScore += 1
				break
		if player2.In:
			player2.stickOrTwist(False, usedCards)
			if player2.bust:
				print("The computer has gone bust. You win! Well done :) ")
				pScore += 1
				break
		if not player1.In and not player2.In:
			break

	if not player1.bust and not player2.bust:
		if player1.handVal > player2.handVal:
			print("Player wins. You had %s points and the computer had %s points. Well done!" % (player1.handVal,player2.handVal))
			pScore += 1
		elif player1.handVal < player2.handVal:
			print("Computer wins! You had %s points and the computer had %s points. Better luck next time!" % (player1.handVal,player2.handVal))
			cScore += 1
		else:
			print("You drew with %s points each. Well done :)" % player1.handVal)
	repeat = pushChoice("Do you want to play again? ",["yes","no"])
	if repeat == "no":
		run = False
	else:
		for i in range(200):
			print()
		print("Player is on %s, computer is on %s. Good luck :)" % (pScore,cScore),"\n\n\n")

