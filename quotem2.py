import random
import time

styles = [
    "theory",   # ソロス哲学
    "field",    # ロジャーズ現場
    "hybrid"    # 混合
]

theory = [
    "市場は常に不完全だ",
    "価格は現実ではなく認識を反映する",
    "投資家は自分の認識に囚われる"
]

dynamics = [
    "その歪みはやがて拡大する",
    "群衆は遅れて反応する",
    "トレンドは静かに始まる"
]

field = [
    "だが現実は現場にある",
    "スクリーンの外に答えがある",
    "世界を見なければ何もわからない"
]

endings = [
    "それに気づける者は少ない",
    "問題は、それを実行できる者が少ないことだ",
    "多くの人はそこで立ち止まる",
    ""
]

while True:
    style = random.choice(styles)

    if style == "theory":
        print(
            random.choice(theory) + "。" +
            random.choice(dynamics) + "。" +
            random.choice(endings) + "。"
        )

    elif style == "field":
        print(
            random.choice(field) + "。" +
            random.choice(endings) + "。"
        )

    else:  # hybrid
        print(
            random.choice(theory) + "。" +
            random.choice(field) + "。" +
            random.choice(dynamics) + "。"
        )
    time.sleep(1)