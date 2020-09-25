import zipfile

f = open('fileone.txt', 'w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt', 'w+')
f.write('TWO FILE')
f.close()


comp_file = zipfile.ZipFile('comp_file.zip', 'w')

comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_object = zipfile.ZipFile('comp_file.zip', 'r')
zip_object.extractall('extracted_content')
