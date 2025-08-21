import pandas as pd
import numpy as np

# 创建示例数据
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'email': ['alice@email.com', 'bob@work.com', 'charlie@gmail.com', 
              'david@company.org', 'eve@personal.net', 'frank@business.com'],
    'description': ['Software Engineer', 'Data Scientist', 'Product Manager',
                   'Marketing Specialist', 'UX Designer', 'Business Analyst']
}

df = pd.DataFrame(data)
print("原始数据:")
print(df)
print("\n" + "="*50 + "\n")

# 1. 基本字符串匹配
print("1. 基本字符串匹配:")
# 查找名字中包含 'a' 的行
contains_a = df['name'].str.contains('a')
print("名字中包含 'a' 的行:")
print(contains_a)
print("对应的数据:")
print(df[contains_a])
print("\n" + "-"*30 + "\n")

# 2. 不区分大小写
print("2. 不区分大小写匹配:")
# 查找名字中包含 'A' 或 'a' 的行（不区分大小写）
contains_a_ignore_case = df['name'].str.contains('a', case=False)
print("名字中包含 'a' 或 'A' 的行（不区分大小写）:")
print(contains_a_ignore_case)
print("对应的数据:")
print(df[contains_a_ignore_case])
print("\n" + "-"*30 + "\n")

# 3. 正则表达式匹配
print("3. 正则表达式匹配:")
# 查找邮箱以 'gmail.com' 结尾的行
gmail_users = df['email'].str.contains(r'gmail\.com$')
print("使用 Gmail 的用户:")
print(gmail_users)
print("对应的数据:")
print(df[gmail_users])
print("\n" + "-"*30 + "\n")

# 4. 多个条件组合
print("4. 多个条件组合:")
# 查找描述中包含 'Engineer' 或 'Scientist' 的行
tech_roles = df['description'].str.contains('Engineer|Scientist')
print("技术岗位（Engineer 或 Scientist）:")
print(tech_roles)
print("对应的数据:")
print(df[tech_roles])
print("\n" + "-"*30 + "\n")

# 5. 处理缺失值
print("5. 处理缺失值:")
# 添加一些缺失值
df_with_na = df.copy()
df_with_na.loc[2, 'name'] = np.nan
df_with_na.loc[4, 'description'] = np.nan

print("包含缺失值的数据:")
print(df_with_na)
print("\n默认处理（缺失值返回 NaN）:")
print(df_with_na['name'].str.contains('a'))
print("\n将缺失值处理为 False:")
print(df_with_na['name'].str.contains('a', na=False))
print("\n" + "-"*30 + "\n")

# 6. 实际应用场景
print("6. 实际应用场景:")
# 筛选特定域名的邮箱
work_emails = df['email'].str.contains(r'@(work|company|business)\.')
print("工作邮箱（包含 work、company 或 business 域名）:")
print(work_emails)
print("对应的数据:")
print(df[work_emails])

# 统计包含特定关键词的数量
engineer_count = df['description'].str.contains('Engineer').sum()
print(f"\n工程师数量: {engineer_count}")

# 查找包含多个关键词的描述
multi_keywords = df['description'].str.contains('Engineer|Scientist|Analyst')
print(f"\n技术相关岗位数量: {multi_keywords.sum()}") 