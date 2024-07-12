import re

with open('generated_code.py', "r", encoding="utf-8") as f:
    a = f.read()

all_info = []

# 使用正则表达式匹配 entries 列表
for es in ['entries', 'comboboxes', 'labels', 'buttons']:
    entries_pattern = re.compile(fr"{es}\s*=\s*\[([^\]]+)\]", re.DOTALL)
    matches = entries_pattern.search(a)

    if matches:
        entries_string = matches.group(1).strip()
        # 解析 entries 字符串为 Python 对象
        entries = eval(f"[{entries_string}]")
        print(entries)
        for e in entries:
            if es == 'entries':
                type = "Entry"
            elif es == 'comboboxes':
                type = 'Combobox'
            elif es == 'labels':
                type = 'Label'
            elif es == 'button':
                type = 'Button'

            a_dict = {
                "type": type,
                "position": [e[2], e[3]],
                "size": [e[4], e[5]],
                "current_value": e[1],
                "values": []
                }
            all_info.append(a_dict)

    else:
        print("No entries found")

print(all_info)