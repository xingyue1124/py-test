'''
    yaml是一种文件格式
    可以定义list和dict不同的格式
'''
import yaml

file = open('para.yaml', 'r', encoding='utf-8')
# 解析yaml格式的文件
value = yaml.load(stream=file, Loader=yaml.FullLoader)
print(value)
print(value[0]['name'])
print(type(value))
file.close()

