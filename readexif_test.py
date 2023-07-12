import os
import tkinter as tk
from tkinter import filedialog
import exifread
from PIL import Image

selected_files = []  # 全局变量，用于保存当前选择的文件路径列表

def clear_exif(image_path):
    image = Image.open(image_path)
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(list(image.getdata()))

    # 获取原始文件名和扩展名
    filename, extension = os.path.splitext(image_path)

    # 创建保存路径，位于原图片同级目录下的"exif"文件夹中
    output_path = os.path.join(os.path.dirname(image_path), "exif", os.path.basename(filename) + extension)

    # 确保"exif"文件夹存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 保存没有EXIF信息的图像
    image_without_exif.save(output_path)

    return output_path

def read_exif(file_path):
    with open(file_path, 'rb') as image_file:
        tags = exifread.process_file(image_file)
        output_text.insert(tk.END, "EXIF information for file: {}\n".format(file_path))
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                output_text.insert(tk.END, "Tag: {}, Value: {}\n".format(tag, tags[tag]))
        output_text.insert(tk.END, "\n")

def browse_files(event=None):
    global selected_files
    selected_files = filedialog.askopenfilenames(filetypes=(("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp"), ("All Files", "*.*")))
    if selected_files:
        output_text.delete('1.0', tk.END)
        for file in selected_files:
            read_exif(file)  # 读取并显示每个图片的EXIF信息
        clear_button.config(state=tk.NORMAL)  # 启用清除按钮

def clear_exif_button():
    global selected_files
    if selected_files:
        output_text.delete('1.0', tk.END)
        for file in selected_files:
            output_text.insert(tk.END, "Cleared EXIF information from file: {}\n".format(file))
            # 清除EXIF信息并保存图像到"exif"文件夹中
            output_path = clear_exif(file)
            output_text.insert(tk.END, "Cleared image saved at: {}\n".format(output_path))
            output_text.insert(tk.END, "\n")

# 创建主窗口
window = tk.Tk()

# 添加标签
label = tk.Label(window, text="点击选择图片", font=("Helvetica", 16), pady=20)
label.pack()

# 设置拖放区域
drop_zone = tk.Label(window, width=50, height=5, relief="groove")
drop_zone.pack(pady=10)

# 定义拖放事件处理函数
def on_drag_enter(event):
    drop_zone['background'] = "light blue"

def on_drag_leave(event):
    drop_zone['background'] = "white"

# 绑定拖放事件
drop_zone.bind("<Enter>", on_drag_enter)
drop_zone.bind("<Leave>", on_drag_leave)
drop_zone.bind("<Button-1>", browse_files)

# 创建清除按钮
clear_button = tk.Button(window, text="清除", command=clear_exif_button, state=tk.DISABLED)
clear_button.pack(pady=10)

# 创建输出窗口
output_text = tk.Text(window, height=20, width=70)
output_text.pack()

# 启动主循环
window.mainloop()
