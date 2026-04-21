import random
import time

premises = [
    "市場は常に不完全だ",
    "価格は現実ではなく認識を反映する",
    "世界は均衡ではなく変化の中にある",
    "投資家は自分の認識に囚われる"
]

dynamics = [
    "その歪みはやがて拡大する",
    "トレンドは静かに始まる",
    "群衆は遅れて反応する",
    "現実とのズレが機会を生む"
]

actions = [
    "だから歪みが大きくなる前に動け",
    "だから現場を見ろ",
    "だから自分の仮説を疑え",
    "だから流れに乗れ、逆らうな",
    "だから変化の初期を捉えろ"
]

realities = [
    "多くの人はそれに気づかない",
    "だが群衆は常に遅れる",
    "そして過去に固執する",
    ""
]

while True:
    print(
        random.choice(premises) + "。" +
        random.choice(dynamics) + "。" +
        random.choice(realities) + "。" +
        random.choice(actions) + "。"
    )
    time.sleep(1)