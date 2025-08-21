import pandas as pd
import numpy as np

# 创建示例数据
data = {
    'product_name': [
        'Apple iPhone 13',
        'Samsung Galaxy S21',
        'Google Pixel 6',
        'OnePlus 9',
        'Xiaomi Mi 11',
        'Huawei P40',
        'Sony Xperia 1',
        'LG G8',
        'Motorola Edge',
        'Nokia 8.3'
    ],
    'description': [
        'Latest smartphone with great camera',
        'Android phone with excellent performance',
        'Google\'s flagship device',
        'Fast charging phone',
        'Affordable high-end device',
        'Premium camera phone',
        'Professional photography device',
        'Budget-friendly option',
        '5G capable smartphone',
        'Durable and reliable phone'
    ]
}

df = pd.DataFrame(data)
print("原始数据:")
print(df)
print("\n" + "="*60 + "\n")

# 要搜索的关键词列表
keywords = ['camera', 'performance', '5G']

print(f"要搜索的关键词: {keywords}")
print("\n" + "-"*40 + "\n")

# 方法1：使用 str.contains 配合 join（推荐方法）
print("方法1：使用 str.contains 配合 join")
contains_keywords_1 = df['description'].str.contains('|'.join(keywords))
print("包含关键词的行:")
print(contains_keywords_1)
print("对应的产品:")
print(df[contains_keywords_1])
print("\n" + "-"*40 + "\n")

# 方法2：使用 apply 和 any
print("方法2：使用 apply 和 any")
contains_keywords_2 = df['description'].apply(lambda x: any(keyword in x for keyword in keywords))
print("包含关键词的行:")
print(contains_keywords_2)
print("对应的产品:")
print(df[contains_keywords_2])
print("\n" + "-"*40 + "\n")

# 方法3：直接在正则表达式中写多个条件
print("方法3：直接在正则表达式中写多个条件")
contains_keywords_3 = df['description'].str.contains('camera|performance|5G')
print("包含关键词的行:")
print(contains_keywords_3)
print("对应的产品:")
print(df[contains_keywords_3])
print("\n" + "-"*40 + "\n")

# 方法4：不区分大小写
print("方法4：不区分大小写匹配")
contains_keywords_4 = df['description'].str.contains('|'.join(keywords), case=False)
print("包含关键词的行（不区分大小写）:")
print(contains_keywords_4)
print("对应的产品:")
print(df[contains_keywords_4])
print("\n" + "-"*40 + "\n")

# 方法5：统计每个关键词的出现次数
print("方法5：统计每个关键词的出现次数")
for keyword in keywords:
    count = df['description'].str.contains(keyword, case=False).sum()
    print(f"包含 '{keyword}' 的产品数量: {count}")

print("\n" + "-"*40 + "\n")

# 方法6：显示具体包含哪些关键词
print("方法6：显示具体包含哪些关键词")
def find_keywords(text, keywords):
    found = [keyword for keyword in keywords if keyword.lower() in text.lower()]
    return ', '.join(found) if found else 'None'

df['found_keywords'] = df['description'].apply(lambda x: find_keywords(x, keywords))
print("每个产品包含的关键词:")
print(df[['product_name', 'found_keywords']])

print("\n" + "-"*40 + "\n")

# 方法7：处理包含特殊字符的关键词
print("方法7：处理包含特殊字符的关键词")
special_keywords = ['camera', '5G', 'smartphone']
# 使用 re.escape 来转义特殊字符
import re
escaped_keywords = [re.escape(keyword) for keyword in special_keywords]
contains_special = df['description'].str.contains('|'.join(escaped_keywords), case=False)
print("包含特殊关键词的行:")
print(df[contains_special])

print("\n" + "-"*40 + "\n")

# 实际应用示例：筛选特定类型的手机
print("实际应用示例：筛选特定类型的手机")
# 筛选包含相机相关关键词的手机
camera_phones = df[df['description'].str.contains('camera|photography', case=False)]
print("相机功能突出的手机:")
print(camera_phones[['product_name', 'description']])

# 筛选包含性能相关关键词的手机
performance_phones = df[df['description'].str.contains('performance|fast|5G', case=False)]
print("\n性能突出的手机:")
print(performance_phones[['product_name', 'description']]) 