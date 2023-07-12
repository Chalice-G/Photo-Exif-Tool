<h2 align = center padding = 20px> Photo Exif Tool</h2>
<p align = center> A simple tool with GUI written in Python to make it available for you to read Exif of photos and delete the Exif data</p>

---

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme) ![Static Badge](https://img.shields.io/badge/python-3.x-brightgreen)


### Features

---

- Select multiple images at once and read the information
- Support common image formats
- Delete the Exif information of the imported images and save them as a new images.

### Install

---

1. Install Python from official website https://www.python.org/

2. Install tkinter library in CMD

   ```
   pip install tkinterdnd2
   ```

3. Install exifread library in CMD

   ```
   pip install exifread
   ```

4. Install pyinstaller

   ```
   pip install pyinstaller
   ```

5. Open CMD, navigate to the location where you saved readexif.py using the cd command. Run the command. This will create a folder named dist containing an executable file. The folder is in the location where you saved your readexif.py.

   ```
   pyinstaller --onefile readexif.py
   ```



### Usage

---

1. If you have successfully generated an execuable file, double-click the file and you will see the interface. 

<div align = center>

<img src="https://img1.imgtp.com/2023/07/12/cTGMjwED.png" alt="image-20230712111325497" align = center style="zoom:80%;" />

</div>

2. Click on the first selection box in the window, select the image you want and the programme will read and output the exif information in the next window. You can select more than one image at the same time, which will be read and output sequentially.

<div align = center>
   
<img src="https://img1.imgtp.com/2023/07/12/MWJcataZ.png" alt="image-20230712111503076" align = center style="zoom:80%;" />

</div>

3. There is a clickable button, when you click on it, the program will clear the exif information of the picture you selected and save it in a folder with the same name as the original file in a folder with the same level as the original file directory, the folder name is exif.

### Maintainers

---

[<img src="https://avatars.githubusercontent.com/u/68186151?v=4" style="zoom:25%;" />](https://github.com/Chalice-G)

### Contributing

---

Any contributions you make are greatly appreciated.

If you find any issues, you can simply open an [issue](https://github.com/Chalice-G/Photo-Exif-Tool/issues) with the tag enhancement. You can also fork the project, modify yourself and submit Pull requests.

### License

---

[MIT](https://github.com/RichardLitt/standard-readme/blob/main/LICENSE) © Chalice-G

