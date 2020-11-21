# Document Scanner

### An interactive document scanner built in Python using OpenCV

The scanner takes a poorly scanned image, finds the corners of the document, applies the perspective transformation to get a top-down view of the document, sharpens the image, and applies an adaptive color threshold to clean up the image.

On my test dataset of 300 images, the program correctly detected the corners of the document 92.8% of the time.

* The scanner can process an entire directory of images automatically and save the output in an output directory:

#### Here are some examples of images before and after scan:

<img src="https://github.com/endalk200/document-scanner/blob/master/sample_images/cell_pic.jpg" height="450"> <img src="https://github.com/endalk200/doc_scanner/blob/master/output/cell_pic.jpg" height="450">

<img src="https://github.com/endalk200/document-scanner/blob/master/sample_images/receipt.jpg" height="450"> <img src="https://github.com/endalk200/document-scanner/blob/master/output/receipt.jpg" height="450">

<img src="https://github.com/endalk200/document-scanner/blob/master/sample_images/math_cheat_sheet.JPG" height="450"> <img src="https://github.com/endalk200/document-scanner/blob/master/output/math_cheat_sheet.JPG" height="450">

<img src="https://github.com/endalk200/document-scanner/blob/master/sample_images/dollar_bill.JPG" width="350"> <img src="https://github.com/endalk200/document-scanner/blob/master/output/dollar_bill.JPG" width="350">


### Usage

You can use this script by downloading it from pypi
```bash
pip install document-scanner
```

aftter installing it from pypi index, you can use it from the terminal as follows.

```
python scan.py (--images <IMG_DIR> | --image <IMG_PATH>) [-i]
```
* The `-i` flag enables interactive mode, where you will be prompted to click and drag the corners of the document. For example, to scan a single image with interactive mode enabled:
```
python scan.py --image sample_images/desk.JPG -i
```
* Alternatively, to scan all images in a directory without any input:
```
python scan.py --images sample_images
```