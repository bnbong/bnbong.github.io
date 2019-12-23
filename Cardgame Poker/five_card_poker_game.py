import random


class not_natural_number(Exception): pass


class not_in_number(Exception): pass


import time


# card_game_five_card_draw_poker 1.03
# 팀이름 : 부드러운
# 조원구성 : 2019043927 김동한, 2019011758 이준혁, 2019003163 허재원

# 본 코드는 파이브 카드 드로우 포커를 적용, 참조하였습니다.
# 딜러(AI)가 결정을 확률적으로 하게 하는 함수를 도입함으로써, 딜러가 블러핑을 하는 효과를 낼 수 있게 했습니다.
# 딜러나 플레이어 둘 중 한명이라도 올인을 했을 경우, 바로 결과를 보여줍니다.

# 2019.6.9 수정: 딜러의 의사표현확률 소폭조정, 딜러와 플레이어의 레이즈 & 콜 & 올인함수 도입, members.txt파일에 자신이 칩을 빚졌는지 그렇지 않았는지\n
# 알 수 있게 member의 구성요소에 debt와 빚진 칩의 개수 debtchips를 추가, 그 외 자잘한 오류 또는 알고리즘 벗어난 부분 수정.

# 2019.6.10수정: members.txt에 새로운 계정에 대한 정보를 입력하는 함수와 게임결과를 갱신해주는 함수 수정.
# 딜러 또는 플레이어가 다이했을 때, 딜러 또는 플레이어의 승패여부를 먼저 프린트 해주고 두명의 카드의 현황을
# 나타내주는 함수 추가, 카드를 바꾸는 함수에서 카드를 5회 바꾸게 되면 카드를 더 바꿀건지 물어보지 않고 바로 break하게 변경.
# login함수에서 자기 계정이 있다고 입력했을 때 members.txt에 자기 계정이 존재하지 않는다면 다시login함수로 리턴하는 부분 수정
# 딜러와 자기의 카드를 보여주는 부분에서 J,Q,K,A를 숫자로 변환한 것을 다시 문자로 되돌리는 부분이 작동하지 않는 것 수정.

# 2019.6.12수정: 플레이어가 콜을 할 때 배팅된 금액을 프린트 하는 값이 잘못 나온 경우 수정.
# 딜러나 플레이어가 다이를 하지 않는 경우 패를 공개할 때 5초 후에 공개하는 함수 추가. 카드를 공개할 때 카드의 문자가 프린트 안되는 경우 수정.


def fresh_deck():
    import random
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    # 중첩 for 문으로 52장의 카드를 만들어 리스트 deck을 만든다.
    for i in suits:
        for j in ranks:
            card = {"suit": i, "rank": j}
            deck.append(card)
    random.shuffle(deck)
    # deck을 무작위로 섞는다.
    return deck


def store_members(members):
    file = open("members.txt", "w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips, debt, debtchips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + ',' + str(debt) + "," + str(debtchips) + '\n'
        file.write(line)
    file.close()


def more(message):
    answer = input(message)
    while not answer == 'y' and answer != 'n':  # (반복 조건):
        answer = input(message)
    return answer == 'y'  # 조건식


def show_cards(cards, message):
    print(message)
    for card in cards:
        print(" ", card["suit"], card["rank"])
        # card를 보기 좋게 한줄에 프린트


def show_cards_listed(cards, message):
    while True:
        try:
            for i in range(0, 5):
                if cards[i][1] == 11:
                    cards[i][1] = "J"
                if cards[i][1] == 12:
                    cards[i][1] = "Q"
                if cards[i][1] == 13:
                    cards[i][1] = "K"
                if cards[i][1] == 14:
                    cards[i][1] = "A"
            break
        except:
            break
    print(message)
    for card in cards:
        print(" ", card[0], card[1])
        # 카드 리스트를 보기 좋게 한줄에 프린트


def countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n = n - 1


def login(members):
    x = more("First Try?: ")  # 처음 오시는건지 물어보고 처음으로 온다면 계정을 새로 만들어줌
    if x == False:  # 계정이 이미 있는 경우
        username = input("Enter your name: ")
        trypasswd = input("Enter your password: ")
        if username in members:
            password, tries, wins, chips, debt, debtchips = members[username]
            while trypasswd != password:
                trypasswd = input("Try again: ")
            if trypasswd == password:  # <trypasswd가 username의 비밀번호와 일치한다>:
                print("You played " + str(tries) + " games and won " + str(
                    int(wins)) + " of them.")  # username의 게임시도 횟수와 이긴 횟수를 members에서 가져와 보여준다.
            # 예시: You played 101 games and won 54 of them.
            while True:
                try:
                    percentage = str(wins / tries * 100)
                    break
                except ZeroDivisionError:
                    print("Your all-time winning percentage is 0 %.")
                    percentage = 0
                    break
            if tries != 0:
                print(
                    "Your all-time winning percentage is " + percentage[:4] + " %")  # 승률 계산하여 %로 보여줌 (분모가 0인 오류 방지해야 함)
            # 예시: Your all-time winning percentage is 53.5 %
            # 칩 보유개수를 보여줌

            if chips >= 0:
                print("You have " + str(chips) + " chips.")
            # 예시 : 개수가 양수이면 You have 5 chips.
            else:
                print("You owe " + str(abs(chips)) + " chips.")
            # 예시 : 개수가 음수이면 You owe 5 chips.
            return username, tries, wins, chips, debt, debtchips, members
        else:
            return login(members)
    elif x == True:  # 계정이 없는경우 (새로온경우)
        username = input("Enter your new name: ")
        password = input("Enter your new password: ")
        chips = 30
        tries = 0
        wins = 0
        debt = False
        debtchips = 0
        members[username] = (password, tries, wins, chips, debt, debtchips)
        # username을 members 사전에 추가한다.
        return username, tries, wins, chips, debt, debtchips, members


def load_members():
    file = open("members.txt", "r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips, debt, debtchips = line.strip('\n').split(',')
        members[name] = (passwd, int(tries), float(wins), int(chips), debt, int(debtchips))
    file.close()
    return members


def hit(deck):
    if len(deck) == 0:  # deck이 비어있으면:
        deck = fresh_deck()
        # 카드 1벌을 새로 만듬
    return (deck[0], deck[1:])  # (맨 앞의 카드 한장 , 남은 deck)


def who_is_first():  # 순서를 정해주는 함수
    percent = ["y", "y", "y", "y", "y", "n", "n", "n", "n", "n"]
    random.shuffle(percent)
    if percent[0] == "y":
        return True
    elif percent[0] == "n":
        return False


def dealer_response(x, y, z):  # 확률적으로 딜러의 대답을 결정
    response = ["A"] * x + ["B"] * y + ["C"] * z
    random.shuffle(response)
    if response[0] == "A":
        return "A"
    elif response[0] == "B":
        return "B"
    elif response[0] == "C":
        return "C"


def dealer_response2(x, y):
    response = ["A"] * x + ["B"] * y
    random.shuffle(response)
    if response[0] == "A":
        return "A"
    elif response[0] == "B":
        return "B"


def dealer_response3(x, y, z, k):  # 확률적으로 딜러의 대답을 결정
    response = ["A"] * x + ["B"] * y + ["C"] * z + ["D"] * k
    random.shuffle(response)
    if response[0] == "A":
        return "A"
    elif response[0] == "B":
        return "B"
    elif response[0] == "C":
        return "C"
    elif response[0] == "D":
        return "D"


def card_sorting_player(player):
    playerlist = [[]] * len(player)
    for i in range(len(player)):
        playerlist[i] = [player[i]["suit"], player[i]["rank"]]
        if str(playerlist[i][1]).isdigit() == False:
            if playerlist[i][1] == "J":
                playerlist[i][1] = 11
            elif playerlist[i][1] == "Q":
                playerlist[i][1] = 12
            elif playerlist[i][1] == "K":
                playerlist[i][1] = 13
            elif playerlist[i][1] == "A":  # 만약 A,2,3,4,5 의 경우 A = 1
                playerlist[i][1] = 14
    playerlist = sorted(playerlist, key=lambda player: player[1])
    for i in range(len(player)):
        if int(playerlist[i][1]) == 11:
            playerlist[i][1] = "J"
        elif int(playerlist[i][1]) == 12:
            playerlist[i][1] = "Q"
        elif int(playerlist[i][1]) == 13:
            playerlist[i][1] = "K"
        elif int(playerlist[i][1]) == 14:
            playerlist[i][1] = "A"
    return playerlist


def card_sorting_dealer(dealer):
    dealerlist = [[]] * len(dealer)
    for i in range(len(dealer)):
        dealerlist[i] = [dealer[i]["suit"], dealer[i]["rank"]]
        if str(dealerlist[i][1]).isdigit() == False:
            if dealerlist[i][1] == "J":
                dealerlist[i][1] = 11
            elif dealerlist[i][1] == "Q":
                dealerlist[i][1] = 12
            elif dealerlist[i][1] == "K":
                dealerlist[i][1] = 13
            elif dealerlist[i][1] == "A":  # 만약 A,2,3,4,5 의 경우 A = 1
                dealerlist[i][1] = 14
    dealerlist = sorted(dealerlist, key=lambda dealer: dealer[1])
    for i in range(len(dealer)):
        if int(dealerlist[i][1]) == 11:
            dealerlist[i][1] = "J"
        elif int(dealerlist[i][1]) == 12:
            dealerlist[i][1] = "Q"
        elif int(dealerlist[i][1]) == 13:
            dealerlist[i][1] = "K"
        elif int(dealerlist[i][1]) == 14:
            dealerlist[i][1] = "A"
    return dealerlist


def jokbo(realcards):
    cards = realcards[:]
    for i in range(len(cards)):
        if cards[i][1] == "J":
            cards[i][1] = 11
        if cards[i][1] == "Q":
            cards[i][1] = 12
        if cards[i][1] == "K":
            cards[i][1] = 13
        if cards[i][1] == "A":
            cards[i][1] = 14
    for i in range(0, 4):
        if cards[i][1] == cards[i + 1][1]:
            for j in range(i + 1, 4):
                if cards[j][1] == cards[j + 1][1]:
                    return 2  # 투페어일경우
            return 1  # 원페어일경우

    for i in range(0, 3):
        if cards[i][1] == cards[i + 1][1] == cards[i + 2][1]:
            for j in range(i + 2, len(cards) - 1):
                if cards[j][1] == cards[j + 1][1]:
                    return 9  # 풀하우스
            return 3  # 똑같은 숫자 3장

    for i in range(0, 4):
        if cards[i][1] == 14:
            if cards[0][1] == "2" and cards[1][1] == "3" and cards[2][1] == "4" and cards[3][1] == "5":
                return 4  # A 2 3 4 5 일 경우
    if int(cards[1][1]) - int(cards[0][1]) == int(cards[2][1]) - int(cards[1][1]) == int(cards[3][1]) - int(
            cards[2][1]) == int(cards[4][1]) - int(cards[3][1]) == 1:
        return 4  # 스트레이트

    if cards[0][0] == cards[1][0] == cards[2][0] == cards[3][0] == cards[4][0]:
        if cards[0][1] == "10" and cards[1][1] == 11 and cards[2][1] == 12 and cards[3][1] == 13 and cards[4][1] == 14:
            return 100  # 로얄 스트레이트 플러시
        if cards[1][1] - cards[0][1] == cards[2][1] - cards[1][1] == cards[3][1] - cards[2][1] == cards[4][1] - \
                cards[3][1] == 1:
            return 50  # 스트레이트 플러시
        return 5  # 플러시(같은 문자)

    for i in range(0, 1):
        if cards[i][1] == cards[i + 1][1] == cards[i + 2][1] == cards[i + 3][1]:
            return 30  # 포카드

    else:
        return 0


def first_one(person, dealercards, chips, money):
    dealercheck = False  # 체크를 하면 True으로 바뀜
    personcheck = False  # 체크를 하면 True으로 바뀜
    dealergiveup = 1  # 딜러가 다이했을때 0으로 변환
    persongiveup = 1  # 플레이어가 다이했을때 0으로 변환
    people = 0  # 다음함수(또는 턴)에서 people이 0 일때는 딜러가, 1일때는 플레이어가 먼저 함
    dealerallin = False
    personallin = False
    bettingmoney = 0  # 플레이어가 총 거는 금액
    dealermoney = 0  # 딜러가 총 거는 금액
    while True:
        if person == True:  # 손님이 첫번째 순서로 걸렸을때,
            if dealercheck == True:  # 딜러가 체크를 한 상태일때(플레이어는 체크불가)
                print("Your turn!")
                response = input("Enter your response: (Enter Die / Bet)")
                while not response == "Die" and response != "Bet":
                    response = input("Enter the word Die / Bet")
            elif dealercheck == False:  # 딜러가 체크를 하지 않았을 때
                print("You are first!")
                response = input("Enter your response: (Enter Die / Check / Bet)")
                while not response == "Die" and response != "Check" and response != "Bet":
                    response = input("Enter the word Die / Check / Bet")
            if response == "Die":
                persongiveup = 0
                return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                # 손님 첫번째 배팅순서이지만 손님이 다이를 했으므로 바로 카드를 공개.
                break
            elif response == "Check":
                # 딜러에게 페이즈가 넘어가고 딜러가 확률적으로 체크, 다이, 페이를 결정.
                person = False  # 딜러에게 순서가 넘어감
                personcheck = True
                continue
            while response == "Bet":  # 배팅을 결정한 경우.
                playermoney = input("Enter amount to pay: ")
                if playermoney.isdigit() == False:
                    playermoney = input("Enter natural number: ")
                playermoney = int(playermoney)
                bettingmoney = bettingmoney + playermoney
                if int(playermoney) <= 0:
                    playermoney = int(input("Enter the number: "))
                if int(playermoney) > int(chips):  # 칩의 보유개수가 베팅하려는 금액보다 적을때
                    x = input("Do you want to All-in your chips?: (y/n)")
                    while not x == "y" and x != "n":
                        x = input("Response with (y/n)")
                    if x == "n":
                        continue
                    elif x == "y":
                        chips = str(chips)
                        playermoney = chips[:]
                        chips = 0
                        money = int(money) + int(playermoney)
                        print("You paid " + str(playermoney) + " chips.")
                        people = 0
                        personallin = True
                        bettingmoney = int(playermoney)
                        return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney  # 올인을 한 경우이므로 딜러는 무조건 콜을 해야함
                        break
                else:
                    chips = int(chips) - int(playermoney)
                    money += playermoney  # 플레이어가 돈을 걸었음.
                    print("You paid " + str(playermoney) + " chips.")
                    people = 0
                    return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                    break


        elif person == False:  # 딜러가 첫번째로 베팅을 할 때
            if personcheck == True:  # 플레이어가 체크를 한 상태일때 이후 바로 next_player_turn으로 넘어감
                print("Dealer turn!")
                if jokbo(dealercards) == 1:  # 원페어
                    response = dealer_response(3, 3, 1)  # (x,y) = (다이, 배팅, 올인)
                elif jokbo(dealercards) == 2:  # 투페어
                    response = dealer_response(2, 3, 1)  # (x,y) = (다이, 배팅, 올인)
                elif jokbo(dealercards) == 3:  # 트리플
                    response = dealer_response(2, 4, 1)  # (x,y) = (다이, 배팅, 올인)
                elif jokbo(dealercards) == 4:  # 스트레이트
                    response = dealer_response(2, 7, 2)  # (x,y) = (다이, 배팅, 올인)
                elif jokbo(dealercards) == 5:  # 플러시
                    response = dealer_response(2, 4, 4)  # (x,y) = (다이, 배팅, 올인)
                elif jokbo(dealercards) == 9:  # 풀하우스
                    response = dealer_response(1, 6, 5)  # (x,y) = (다이, 배팅, 올인)
                elif jokbo(dealercards) == 30:  # 포카드
                    response = dealer_response(1, 10, 8)  # (x,y) = (다이, 베팅, 올인)
                elif jokbo(dealercards) == 50:  # 스트레이트 플러시
                    response = dealer_response(1, 9, 10)  # (x,y) = (다이, 배팅, 올인)
                elif jokbo(dealercards) == 100:  # 로열 스트레이트 플러시
                    response = dealer_response(1, 10, 11)  # (x,y) = (다이, 배팅, 올인)
                elif jokbo(dealercards) == 0:
                    response = dealer_response(5, 3, 1)  # (x,y) = (다이, 배팅, 올인)
                #
                if response == "A":
                    print("Dealer gives up the game.")  # 딜러 다이(플레이어가 체크 한 후)
                    dealergiveup = 0
                    return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                    break
                elif response == "B":  # 딜러가 돈을 검(플레이어가 체크 한 후)
                    dealer_money = dealer_response(3, 3, 3)
                    if dealer_money == "A":
                        money += 3
                        dealermoney += 3
                        print("Dealer paid 3 chips.")
                        people = 1
                        return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                        break
                    elif dealer_money == "B":
                        money += 5
                        dealermoney += 5
                        print("Dealer paid 5 chips.")
                        people = 1
                        return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                        break
                    elif dealer_money == "C":
                        money += 7
                        dealermoney += 7
                        print("Dealer paid 7 chips.")
                        people = 1
                        return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                        break
                elif response == "C":  # 딜러가 올인함
                    print("Dealer all-in his chips.")
                    money = int(money) + 30
                    dealermoney += 30
                    dealerallin = True
                    return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                    break

            else:  # 플레이어가 체크를 하지 않았고, 딜러가 첫 배팅을 할 때. 딜러가 배팅을 했다면 next_player_turn()으로 넘어감
                print("Dealer is first!")
                if jokbo(dealercards) == 1:  # 원페어
                    response = dealer_response3(3, 3, 2, 1)  # (x,y,z) = (다이, 체크, 배팅, 올인)
                elif jokbo(dealercards) == 2:  # 투페어
                    response = dealer_response3(2, 3, 3, 1)  # (x,y,z) = (다이, 체크, 배팅, 올인)
                elif jokbo(dealercards) == 3:  # 트리플
                    response = dealer_response3(2, 3, 5, 2)  # (x,y,z) = (다이, 체크, 배팅, 올인)
                elif jokbo(dealercards) == 4:  # 스트레이트
                    response = dealer_response3(2, 3, 8, 4)  # (x,y,z) = (다이, 체크, 배팅, 올인)
                elif jokbo(dealercards) == 5:  # 플러시
                    response = dealer_response3(2, 2, 6, 4)  # (x,y,z) = (다이, 체크, 배팅, 올인)
                elif jokbo(dealercards) == 9:  # 풀하우스
                    response = dealer_response3(1, 2, 7, 6)  # (x,y,z) = (다이, 체크, 배팅, 올인)
                elif jokbo(dealercards) == 30:  # 포카드
                    response = dealer_response3(1, 2, 9, 10)  # (x,y,z) = (다이, 체크, 배팅, 올인)
                elif jokbo(dealercards) == 50:  # 스트레이트 플러시
                    response = dealer_response3(1, 3, 9, 10)  # (x,y,z) = (다이, 체크, 배팅, 올인)
                elif jokbo(dealercards) == 100:  # 로열 스트레이트 플러시
                    response = dealer_response3(1, 3, 10, 13)  # (x,y,z) = (다이, 체크, 배팅, 올인)
                elif jokbo(dealercards) == 0:
                    response = dealer_response3(3, 2, 1, 1)  # (x,y,z) = (다이, 체크, 배팅, 올인)
                #
                if response == "A":
                    print("Dealer gives up the game.")  # 딜러 다이
                    dealergiveup = 0
                    return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                    break
                elif response == "B":
                    print("Dealer checked his turn!")  # 딜러 체크
                    dealercheck = True
                    person = True
                    continue
                elif response == "C":  # 딜러 배팅
                    dealer_money = dealer_response(3, 3, 3)
                    if dealer_money == "A":
                        money += 3
                        dealermoney += 3
                        print("Dealer paid 3 chips.")
                        people = 1
                        return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                        break
                    elif dealer_money == "B":
                        money += 5
                        dealermoney += 5
                        print("Dealer paid 5 chips.")
                        people = 1
                        return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                        break
                    elif dealer_money == "C":
                        money += 7
                        dealermoney += 7
                        print("Dealer paid 7 chips.")
                        people = 1
                        return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                        break
                elif response == "D":  # 딜러 올인
                    print("Dealer all-in his chips.")
                    money = int(money) + 30
                    dealermoney += 30
                    dealerallin = True
                    return persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney
                    break


def next_step(dealercards, persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney,
              dealermoney):
    while True:
        if people == 1:  # 플레이어턴
            print("Your turn!")
            if dealerallin == True:
                response = input("Enter your response: (Die / Call)")
                while not response == "Die" and response != "Call":
                    response = input("Enter the response with Die / Call: ")
            else:
                response = input("Enter your response: (Die / Call / Raise)")
                while not response == "Die" and response != "Call" and response != "Raise":
                    response = input("Enter the response with Die / Call / Raise: ")
            if response == "Die":
                persongiveup = 0
                return persongiveup, dealergiveup, money, chips, personallin, bettingmoney, dealermoney
                break
            elif response == "Call":  # 딜러가 다이를 하지 않는 이상 돈이 걸어진 상태일 것임.
                print("You called this game.")
                paying = int(dealermoney) - int(bettingmoney)
                money = int(money) + int(paying)
                chips = int(chips) - int(paying)
                bettingmoney = bettingmoney + int(paying)
                return persongiveup, dealergiveup, money, chips, personallin, bettingmoney, dealermoney
            elif response == "Raise":
                while people == 1:
                    raise_response = input("How much do you want to raise?: (Enter number)")
                    while int(raise_response) == ValueError:
                        print("Please enter the number.")
                    if int(raise_response) + int(dealermoney) - int(bettingmoney) >= int(chips):
                        allin = input("Do you want to all-in your chips?: (y/n)")
                        while not allin == "y" and allin != "n":
                            allin = input("Please response with word 'y' or 'n'.")
                        if allin == "y":  # 올인을 하고싶은 경우
                            print("You all-in your chips.")
                            chips = str(chips)
                            raise_response = chips[:]
                            chips = 0
                            money = int(money) + int(raise_response)
                            personallin = True
                            bettingmoney = bettingmoney + int(raise_response)
                            return persongiveup, dealergiveup, money, chips, personallin, bettingmoney, dealermoney
                            break
                        elif allin == "n":  # 올인을 하고싶지 않은 경우
                            continue
                    else:
                        print("You raised " + str(raise_response) + " chips.")
                        paying = int(dealermoney) - int(bettingmoney)
                        money = int(money) + int(raise_response)
                        people = 0
                        bettingmoney = bettingmoney + int(raise_response) + int(paying)
                        chips = int(chips) - int(paying) - int(raise_response)
                        continue

        elif people == 0:
            print("Dealer's turn!")
            if jokbo(dealercards) == 1:  # 원페어
                response = dealer_response3(2, 3, 2, 1)  # (x,y,z) = (다이, 체크, 배팅, 올인)
            elif jokbo(dealercards) == 2:  # 투페어
                response = dealer_response3(2, 3, 3, 1)  # (x,y,z) = (다이, 체크, 배팅, 올인)
            elif jokbo(dealercards) == 3:  # 트리플
                response = dealer_response3(2, 3, 5, 2)  # (x,y,z) = (다이, 체크, 배팅, 올인)
            elif jokbo(dealercards) == 4:  # 스트레이트
                response = dealer_response3(2, 3, 8, 4)  # (x,y,z) = (다이, 체크, 배팅, 올인)
            elif jokbo(dealercards) == 5:  # 플러시
                response = dealer_response3(2, 2, 6, 4)  # (x,y,z) = (다이, 체크, 배팅, 올인)
            elif jokbo(dealercards) == 9:  # 풀하우스
                response = dealer_response3(1, 2, 7, 6)  # (x,y,z) = (다이, 체크, 배팅, 올인)
            elif jokbo(dealercards) == 30:  # 포카드
                response = dealer_response3(1, 2, 9, 10)  # (x,y,z) = (다이, 체크, 배팅, 올인)
            elif jokbo(dealercards) == 50:  # 스트레이트 플러시
                response = dealer_response3(1, 3, 9, 10)  # (x,y,z) = (다이, 체크, 배팅, 올인)
            elif jokbo(dealercards) == 100:  # 로열 스트레이트 플러시
                response = dealer_response3(1, 3, 10, 13)  # (x,y,z) = (다이, 체크, 배팅, 올인)
            elif jokbo(dealercards) == 0:
                response = dealer_response3(3, 2, 1, 1)  # (x,y,z) = (다이, 체크, 배팅, 올인)
            #
            if response == "A":  # 딜러 다이
                print("Dealer give up this game.")
                dealergiveup = 0
                return persongiveup, dealergiveup, money, chips, personallin, bettingmoney, dealermoney
                break
            elif response == "B":  # 딜러 콜
                print("Dealer called this game.")
                paying = int(bettingmoney) - int(dealermoney)
                money = int(money) + int(paying)
                return persongiveup, dealergiveup, money, chips, personallin, bettingmoney, dealermoney
                break
            elif response == "C":  # 딜러 레이즈
                dealer_money = dealer_response(3, 3, 3)
                if dealer_money == "A":
                    print("Dealer raised 3 chips!")
                    money = int(money) + 3
                    paying = int(bettingmoney) - int(dealermoney)
                    dealermoney = int(dealermoney) + int(paying) + 3
                    people = 1
                    continue
                elif dealer_money == "B":
                    print("Dealer raised 5 chips!")
                    money = int(money) + 5
                    paying = int(bettingmoney) - int(dealermoney)
                    dealermoney = int(dealermoney) + int(paying) + 5
                    people = 1
                    continue
                elif dealer_money == "C":
                    print("Dealer raised 7 chips!")
                    money = int(money) + 7
                    paying = int(bettingmoney) - int(dealermoney)
                    dealermoney = int(dealermoney) + int(paying) + 7
                    people = 1
                    continue
            elif response == "D":  # 딜러 올인
                print("Dealer all-in his chips.")
                money = int(money) + 30
                dealermoney += 30
                dealerallin = True
                return persongiveup, dealergiveup, money, chips, personallin, bettingmoney, dealermoney
                break


def card_game_Five_Poker():
    print("Welcome to SMaSH's Five Poker Game!")
    print("-----")
    username, tries, wins, chips, debt, debtchips, members = login(load_members())
    while True:
        deck = fresh_deck()
        money = 0
        dealer = []
        player = []
        card, deck = hit(deck)  # 손님 첫번째카드
        player.append(card)
        card, deck = hit(deck)  # 딜러 첫번째카드
        dealer.append(card)
        card, deck = hit(deck)  # 손님 두번째카드
        player.append(card)
        card, deck = hit(deck)  # 딜러 두번째카드
        dealer.append(card)
        card, deck = hit(deck)  # 손님 세번째카드
        player.append(card)
        card, deck = hit(deck)  # 딜러 세번째카드
        dealer.append(card)
        card, deck = hit(deck)  # 손님 네번째카드
        player.append(card)
        card, deck = hit(deck)  # 딜러 네번째카드
        dealer.append(card)
        card, deck = hit(deck)  # 손님 다섯번째카드
        player.append(card)
        card, deck = hit(deck)  # 딜러 다섯번째카드
        dealer.append(card)
        playercards = card_sorting_player(player)
        dealercards = card_sorting_dealer(dealer)
        show_cards(player, "Your cards are:")
        cardchange = more("Do you want to change your card?")
        cardroom = []
        cardcount = 0
        while cardchange == True:  # 손님이 카드를 바꾸는걸 원했을 때,
            cardcount = cardcount + 1
            for i in range(5):
                print(str(i + 1) + ".", player[i]["suit"], player[i]["rank"])
                cardroom.append([player[i]["suit"], player[i]["rank"]])
            while True:
                try:
                    changing = int(input("Which card do you want to change?: (Write number) %s. " % cardcount))
                    if not 1 <= int(changing) <= 5: raise not_in_number
                    break
                except ValueError:
                    print("Write natural number")
                except not_in_number:
                    print("Write natural number in 1 ~ 5")
            if changing == 1:
                card, deck = hit(deck)
                player[0] = card
            elif changing == 2:
                card, deck = hit(deck)
                player[1] = card
            elif changing == 3:
                card, deck = hit(deck)
                player[2] = card
            elif changing == 4:
                card, deck = hit(deck)
                player[3] = card
            elif changing == 5:
                card, deck = hit(deck)
                player[4] = card
            show_cards(player, "Your cards are:")
            if cardcount >= 5:
                break
            else:
                x = more("Do you want to change more card?: (y/n)")
                if x == True:  # 카드를 더 바꾸고 싶은 경우
                    continue
                elif x == False:  # 카드를 그만 바꾸려는 경우
                    break
        playercards = card_sorting_player(player)
        person = who_is_first()
        persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney = first_one(person, dealercards, chips, money)
        dealercards = card_sorting_dealer(dealer)
        if dealergiveup == 0:  # 첫번째 턴에서 딜러가 다이했을 때
            print("You won this game!")
            show_cards_listed(playercards, "Your cards are: ")
            show_cards_listed(dealercards, "Dealer cards are: ")
            wins += 1
            print("You earned " + str(money * 2) + " chips.")
            chips = int(chips) + int(money) * 2
            if debt == True and int(chips) > 20:
                debtchips = int(debtchips) - 20
                print("You repay 20 chips!")
                chips = int(chips) - 20
                if int(debtchips) == 0:
                    debt = False
            if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                chips = int(chips) - 8
                print("You lost additional 8 chips for penalty.")
        elif persongiveup == 0:  # 첫번째 턴에서 플레이어가 다이했을 때
            print("Dealer won this game.")
            show_cards_listed(playercards, "Your cards are: ")
            show_cards_listed(dealercards, "Dealer cards are: ")
            print("you lost " + str(bettingmoney) + "chips.")
            chips = int(chips) - int(bettingmoney)
            if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                chips = int(chips) - 8
                print("You lost additional 8 chips for penalty.")
            if int(chips) <= 0:
                debtchips += 20
                chips = 0
                chips = int(chips) + 20
                debt = True
                print("You owe 20 chips.")
        elif dealerallin == True or personallin == True:  # 첫번째 턴에서 누군가가 올인을 했을 때
            if jokbo(dealercards) > jokbo(playercards):  # 진경우
                countdown(5)
                show_cards_listed(playercards, "Your cards are: ")
                show_cards_listed(dealercards, "Dealer cards are: ")
                print("Dealer won this game!")
                chips = int(chips) - int(bettingmoney)
                print("You lost " + str(bettingmoney) + " chips.")
                if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                    chips = int(chips) - 8
                    print("You lost additional 8 chips for penalty.")
                if int(chips) <= 0:
                    chips = 0
                    chips = int(chips) + 20
                    debtchips += 20
                    debt = True
                    print("You owe 20 chips.")
            elif jokbo(dealercards) < jokbo(playercards):  # 이긴경우
                countdown(5)
                show_cards_listed(playercards, "Your cards are: ")
                show_cards_listed(dealercards, "Dealer cards are: ")
                print("You won this game!!")
                wins += 1
                chips = int(chips) + int(money) * 2
                print("You earned " + str(money * 2) + " chips.")
                if debt == True and int(chips) > 20:
                    debtchips = int(debtchips) - 20
                    print("You repay 20 chips!")
                    chips = int(chips) - 20
                    if int(debtchips) == 0:
                        debt = False
                if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                    chips = int(chips) - 8
                    print("You lost additional 8 chips for penalty.")
                if int(chips) <= 0:
                    debtchips += 20
                    chips = 0
                    chips = int(chips) + 20
                    debt = True
                    print("You owe 20 chips.")


            elif jokbo(playercards) == jokbo(dealercards):  # 비긴경우
                countdown(5)
                show_cards_listed(playercards, "Your cards are: ")
                show_cards_listed(dealercards, "Dealer cards are: ")
                print("We draw this game.")
                chips = int(chips) + bettingmoney
                if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                    chips = int(chips) - 8
                    print("You lost additional 8 chips for penalty.")
                if int(chips) <= 0:
                    debtchips += 20
                    chips = 0
                    chips = int(chips) + 20
                    debt = True
                    print("You owe 20 chips.")
        elif persongiveup == 1 and dealergiveup == 1:  # 누군가가 첫번째 턴에서 다이를 하거나 올인을 하지 않았을 경우
            persongiveup, dealergiveup, money, chips, personallin, bettingmoney, dealermoney = next_step(dealercards, persongiveup, dealergiveup, money, chips, people, dealerallin, personallin, bettingmoney, dealermoney)
            dealercards = card_sorting_dealer(dealer)
            if dealergiveup == 0:  # 두번째 턴이상에서 딜러가 다이했을 때
                print("You won this game!")
                show_cards_listed(playercards, "Your cards are: ")
                show_cards_listed(dealercards, "Dealer cards are: ")
                wins += 1
                print("You earned " + str(money * 2) + " chips.")
                chips = int(chips) + int(money) * 2
                if debt == True and int(chips) > 20:
                    debtchips = int(debtchips) - 20
                    print("You repay 20 chips!")
                    chips = int(chips) - 20
                    if int(debtchips) == 0:
                        debt = False
                if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                    chips = int(chips) - 8
                    print("You lost additional 8 chips for penalty.")
                if int(chips) <= 0:
                    debtchips += 20
                    chips = 0
                    chips = int(chips) + 20
                    debt = True
                    print("You owe 20 chips.")
            elif persongiveup == 0:  # 두번째 턴 이상에서 플레이어가 다이했을 때
                print("Dealer won this game.")
                show_cards_listed(playercards, "Your cards are: ")
                show_cards_listed(dealercards, "Dealer cards are: ")
                print("you lost " + str(bettingmoney) + " chips.")
                chips = int(chips) - int(bettingmoney)
                if int(chips) <= 0:  # 칩의 개수가 음수일 때 대출받음
                    debtchips += 20
                    chips = 0
                    chips = int(chips) + 20
                    debt = True
                    print("You owe 20 chips.")
            elif dealerallin == True or personallin == True:  # 두번째 턴 이상에서 딜러나 플레이어 둘 중 누군가가 올인을 했을 때
                if jokbo(dealercards) > jokbo(playercards):  # 진경우
                    countdown(5)
                    show_cards_listed(playercards, "Your cards are: ")
                    show_cards_listed(dealercards, "Dealer cards are: ")
                    print("Dealer won this game!")
                    chips = int(chips) - int(bettingmoney)
                    print("You lost " + str(bettingmoney) + " chips.")
                    if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                        chips = int(chips) - 8
                        print("You lost additional 8 chips for penalty.")
                    if int(chips) <= 0:
                        debtchips += 20
                        chips = 0
                        chips = int(chips) + 20
                        debt = True
                        print("You owe 20 chips.")
                elif jokbo(dealercards) < jokbo(playercards):  # 이긴경우
                    countdown(5)
                    show_cards_listed(playercards, "Your cards are: ")
                    show_cards_listed(dealercards, "Dealer cards are: ")
                    print("You won this game!!")
                    wins += 1
                    chips = int(chips) + int(money) * 2
                    print("You earned " + str(money * 2) + " chips.")
                    if debt == True and int(chips) > 20:
                        debtchips = int(debtchips) - 20
                        print("You repay 20 chips!")
                        chips = int(chips) - 20
                        if int(debtchips) == 0:
                            debt = False
                    if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                        chips = int(chips) - 8
                        print("You lost additional 8 chips for penalty.")
                    if int(chips) <= 0:
                        debtchips += 20
                        chips = 0
                        chips = int(chips) + 20
                        debt = True
                        print("You owe 20 chips.")


                elif jokbo(playercards) == jokbo(dealercards):  # 비긴경우
                    countdown(5)
                    show_cards_listed(playercards, "Your cards are: ")
                    show_cards_listed(dealercards, "Dealer cards are: ")
                    print("We draw this game.")
                    chips = int(chips) + bettingmoney
                    if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                        chips = int(chips) - 8
                        print("You lost additional 8 chips for penalty.")
                    if int(chips) <= 0:
                        debtchips += 20
                        chips = 0
                        chips = int(chips) + 20
                        debt = True
                        print("You owe 20 chips.")
            else:  # 그 누구도 올인을 하지 않았을 때
                if jokbo(dealercards) > jokbo(playercards):  # 진경우
                    countdown(5)
                    show_cards_listed(playercards, "Your cards are: ")
                    show_cards_listed(dealercards, "Dealer cards are: ")
                    print("Dealer won this game!")
                    chips = int(chips) - int(bettingmoney)
                    print("You lost " + str(bettingmoney) + " chips.")
                    if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                        chips = int(chips) - 8
                        print("You lost additional 8 chips for penalty.")
                    if int(chips) <= 0:
                        debtchips += 20
                        chips = 0
                        chips = int(chips) + 20
                        debt = True
                        print("You owe 20 chips.")
                elif jokbo(dealercards) < jokbo(playercards):  # 이긴경우
                    countdown(5)
                    show_cards_listed(playercards, "Your cards are: ")
                    show_cards_listed(dealercards, "Dealer cards are: ")
                    print("You won this game!!")
                    wins += 1
                    chips = int(chips) + int(money) * 2
                    print("You earned " + str(money * 2) + " chips.")
                    if debt == True and int(chips) > 20:
                        debtchips = int(debtchips) - 20
                        print("You repay 20 chips!")
                        chips = int(chips) - 20
                        if int(debtchips) == 0:
                            debt = False
                    if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                        chips = int(chips) - 8
                        print("You lost additional 8 chips for penalty.")
                    if int(chips) <= 0:
                        debtchips += 20
                        chips = 0
                        chips = int(chips) + 20
                        debt = True
                        print("You owe 20 chips.")


                elif jokbo(playercards) == jokbo(dealercards):  # 비긴경우
                    countdown(5)
                    show_cards_listed(playercards, "Your cards are: ")
                    show_cards_listed(dealercards, "Dealer cards are: ")
                    print("We draw this game.")
                    chips = int(chips) + bettingmoney
                    if jokbo(playercards) == 1 or jokbo(playercards) == 0:
                        chips = int(chips) - 8
                        print("You lost additional 8 chips for penalty.")
                    if int(chips) <= 0:
                        debtchips += 20
                        chips = 0
                        chips = int(chips) + 20
                        debt = True
                        print("You owe 20 chips.")
        print("You have " + str(chips) + " chips.")
        tries += 1
        print("You played " + str(tries) + " games and won " + str(wins) + " games.")
        passwd = members[username][0]
        members[username] = (passwd, int(tries), float(wins), int(chips), str(debt), str(debtchips))
        store_members(members)
        again = more("Do you want to play more?: (y/n)")
        if again == True:
            continue
        elif again == False:
            print("Bye!")
            break


card_game_Five_Poker()
