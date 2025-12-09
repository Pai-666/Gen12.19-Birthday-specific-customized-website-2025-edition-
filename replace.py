import os

# 你的GitHub仓库Raw链接前缀（必须正确）
prefix = "https://media.githubusercontent.com/media/Pai-666/Gen12.19-Birthday-specific-customized-website-2025-edition-/refs/heads/main/"
# 遍历所有HTML文件
for filename in os.listdir("."):
    if filename.endswith(".html"):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        # 替换图片路径（.jpg .png）
        content = content.replace('src="', f'src="{prefix}')
        # 保存修改
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

print("所有HTML文件的路径已替换完成！")