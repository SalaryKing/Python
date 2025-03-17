# 文本处理
import jieba  # jieba.lcut, jieba.load_userdict
from collections import Counter

# 数据可视化
import matplotlib.pyplot as plt  # plt.pie(), plt.bar()
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from wordcloud import WordCloud  # WordCloud().generate()
import networkx as nx  # nx.Graph()

# 文件处理
import json
import os

# 界面库
import tkinter as tk
from tkinter import filedialog, messagebox


class NLPProcessor:
    def __init__(self):
        self.custom_dict = "user_dict.txt"
        self.load_custom_dict()

    def load_custom_dict(self):
        """加载自定义词典"""
        if os.path.exists(self.custom_dict):
            jieba.load_userdict(self.custom_dict)
            print(f"成功加载自定义词典：{self.custom_dict}")
        else:
            print(f"警告：自定义词典 {self.custom_dict} 不存在")

    def tokenize(self, text):
        """智能分词"""
        return [token for token in jieba.lcut(text) if len(token.strip()) > 1]

    def analyze_entities(self, text):
        """实体识别"""
        words = jieba.posseg.lcut(text)
        persons = [word for word, flag in words if flag == 'nr']  # 人名
        places = [word for word, flag in words if flag == 'ns']  # 地名
        weapons = [word for word, flag in words if word in ["青龙偃月刀", "雌雄双股剑", "方天画戟"]]  # 武器
        return {"人物": persons, "地名": places, "武器": weapons}

    def generate_wordcloud(self, freq_dict, output_path="wordcloud.png"):
        """词云生成"""
        if not freq_dict:
            raise ValueError("词频数据为空，无法生成词云")

        wc = WordCloud(font_path="msyh.ttc", width=800, height=600, background_color="white")
        wc.generate_from_frequencies(freq_dict)
        plt.figure(figsize=(10, 8))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"词云已保存至 {output_path}")

    def save_results(self, data, filename):
        """保存结果到文件"""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"结果已保存至 {filename}")


class NLPApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("自然语言处理工具")
        self.geometry("800x600")
        self.processor = NLPProcessor()
        self.create_widgets()

    def create_widgets(self):
        """界面组件"""
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

    def analyze(self):
        """分析处理"""
        text = self.text_entry.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("输入为空", "请输入文本内容")
            return

        try:
            # 分词与词频统计
            tokens = self.processor.tokenize(text)
            freq = Counter(tokens)

            # 实体识别
            entities = self.processor.analyze_entities(text)

            # 显示结果
            result = f"词频统计（TOP10）：\n{freq.most_common(10)}\n\n"
            result += f"人物：{entities['人物']}\n"
            result += f"地名：{entities['地名']}\n"
            result += f"武器：{entities['武器']}\n"
            self.result_area.config(text=result)

            # 生成词云
            self.processor.generate_wordcloud(freq, "wordcloud.png")
            messagebox.showinfo("成功", "分析完成，词云已保存")
        except Exception as e:
            messagebox.showerror("错误", f"分析失败：{str(e)}")

    def clear_text(self):
        """清空输入"""
        self.text_entry.delete("1.0", tk.END)
        self.result_area.config(text="结果将显示在这里")


if __name__ == "__main__":
    app = NLPApp()
    app.mainloop()