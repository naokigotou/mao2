import random
import time

openings = [
    "投資で大切なのは",
    "私たちが学んだのは",
    "長年の経験から言えるのは",
    "シンプルだが重要なのは"
]

principles = [
    "理解できるものに投資すること",
    "優れた企業を適正な価格で買うこと",
    "長期で保有すること",
    "感情に流されないこと",
    "無理に動かないこと"
]

metaphors = [
    "野球のように、良い球が来るまで待てばいい",
    "市場は短期的には投票機だが、長期的には計量機だ",
    "潮が引いたときに、誰が裸で泳いでいたかがわかる",
    "雪だるまのように、小さな差がやがて大きくなる"
]

lessons = [
    "だから焦る必要はない",
    "だから忍耐が報われる",
    "だから多くの人が失敗する",
    "だからシンプルでいい",
    "だから規律が必要になる"
]

warnings = [
    "多くの人はこれを理解していない",
    "それでも人は短期の動きに振り回される",
    "しかし群衆は逆の行動をとる",
    "にもかかわらず無視されがちだ",
    ""
]

while True:
    sentence = (
        random.choice(openings) + "、" +
        random.choice(principles) + "だ。" +
        random.choice(metaphors) + "。" +
        random.choice(warnings) + "。" +
        random.choice(lessons) + "。"
    )

    print(sentence)
    time.sleep(1)