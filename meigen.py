import random
import time

subjects = [
    "投資とは",
    "成功とは",
    "市場は",
    "人間は",
    "リスクとは",
    "時間は",
    "複利は"
]

verbs = [
    "裏切ることがあるが",
    "単純に見えて",
    "常にあなたを試し",
    "しばしば誤解され",
    "長期的には報われ",
    "短期的には狂い",
    "静かに働き"
]

endings = [
    "最後に本質を明らかにする",
    "忍耐ある者に味方する",
    "愚かさを拡大する",
    "理解した者にだけ報いる",
    "時間とともに真価を示す",
    "群衆とは逆の結果を生む",
    "複利の力で差を広げる"
]

while True:
    s = random.choice(subjects)
    v = random.choice(verbs)
    e = random.choice(endings)
    print(s + v + e)
    time.sleep(1)
