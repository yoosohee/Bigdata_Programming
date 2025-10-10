import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import rc

from ch05.common_function import get_font_name

# pip install matplotlib

#한글폰트 처리(깨짐처리)
rc('font', family=get_font_name())
plt.rcParams['axes.unicode_minus'] = False

jumsu1_data = [3.5, 4.1, 4.2, 4.5]
jumsu2_data = [3.65, 4.12, 4.23, 4.5]
index_data = [2024, 2025, 2026, 2027]

df = pd.DataFrame(
    {
        '홍길동': jumsu1_data,
        '이순신': jumsu2_data,
    }
    , index=index_data)
df.plot.line()
plt.show()