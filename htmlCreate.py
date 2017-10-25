import os


if __name__ == "__main__" :
    dirPath = os.getcwd()
    fileName = input('Key in the fileName:')
    file = '%s%s%s%s' % (dirPath, os.sep, fileName, '.html')
    print(file)
    f = open(file, mode='w', newline='\n')
    dataStr = '<!doctype html>\n' \
              '<html>\n' \
              '\t<head>\n' \
              '\t\t<meta charset=\"utf-8\">\n' \
              '\t\t<title></title>\n' \
              '\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n' \
              '\t\t<link rel=\"stylesheet\" href=\"../../../assets/css/main.css\" />\n' \
              '\t\t<link rel=\"stylesheet\" href=\"../../../assets/css/marxico.css\" />\n' \
              '\t</head>\n' \
              '\n' \
              '\t<body>\n' \
              '\t\t<div id=\"page-wrapper\">\n' \
              '\t\t\t<!-- Header -->\n' \
              '\t\t\t<header id=\"header\">\n' \
              '\t\t\t\t<h1><a href=\"../../../index.html\">Yepoch Blog</a></h1>\n' \
              '\t\t\t\t<nav><a href=\"#menu\">目录</a></nav>\n' \
              '\t\t\t</header>\n' \
              '\n' \
              '\t\t\t<!-- Wrapper -->\n' \
              '\t\t\t<section id=\"wrapper\">\n' \
              '\t\t\t\t<header>\n' \
              '\t\t\t\t\t<div class=\"inner\">\n' \
              '\t\t\t\t\t\t<h2></h2>\n' \
              '\t\t\t\t\t\t<p></p>\n' \
              '\t\t\t\t\t</div>\n' \
              '\t\t\t\t</header>\n' \
              '\n' \
              '\t\t\t\t<div class=\"wrapper\"><div class=\"inner\">\n' \
              '\n' \
              '\t\t\t\t</div></div>\n' \
              '\t\t\t</section>\n' \
              '\n' \
              '\t\t\t<section id=\"footer\"><div class=\"inner\">\n' \
              '\t\t\t\t<ul class=\"copyright\"><li>&copy; Yepoch Inc. All rights reserved.</li></ul>\n' \
              '\t\t\t</div></section>\n' \
              '\t\t</div>\n' \
              '\n' \
              '\t\t<script src=\"../../../assets/js/skel.min.js\"></script>\n' \
              '\t\t<script src=\"../../../assets/js/jquery.min.js\"></script>\n' \
              '\t\t<script src=\"../../../assets/js/util.js\"></script>\n' \
              '\t\t<script src=\"../../../assets/js/main.js\"></script>\n' \
              '\t</body>\n' \
              '</html>\n'
    f.writelines(dataStr)
    f.close()
