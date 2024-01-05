import os


def file_11():  # 加函数在其他文件直接调用file_11函数就可以
    path = os.path.dirname(
        os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "file",
                     "logo.png"))  # 按下边的解释来先找到当前文件位置然后上一级上一级找到上传文件路径
    return path


if __name__ == '__main__':
    print(os.path.relpath(__file__))
    print(os.path.dirname(os.path.realpath(__file__)))  # 定位到上一层
    print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))  # 定位到上一层
    print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))  # 定位到项目
    print(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "file", "logo.png"))  # 定位到文件的路径
    print(file_11())
