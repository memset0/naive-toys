import sys
from os import path


def readFile(dir):
    realdir = path.abspath(path.join(path.dirname(__file__), dir))
    with open(realdir, 'r+', encoding='utf-8') as file:
        return file.read()


def writeFile(dir, content):
    realdir = path.abspath(path.join(path.dirname(__file__), dir))
    with open(realdir, 'w+', encoding='utf-8') as file:
        file.write(content)


source = readFile('source.py').splitlines()
blank = readFile('blank.py').splitlines()
filename = '' if len(sys.argv) < 2 else sys.argv[1]
assert len(source) == len(blank)

svg = '<svg t="1634369767437" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1540" width="200" height="200"><path d="M522.666667 492.885333h85.333333a57.6 57.6 0 0 0 57.6-57.6v-192a57.6 57.6 0 0 0-57.6-57.6h-192a57.6 57.6 0 0 0-57.6 57.6v74.666667h132.266667v42.666667h-213.333334a64 64 0 0 0-64 64v170.666666a64 64 0 0 0 64 64v42.666667a106.666667 106.666667 0 0 1-106.666666-106.666667v-170.666666a106.666667 106.666667 0 0 1 106.666666-106.666667h42.666667v-74.666667a96 96 0 0 1 96-96h192a96 96 0 0 1 96 96v192a96 96 0 0 1-96 96h-106.666667v-0.170666h-85.333333a57.6 57.6 0 0 0-57.6 57.6v192c0 31.829333 25.770667 57.6 57.6 57.6h192a57.6 57.6 0 0 0 57.6-57.6v-78.762667h-132.266667v-42.666667h213.333334a64 64 0 0 0 64-64v-170.666666a64 64 0 0 0-64-64v-42.666667a106.666667 106.666667 0 0 1 106.666666 106.666667v170.666666a106.666667 106.666667 0 0 1-106.666666 106.666667h-42.666667v78.762667a96 96 0 0 1-96 96h-192a96 96 0 0 1-96-96v-192a96 96 0 0 1 96-96h106.666667v0.170666zM426.666667 275.285333a21.333333 21.333333 0 1 1 0-42.666666 21.333333 21.333333 0 0 1 0 42.666666z m170.666666 512a21.333333 21.333333 0 1 1 0-42.666666 21.333333 21.333333 0 0 1 0 42.666666z" p-id="1541" fill="#000000"></path></svg>'
html = '''<style>
*{font-family:consolas,"Microsoft Yahei Light"}
body{font-size:15px;line-height:1.5em}
.hide{display:none}
.icon{height:1.4em;width:1.4em;margin:.05em .1em .05em 0}
.file{position:relative;width:fit-content;padding:.2em 1.35em;margin-bottom:-1em;display:inline-flex;align-self:center}
.file:before{content:'';position:absolute;top:0;right:0;left:0;bottom:0;z-index:-1;border:2px solid #ccc;border-bottom:none;border-radius:.5em .5em 0 0;transform:scaleY(1.3) perspective(.5em) rotateX(5deg);transform-origin:bottom}
.code{border:2px solid #ccc}
.line-number{color:#666;border-right:2px solid #ccc;padding-right:12px;margin-right:12px;line-height:1.5em;height:1.5em;display:inline-block}
.blank{border-bottom:1.2px solid #000;box-sizing:border-box}
.placer{max-height:.5em;display:block;overflow:hidden}
@media print {.page-breaker{page-break-after:always}}
</style>'''

if filename:
    html += '<pre class="file">' + svg + '<code>' + filename + '</code></pre>'
html += '<pre class="code main" id="main"><code><span class="placer"><span class="line-number">    </span>\n</span>'
cnt = 0
answer = []
for i in range(len(source)):
    html += '<span class="line-number">' + ('%4d' % i) + '</span>'
    if source[i] == blank[i]:
        html += source[i] + '\n'
        continue
    source[i] += '\0'
    blank[i] += '\0'
    pattern = blank[i].split('{{}}')
    p = 0
    for j in range(len(pattern)):
        u = source[i].find(pattern[j], p)
        if u > 0:
            cnt += 1
            html += '<span class="blank">' + str(
                cnt) + '.' + ' ' * 10 + '</span>'
            answer.append(source[i][p:u])
        p = u + len(pattern[j])
        html += pattern[j]
        print(u, p, pattern[j])
    html += '\n'
html += '<span class="placer"><span class="line-number">    </span>\n</span></code></pre>'
html += '<div class="page-breaker"></div>'
html += '<pre class="file"><code>answer</code></pre>'
html += '<pre class="code answer" id="answer"><code><span class="placer"><span class="line-number">    </span>\n</span>'
for i in range(cnt):
    html += '<span class="line-number">' + ('%4d' % i) + '</span>'
    html += answer[i] + '\n'
html += '<span class="placer"><span class="line-number">    </span>\n</span></code></pre>'
html += '<pre class="hide source" id="source"><code>\n'
html += readFile('source.py')
html += '\n</code></pre>'
html += '<pre class="hide blank" id="blank"><code>\n'
html += readFile('blank.py')
html += '\n</code></pre>'
writeFile('result.html', html)
print(answer)