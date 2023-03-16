_ = input()
A_cards = list(map(int,input().split()))
card_map = {}
for card in A_cards:
    if card not in card_map:
        card_map[card] = 1
    else:
        card_map[card] += 1

_ = input()
B_cards = list(map(int,input().split()))

ans = [card_map[card] if card in card_map else 0 for card in B_cards]
print(*ans)