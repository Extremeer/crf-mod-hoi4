import re

# 读取文件内容
with open("china_nationalist.txt", "r", encoding="utf-8") as file:
    content = file.read()

# 使用正则表达式提取id和cost
focuses = re.findall(r'focus\s*=\s*{\s*id\s*=\s*([\w_]+)[\s\S]*?cost\s*=\s*(\d+)?', content)

# 打印结果
print("| id                          | cost |")
print("|-----------------------------|------|")
for focus in focuses:
    id = focus[0]
    cost = focus[1] if focus[1] else "未定义"
    print(f"| {id:<28} | {cost:<4} |")