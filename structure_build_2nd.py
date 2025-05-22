import os

def generate_file_structure(root_dir, output_file):
    def traverse_directory(current_dir):
        structure = ""
        # 获取当前目录下的所有文件和文件夹
        entries = os.listdir(current_dir)
        entries.sort()  # 确保文件按顺序排列
        for entry in entries:
            full_path = os.path.join(current_dir, entry)
            if os.path.isdir(full_path):
                structure += "├── " + entry + "/\n"
                # 获取当前子文件夹下的文件和文件夹
                sub_entries = os.listdir(full_path)
                sub_entries.sort()
                for sub_entry in sub_entries:
                    sub_full_path = os.path.join(full_path, sub_entry)
                    if os.path.isdir(sub_full_path):
                        structure += "│   ├── " + sub_entry + "/\n"
                    else:
                        structure += "│   ├── " + sub_entry + "\n"
            else:
                structure += "├── " + entry + "\n"
        return structure

    # 获取文件夹结构
    structure = traverse_directory(root_dir)

    # 将结构写入指定文件，显式指定UTF-8编码
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(root_dir.split(os.sep)[-1] + "/\n")  # 添加根文件夹名
        f.write(structure)

# 获取当前目录
current_directory = os.getcwd()
output_txt_file = "file_structure.txt"

# 生成并保存文件夹结构
generate_file_structure(current_directory, output_txt_file)

