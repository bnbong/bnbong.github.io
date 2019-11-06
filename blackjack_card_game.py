# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:42:30 2019

@author: bnbon
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:28:24 2019

@author: bnbon
"""

print("Welcome to SMaSH Casino!")

def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + '\n'              
        file.write(line)
    file.close()
    
    
def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members



def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(),key=lambda x: x[1][3], reverse=True)
    # 칩의 개수 역순으로 정렬
    print("All-time Top 5 based on the number of chips earned")
    count = 0
    for i in sorted_members:
        if i[1][3] > 0:
            count += 1
            print("%s."%count,i[0],":",i[1][3])

def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members:#<members의 키 중에서 username이 있다>:
        password, tries, wins, chips = members[username]
        if trypasswd == password:#<trypasswd가 username의 비밀번호와 일치한다>:
            print("You played " + str(tries) + " games and won " + str(int(wins)) + " of them.")# username의 게임시도 횟수와 이긴 횟수를 members에서 가져와 보여준다.
            # 예시: You played 101 games and won 54 of them.
            percentage = str(wins/tries*100)
            if tries != 0:
                print("Your all-time winning percentage is " + percentage[:4]  + " %")# 승률 계산하여 %로 보여줌 (분모가 0인 오류 방지해야 함)
            # 예시: Your all-time winning percentage is 53.5 %
            # 칩 보유개수를 보여줌
            
            if chips >= 0:
                print("You have " + str(chips) + " chips.")
            # 예시 : 개수가 양수이면 You have 5 chips.
            else:
                print("You owe " + str(abs(chips)) + " chips.")
            # 예시 : 개수가 음수이면 You owe 5 chips.
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd,0,0,0)
        # username을 members 사전에 추가한다.
        return username, 0, 0, 0, members
    
def fresh_deck():
    import random
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    # 중첩 for 문으로 52장의 카드를 만들어 리스트 deck을 만든다.
    for i in suits:
        for j in ranks:
            card = {"suit" : i,"rank" : j}
            deck.append(card)
    random.shuffle(deck)
    # deck을 무작위로 섞는다.
    return deck

def hit(deck):
    if len(deck) == 0: # deck이 비어있으면:
        deck = fresh_deck()
        # 카드 1벌을 새로 만듬
    return (deck[0], deck[1:])# (맨 앞의 카드 한장 , 남은 deck)

def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        if card['rank'] == 'K' or card['rank'] == 'J' or card['rank'] == 'Q':
            score += 10
        elif card['rank'] == 'A':
            number_of_ace += 1
            score += 11
        else:
            score += card['rank']
    while score > 21:
        if number_of_ace > 0:
            score -= 10
        else:
            break
        # card의 값을 평가하여 score에 더함 (A는 11로 계산)
      # score가 21이 넘고 A가 있으면 score를 재조정함
    # A가 2장 이상 있을 수 있음에 유의
    return score

def show_cards(cards,message):
    print(message)
    for card in cards:
        print(" ", card["suit"], card["rank"])
        # card를 보기 좋게 한줄에 프린트

def more(message):
    answer = input(message)
    while not answer == 'y' and answer != 'n':#(반복 조건):
        answer = input(message)
    return answer == 'y'# 조건식



def blackjack():
    print("-----")
    twins = 0
    ttry = 0
    username, tries, wins, chips, members = login(load_members())
    while True:
        deck = fresh_deck()
        dealer = []
        player = []
        card, deck = hit(deck) #손님 첫번째카드
        player.append(card)
        card, deck = hit(deck) #딜러 첫번째카드
        dealer.append(card)
        card, deck= hit(deck) #손님 두번째카드
        player.append(card)
        card, deck = hit(deck) #딜러 두번째카드
        dealer.append(card)
        print("My cards are:")
        print(" ", "****", "**")
        print(" ", dealer[1]["suit"], dealer[1]["rank"])
        show_cards(player, "Your cards are:")
        score_player = count_score(player)
        score_dealer = count_score(dealer)
        
        while score_player < 21 and more("Hit? (y/n) ") == True:
            card, deck = hit(deck)
            player.append(card)
            print(" ", card["suit"], card["rank"])
            score_player = count_score(player)
            
        while score_dealer <= 16:
            card, deck = hit(deck)
            dealer.append(card)
            score_dealer = count_score(dealer)
                
        if score_player > 21: #손님버스트
            show_cards(dealer, "My cards are:")
            chips = chips - 1
            tries = tries + 1
            ttry += 1
            passwd = members[username][0]
            (passwd, tries, wins, chips) = members[username]
            store_members(members)
            print("You bust! I won.")
            print("Chips =", chips)
            responseplay = more("Play more? (y/n) ")
            if responseplay == False:
                    break
                            
        elif score_dealer > 21: #딜러버스트
            show_cards(dealer, "My cards are:")
            chips = chips + 1
            tries = tries + 1
            wins = wins + 1
            ttry += 1
            twins += 1
            passwd = members[username][0]
            members[username] = (passwd,int(tries),float(wins),int(chips))
            store_members(members)
            print("I bust! You won.")
            print("Chips =", chips)
            responseplay = more("Play more? (y/n) ")
            if responseplay == False:
                break
                    
        elif score_player == 21: #손님 블랙잭
            show_cards(dealer, "My cards are:")
            chips = chips + 2
            tries = tries + 1
            wins = wins + 1
            ttry += 1
            twins += 1
            passwd = members[username][0]
            members[username] = (passwd,int(tries),float(wins),int(chips))
            store_members(members)
            print("Blackjack! You won.")
            print("Chips =", chips)
            responseplay = more("Play more? (y/n) ")
            if responseplay == False:
                break
            
            
        elif score_player == score_dealer and score_player < 21 and score_dealer <= 21:
            show_cards(dealer, "My cards are:")
            tries = tries + 1
            ttry += 1
            passwd = members[username][0]
            members[username] = (passwd,int(tries),float(wins),int(chips))
            store_members(members)
            print("We draw.")
            print("Chips =", chips)
            responseplay = more("Play more? (y/n) ")
            if responseplay == False:
                break
            
        
        elif score_player < score_dealer and score_player <21 and score_dealer <= 21:
            show_cards(dealer, "My cards are:")
            chips = chips - 1
            tries = tries + 1
            ttry += 1
            passwd = members[username][0]
            members[username] = (passwd,int(tries),float(wins),int(chips))
            store_members(members)
            print("I won.")
            print("Chips =", chips)
            responseplay = more("Play more? (y/n) ")
            if responseplay == False:
                break
            
        elif score_player > score_dealer and score_player < 21 and score_dealer <= 21:
            show_cards(dealer, "My cards are:")
            chips = chips + 1
            tries = tries + 1
            wins = wins + 1
            twins += 1
            ttry += 1
            passwd = members[username][0]
            members[username] = (passwd,int(tries),float(wins),int(chips))
            store_members(members)
            print("You won.")
            print("Chips =", chips)
            responseplay = more("Play more? (y/n) ")
            if responseplay == False:
                break
    percentage = (twins/ttry*100)
    print("You played " + str(tries) + " games and won " + str(wins) + " of them.\n" "Your winning percentage today is " + "{0:.1f}".format(percentage) + "%.")
    print(show_top5(members))
    print("Bye!")
blackjack()
            
