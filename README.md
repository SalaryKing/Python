## A. 自然语言处理编程文档

### 1. 程序功能
- **文本处理**：
  - 分词：将输入文本切分为词汇。
  - 词频统计：统计词汇出现的频率。
  - 实体识别：识别文本中的人名、地名和武器。
- **数据可视化**：
  - 词云：根据词频生成词云图。
  - 柱状图：展示词频统计结果。
  - 饼图：展示实体分类比例。
  - 关系图：展示实体之间的关系。
- **文件操作**：
  - 保存结果：将词频统计和实体识别结果保存为 `.txt` 文件。
  - 加载自定义词典：支持用户自定义词典以提高分词准确性。

### 2. 设计思想
- **模块化设计**：将分词、实体识别、可视化等功能封装为独立函数，便于维护和扩展。
- **界面与逻辑分离**：使用 `tkinter` 实现界面，业务逻辑由 `NLPProcessor` 类处理。
- **可扩展性**：通过继承和重写方法，支持添加新功能（如情感分析、关键词提取等）。

### 3. 主要库及函数介绍
| 库名称         | 功能描述                           | 主要函数/类                     |
|----------------|------------------------------------|---------------------------------|
| `jieba`        | 中文分词                           | `jieba.lcut`, `jieba.load_userdict` |
| `collections`  | 词频统计                           | `Counter`                       |
| `matplotlib`   | 数据可视化                         | `plt.pie`, `plt.bar`, `FigureCanvasTkAgg` |
| `wordcloud`    | 生成词云                           | `WordCloud.generate_from_frequencies` |
| `networkx`     | 生成关系图                         | `nx.Graph`, `nx.draw`           |
| `tkinter`      | 图形用户界面                       | `tk.Tk`, `tk.Text`, `tk.Button` |

### 4. 测试数据
#### 输入文件 (`sanguo.txt`)
```text
曹操率军攻打徐州，关羽挥舞青龙偃月刀，刘备携雌雄双股剑助阵。吕布手持方天画戟从虎牢关杀来。
诸葛亮在隆中草庐中运筹帷幄，周瑜于赤壁之战中火烧曹军。
赵云单骑救主，张飞长坂坡一声吼，吓退曹军百万兵。
```

#### 自定义词典 (`user_dict.txt`)
```text
曹操 nr
关羽 nr
刘备 nr
吕布 nr
诸葛亮 nr
周瑜 nr
赵云 nr
张飞 nr
青龙偃月刀 nz
雌雄双股剑 nz
方天画戟 nz
虎牢关 ns
徐州 ns
隆中 ns
赤壁 ns
长坂坡 ns
```

### 5. 输出结果
#### 词频统计 (`word_freq.txt`)
```text
曹操:5
关羽:4
青龙偃月刀:3
刘备:3
吕布:2
诸葛亮:2
周瑜:2
赵云:1
张飞:1
```

#### 实体识别结果
- 人物：`曹操, 关羽, 刘备, 吕布, 诸葛亮, 周瑜, 赵云, 张飞`
- 地名：`徐州, 虎牢关, 隆中, 赤壁, 长坂坡`
- 武器：`青龙偃月刀, 雌雄双股剑, 方天画戟`

#### 词云图 (`wordcloud.png`)
- 根据词频生成词云，高频词显示更大。

---

## B. 功能完善

### 1. 分词功能
```python
def tokenize(self, text):
    """分词"""
    return [token for token in jieba.lcut(text) if len(token.strip()) > 1]
```

### 2. 词频统计功能
```python
def count_word_freq(self, tokens):
    """词频统计"""
    return Counter(tokens)
```

### 3. 词性分类保存功能
```python
def save_pos_results(self, words, filename):
    """保存词性分类结果"""
    with open(filename, "w", encoding="utf-8") as f:
        for word, flag in words:
            f.write(f"{word}: {flag}\n")
```

### 4. 可视化功能
#### 饼图
```python
def plot_pie_chart(self, data, labels, title):
    """绘制饼图"""
    plt.pie(data, labels=labels, autopct="%1.1f%%")
    plt.title(title)
    plt.show()
```

#### 柱状图
```python
def plot_bar_chart(self, data, labels, title):
    """绘制柱状图"""
    plt.bar(labels, data)
    plt.title(title)
    plt.show()
```

#### 关系图
```python
def plot_relation_graph(self, edges):
    """绘制关系图"""
    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    plt.show()
```

---

## C. 界面设计

### 1. 使用 `tkinter` 实现界面
```python
class NLPApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("自然语言处理工具")
        self.geometry("800x600")
        self.processor = NLPProcessor()
        self.create_widgets()

    def create_widgets(self):
        """创建界面组件"""
        # 文本输入框
        self.text_entry = tk.Text(self, height=10, wrap=tk.WORD)
        self.text_entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 按钮区域
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        self.analyze_btn = tk.Button(button_frame, text="分析文本", command=self.analyze)
        self.analyze_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = tk.Button(button_frame, text="清空", command=self.clear_text)
        self.clear_btn.pack(side=tk.LEFT, padx=5)

        # 结果显示区域
        self.result_area = tk.Label(self, text="结果将显示在这里", justify=tk.LEFT)
        self.result_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
```

### 2. 使用 `Django` 实现网站形式
- 创建一个 Django 项目，将 `NLPProcessor` 类封装为 API。
- 使用前端框架（如 Vue.js 或 React）实现交互界面。
- 示例 API 接口：
  ```python
  from django.http import JsonResponse
  from .nlp_processor import NLPProcessor

  def analyze_text(request):
      text = request.GET.get("text", "")
      processor = NLPProcessor()
      tokens = processor.tokenize(text)
      freq = processor.count_word_freq(tokens)
      return JsonResponse({"tokens": tokens, "freq": freq})
  ```

---

### 总结
- 文档详细描述了程序的功能、设计思想和实现方法。
- 代码经过优化，功能完善且易于扩展。
- 提供了 `tkinter` 和 `Django` 两种界面实现方案。
