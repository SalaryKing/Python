# **利用DeepSeek完成数据分析可视化：从数据到图表的完整实践记录**

## **一、项目背景**
最近我需要分析微信好友的地域分布数据，将CSV格式的好友信息（包含省份、城市等字段）进行可视化展示。通过DeepSeek Chat的指导，我成功用Python实现了数据读取、清洗、分析和可视化全流程，并将结果保存为图片。本文将完整记录这个过程。

---

## **二、技术栈**
- **数据读取**：Pandas（支持自动检测文件编码）
- **数据分析**：value_counts() 统计分布
- **可视化**：Matplotlib + Seaborn（美观的统计图表）
- **部署**：Git版本控制 + Markdown文档

---

## **三、完整实现步骤**

### **1. 数据准备**
微信好友信息CSV格式示例：
```csv
,City,Province
0,北京,北京
1,上海,上海
2,,未知
```

### **2. 关键代码实现**
#### (1) 数据加载（自动处理编码）
```python
try:
    df = pd.read_csv('wechat_friends.csv', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('wechat_friends.csv', encoding='gbk')
```

#### (2) 省份分布分析
```python
province_data = df['Province'].value_counts().head(10)
sns.barplot(x=province_data.index, 
            y=province_data.values,
            palette="viridis")
plt.savefig('province_dist.png')
```

#### (3) 城市分布分析
```python
city_data = df['City'].value_counts().head(10)
sns.barplot(x=city_data.index,
            y=city_data.values,
            palette="magma")
```

#### (4) 结果保存
```python
plt.savefig('city_dist.png', dpi=300, bbox_inches='tight')
```

---

## **四、遇到的问题及解决方案**
### **1. 中文编码问题**
- **现象**：`UnicodeDecodeError`
- **解决**：自动尝试UTF-8和GBK编码

### **2. 可视化报错**
- **现象**：`AttributeError: tostring_rgb`
- **解决**：改用`plt.savefig()`直接保存图片

### **3. Git推送冲突**
- **现象**：`! [rejected] main -> main`
- **解决流程**：
  ```bash
  git pull origin main
  # 解决冲突后
  git push origin main
  ```

---

## **五、最终成果展示**
| 图表类型 | 示例输出 |
|----------|----------|
| 省份分布 | ![province_distribution](https://github.com/user-attachments/assets/d6b8082d-b437-4329-a0da-177700912f92)
|
| 城市分布 | ![city_distribution](https://github.com/user-attachments/assets/3033eb28-f09c-48d2-b154-0f70411fc449)
|
| 省份占比 | ![province_pie](https://github.com/user-attachments/assets/b5f2ceca-5ad1-4524-b093-9c59e1a9a7ad)
 |

---

## **六、经验总结**
1. **编码处理**：中文CSV文件优先尝试`gbk`编码
2. **可视化技巧**：
   - Seaborn的`palette`参数快速美化图表
   - `plt.tight_layout()`避免标签重叠
3. **版本控制**：
   - 推送前务必先`git pull`
   - 使用`-u`参数设置默认推送分支

完整代码已开源：[GitHub仓库链接](https://github.com/SalaryKing/Python/tree/main)

---

**后续计划**：  
尝试用Plotly制作交互式图表，并部署为Web应用。本次实践证明，借助DeepSeek等AI助手可以快速解决技术难题，显著提高开发效率！
