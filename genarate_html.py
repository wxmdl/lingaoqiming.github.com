import markdown as md
import os
root = './_posts/'
chapter_name = ['前言','第一章','第二章','第三章','第三章','第四章','第五章','第六章','第七章']

prefix = '''<!DOCTYPE html>\n
<html>\n
<head>\n
<meta charset="utf-8">\n
<title>临高启明</title>\n
<meta name="author" content="吹牛者">\n
</head>\n
<body>\n'''
toc = '''<dl>'''
for file_name in os.listdir(root):
    chapter_idx = int(file_name.split('.')[0].split('_')[-2])
    section_idx = int(file_name.split('.')[0].split('_')[-1])//100
    if section_idx == 1:
        toc = toc + u'<dt id="tocc{:d}"> <a href="#c{:d}">{}</a> </dt>\n'.format(chapter_idx,chapter_idx,chapter_name[chapter_idx])
    with open(root+file_name,'r',encoding='UTF-8') as file:
        print(chapter_idx,section_idx)
        text = file.read()
        title = text.split('\n')[2].split(':')[1].split('\n')[0]
        toc = toc + u'<dd id="tocc{:d}s{:d}"> <a href="#c{:d}s{:d}">{}</a> </dd>\n'.format(chapter_idx,section_idx,chapter_idx,section_idx,title)
toc += u'''</dl>'''
body = ''''''
for file_name in os.listdir(root):
    chapter_idx = int(file_name.split('.')[0].split('_')[-2])
    section_idx = int(file_name.split('.')[0].split('_')[-1])//100
    if section_idx == 1:
        body = body + u'<h1 id="c{:d}"><a href="#tocc{:d}">{}</a></h2>\n'.format(chapter_idx,chapter_idx,chapter_name[chapter_idx])
    with open(root+file_name,'r',encoding='UTF-8') as file:
        print(chapter_idx,section_idx)
        text = file.read()
        title = text.split('\n')[2].split(':')[1].split('\n')[0]
        # # 前7行都是标签之类的东西
        # print
        cnt = 0 
        idx = 0
        for c in text:
            if cnt == 10:
                break
            idx += 1
            if c == '-':
                cnt+=1
        # TODO: 去掉人名等中的超链接，因为没有意义。
        body = body + u'<h2 id="c{:d}s{:d}"><a href="#tocc{:d}s{:d}">{}</a></h2>\n'.format(chapter_idx,section_idx,chapter_idx,section_idx,title)
        body = body + md.markdown(text[idx:])
body+='''\n</body>\n</html>'''
print(prefix+toc+body,file=open('./test.html','w',encoding='UTF-8'))
        # exit()
        # 加入正文
        # html = md.markdown(file.read())
        # print(html,file=open('./test.html','w'))