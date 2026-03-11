def step(h):
    k1, k2 = h
    return (
        (k1 + 1, k2),
        (k1 * 4, k2),
        (k1, k2 + 1),
        (k1, k2 * 4)
    )

def game(h, max_moves, move=0, path=None, results=None):
    if path is None:
        path = [h]
    if results is None:
        results = []

    # если уже победа
    if sum(h) >= 77:
        winner = 'Петя' if move % 2 == 1 else 'Ваня'
        results.append({
            'path': path,
            'end': h,
            'status': 'win',
            'winner': winner,
            'move': move
        })
        return results

    # если достигли лимита ходов, но победы нет
    if move == max_moves:
        results.append({
            'path': path,
            'end': h,
            'status': 'no win',
            'winner': None,
            'move': move
        })
        return results

    # продолжаем игру
    for next_h in step(h):
        game(next_h, max_moves, move + 1, path + [next_h], results)

    return results

res = []
f = True
for S in range(1,78):
    if f:
        results = game((4, S), 2)
        for r in results:
            if r['status'] == 'win' and r['winner'] == 'Ваня' and r['move'] == 2:
                res.append(S)
                print(S, r)
                f = False
                break
    else:
        break

# alls = {el:res.count(el) for el in set(res)}
# print(alls,'\n',[k for k, v in alls.items() if v == max(alls.values())])