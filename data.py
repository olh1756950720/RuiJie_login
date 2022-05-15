
# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def write_data(name, msg, conf):
    desktop_path = "D:\\"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + ".txt"  # 也可以创建一个.doc的word文档
    file = open(full_path, conf, encoding="utf-8")
    file.write(msg)  # msg也就是下面的Hello world!
    file.close()

def read_date(name):
    desktop_path = "D:\\"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + ".txt"  # 也可以创建一个.doc的word文档
    file = open(full_path, 'r', encoding="utf-8")
    data = file.readlines()
    file.close()
    return data

if __name__ == '__main__':
    pass
    # text_create('文件', 'Hello world!')
    # 调用函数创建一个名为mytxtfile的.txt文件，并向其写入Hello world!
