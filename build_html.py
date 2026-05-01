
html = open('index.html', 'r', encoding='utf-8').read()
print(f"Current: {len(html)} bytes, {html.count(chr(10))} lines")
