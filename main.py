from docx2python import docx2python
 
# extract docx content
result = docx2python('document.docx', html=True)

for name, image in result.images.items():
    with open(name, 'wb') as image_destination:
        write(image_destination, image)