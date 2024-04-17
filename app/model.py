from schema import ModelDayInput
from collections import defaultdict
import random


class Model:
    """заплатка что с моделью"""
    def __init__(self):
        self.data_cashe = defaultdict(dict)
        # k v r

    def forward(self, data: ModelDayInput):
        moex_df = {
            "CAPITALIZATION": data.CAPITALIZATION,
            "CLOSE": data.CLOSE,
            "DIVISOR": data.DIVISOR,
            "HIGH": data.HIGH,
            "LOW": data.LOW,
            "OPEN": data.OPEN,
            "TRADEDATE": str(data.TRADEDATE),
            "finance": data.finance,
            "economic": data.economic,
            "politic": data.politic,
        }
        val = data.CLOSE
        for k, v in moex_df.items():
            if v in self.data_cashe[k]:
                val += self.data_cashe[k][v]
            else:
                r = (random.random() - 0.3) * 6
                self.data_cashe[k][v] = r
                val += r
        return val

    def __call__(self, data: ModelDayInput):
        return self.forward(data)
