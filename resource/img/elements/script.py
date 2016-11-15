import glob
import os

# problem with pngs: Warning: libpng warning: iCCP known incorrect sRGB profile
# http://stackoverflow.com/questions/22745076/libpng-warning-iccp-known-incorrect-srgb-profile

os.chdir(os.getcwd())
for file in glob.glob("*.png"):
    os.system("convert {file} {file}.1".format(file=file))
    os.remove("{file}".format(file=file))
    os.system("mv {file}.1 {file} ".format(file=file))
    print("<file alias=\"{file}\">img/elements/{file}.png</file>".format(file=file.replace(".png", "")))
