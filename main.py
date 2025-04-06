import matplotlib
matplotlib.use('Agg')  # 解决方案1：使用非交互式后端

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
try:
    df = pd.read_csv('我的微信好友信息.csv', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('我的微信好友信息.csv', encoding='gbk')

# 数据处理
province_data = df['Province'].value_counts().head(10)
city_data = df['City'].value_counts().head(10)

# 1. 省份分布图
plt.figure(figsize=(12, 6))
sns.barplot(
    x=province_data.index,
    y=province_data.values,
    hue=province_data.index,
    palette="viridis",
    legend=False
)
plt.title("微信好友省份分布 Top 10")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('province_distribution.png')  # 保存图片
plt.close()

# 2. 城市分布图
plt.figure(figsize=(12, 6))
sns.barplot(
    x=city_data.index,
    y=city_data.values,
    hue=city_data.index,
    palette="magma",
    legend=False
)
plt.title("微信好友城市分布 Top 10")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('city_distribution.png')
plt.close()

# 3. 省份饼图
province_pie = province_data[province_data >= 5]
plt.figure(figsize=(10, 10))
plt.pie(
    province_pie,
    labels=province_pie.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette("viridis", len(province_pie))
)
plt.title("微信好友省份占比")
plt.tight_layout()
plt.savefig('province_pie.png')
plt.close()

print("图表已保存为图片文件！")