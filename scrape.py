import re

def extract_content(xml_string):
    # 定义正则表达式模式，确保匹配到具体层级
    title_pattern = re.compile(r'<item>.*?<title><!\[CDATA\[(.*?)\]\]></title>.*?</item>', re.DOTALL)
    url_pattern = re.compile(r'<item>.*?<url><!\[CDATA\[(.*?)\]\]></url>.*?</item>', re.DOTALL)
    pub_time_pattern = re.compile(r'<item>.*?<pub_time>(.*?)</pub_time>.*?</item>', re.DOTALL)
    username_pattern = re.compile(r'<publisher>.*?<username><!\[CDATA\[(.*?)\]\]></username>.*?</publisher>', re.DOTALL)
    nickname_pattern = re.compile(r'<publisher>.*?<nickname><!\[CDATA\[(.*?)\]\]></nickname>.*?</publisher>', re.DOTALL)

    # 使用正则表达式查找内容
    titles = title_pattern.findall(xml_string)
    urls = url_pattern.findall(xml_string)
    pub_times = pub_time_pattern.findall(xml_string)  # UNIX时间戳
    usernames = username_pattern.findall(xml_string)
    nicknames = nickname_pattern.findall(xml_string)

    # 去除链接中的多余参数
    cleaned_urls = []
    for url in urls:
        cleaned_url = re.sub(r'&chksm=.*', '', url)
        cleaned_urls.append(cleaned_url)

    # 打印提取的内容
    for i in range(len(titles)):
        print(f"标题: {titles[i]}")
        print(f"链接: {cleaned_urls[i]}")
        print(f"发布时间: {pub_times[i]}")
        print(f"公众号ID: {usernames[0] if usernames else 'N/A'}")
        print(f"公众号名称: {nicknames[0] if nicknames else 'N/A'}")
        print()

# 读取XML文件内容
with open('example.xml', 'r', encoding='utf-8') as file:
    xml_content = file.read()

extract_content(xml_content)
