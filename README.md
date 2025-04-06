# **Python数据分析实战：微信好友地域分布可视化教程**

本教程将带你完整实现一个微信好友地域分布分析工具，使用Python的Pandas进行数据处理，Seaborn和Matplotlib进行可视化，并将结果保存为图片。这个项目非常适合数据分析初学者练手，也可以作为个人技术博客的优质内容。

---

## **一、项目概述**
### **1.1 功能目标**
- 读取微信好友信息CSV文件
- 分析好友的省份和城市分布
- 生成三种可视化图表并保存为图片：
  1. 好友省份分布柱状图
  2. 好友城市分布柱状图
  3. 好友省份占比饼图

### **1.2 技术栈**
- **Pandas** - 数据处理
- **Matplotlib** - 基础可视化
- **Seaborn** - 高级统计图表
- **编码处理** - 解决中文文件读取问题

---

## **二、环境准备**
### **2.1 安装依赖库**
```bash
pip install pandas matplotlib seaborn
```

### **2.2 文件准备**
确保你的微信好友信息CSV文件（如`我的微信好友信息.csv`）包含以下字段：
```csv
,City,NickName,Province,Sex,Signature
0,,吴迪,,1,时间旅行者
1,,孟凡坤,,1,
...
```

---

## **三、代码实现与解析**
### **3.1 完整代码**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（解决中文乱码）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

def load_data():
    """加载CSV数据，处理编码问题"""
    try:
        df = pd.read_csv('我的微信好友信息.csv', encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv('我的微信好友信息.csv', encoding='gbk')
    return df

def analyze_province(df):
    """分析省份分布"""
    province_data = df['Province'].value_counts().head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x=province_data.index,
        y=province_data.values,
        hue=province_data.index,  # 避免Seaborn警告
        palette="viridis",
        legend=False
    )
    plt.title("微信好友省份分布 Top 10")
    plt.xlabel("省份")
    plt.ylabel("人数")
    plt.xticks(rotation=45)  # 旋转标签
    plt.tight_layout()
    plt.savefig('province_distribution.png', dpi=300)  # 保存高清图
    plt.close()

def analyze_city(df):
    """分析城市分布"""
    city_data = df['City'].value_counts().head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x=city_data.index,
        y=city_data.values,
        hue=city_data.index,
        palette="magma",
        legend=False
    )
    plt.title("微信好友城市分布 Top 10")
    plt.xlabel("城市")
    plt.ylabel("人数")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('city_distribution.png', dpi=300)
    plt.close()

def analyze_pie_chart(df):
    """分析省份占比（饼图）"""
    province_data = df['Province'].value_counts()
    province_pie = province_data[province_data >= 5]  # 只显示占比≥5%的省份
    plt.figure(figsize=(10, 10))
    plt.pie(
        province_pie,
        labels=province_pie.index,
        autopct='%1.1f%%',  # 显示百分比
        startangle=90,      # 起始角度
        colors=sns.color_palette("viridis", len(province_pie))
    )
    plt.title("微信好友省份占比")
    plt.tight_layout()
    plt.savefig('province_pie.png', dpi=300)
    plt.close()

if __name__ == "__main__":
    df = load_data()
    analyze_province(df)
    analyze_city(df)
    analyze_pie_chart(df)
    print("分析完成！图表已保存为PNG文件。")
```

---

## **四、代码模块详解**
### **4.1 数据加载 (`load_data`)**
- **功能**：读取CSV文件，自动处理编码问题（UTF-8或GBK）。
- **关键点**：
  - `pd.read_csv()` 默认使用UTF-8，如果失败则尝试GBK。
  - 避免因编码问题导致的 `UnicodeDecodeError`。

### **4.2 省份分析 (`analyze_province`)**
- **数据处理**：
  - `df['Province'].value_counts().head(10)` 统计前10省份。
- **可视化**：
  - 使用Seaborn的 `barplot` 绘制柱状图。
  - `palette="viridis"` 设置颜色。
  - `plt.xticks(rotation=45)` 旋转X轴标签，避免重叠。
- **保存图片**：
  - `plt.savefig('province_distribution.png', dpi=300)` 保存高清图。

### **4.3 城市分析 (`analyze_city`)**
- 类似省份分析，但使用 `magma` 调色板。

### **4.4 饼图分析 (`analyze_pie_chart`)**
- **数据处理**：
  - 只显示占比≥5%的省份，避免饼图过于碎片化。
- **可视化**：
  - `autopct='%1.1f%%'` 显示百分比。
  - `startangle=90` 从90度开始绘制，提升可读性。

---

## **五、运行结果**
执行代码后，会生成3张图片：
1. `province_distribution.png` - 省份分布柱状图  ![province_distribution](https://github.com/user-attachments/assets/bbfe1ca0-d33f-4fa0-8390-3a580c8b7342)
2. `city_distribution.png` - 城市分布柱状图  ![city_distribution](https://github.com/user-attachments/assets/aec2a946-bfcc-4537-b33a-5854b292cdf6)
3. `province_pie.png` - 省份占比饼图  ![province_pie](https://github.com/user-attachments/assets/9c095f84-8599-43ef-a803-3d48a3f41d91)
---

## **六、优化与扩展**
### **6.1 优化建议**
- **动态路径**：使用 `os.path` 处理文件路径，增强跨平台兼容性。
- **异常处理**：增加对文件不存在、空数据的检查。
- **交互式图表**：用 `Plotly` 替代Matplotlib，生成可交互HTML图表。

### **6.2 扩展方向**
1. **性别分布分析**  
   ```python
   gender_data = df['Sex'].value_counts()
   ```
2. **签名关键词分析**（使用 `jieba` 分词 + 词云）  
   ```python
   from wordcloud import WordCloud
   ```

---

## **七、总结**
本教程实现了一个完整的微信好友地域分析工具，涵盖：
- **数据读取**（Pandas + 编码处理）
- **统计分析**（`value_counts`）
- **可视化**（Seaborn柱状图 + Matplotlib饼图）
- **结果导出**（保存为PNG）
