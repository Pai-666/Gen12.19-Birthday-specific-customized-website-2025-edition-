import os

# 你的GitHub仓库Raw链接前缀（替换为你实际的前缀）
GITHUB_PREFIX = "https://media.githubusercontent.com/media/Pai-666/Gen12.19-Birthday-specific-customized-website-2025-edition-/refs/heads/main/"

# 扫描文件夹中所有图片和音乐文件
def get_all_resources():
    resources = {"img": [], "audio": []}
    for file in os.listdir("."):
        if file.lower().endswith((".jpg", ".png")):
            resources["img"].append(file)
        elif file.lower().endswith(".mp3"):
            resources["audio"].append(file)
    return resources

# 全量替换HTML中的资源路径
def replace_all_paths():
    resources = get_all_resources()
    # 遍历所有HTML文件
    for html_file in os.listdir("."):
        if not html_file.endswith(".html"):
            continue
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 替换所有图片路径
        for img in resources["img"]:
            # 匹配所有包含该图片名的src（忽略旧路径）
            content = content.replace(f'src="{img}"', f'src="{GITHUB_PREFIX}{img}"')
            content = content.replace(f'data-src="{img}"', f'data-src="{GITHUB_PREFIX}{img}"')
        
        # 替换所有音乐路径
        for audio in resources["audio"]:
            content = content.replace(f'src="{audio}"', f'src="{GITHUB_PREFIX}{audio}"')
            content = content.replace(f'source src="{audio}"', f'source src="{GITHUB_PREFIX}{audio}"')
        
        # 保存修改
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(content)
    print("全量资源路径替换完成！所有图片/音乐已统一配置为GitHub链接")

if __name__ == "__main__":
    replace_all_paths()