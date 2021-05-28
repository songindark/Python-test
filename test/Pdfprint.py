import os
import tempfile
import time
import win32api
import win32print

def print_file(filename):
    file = open(filename,"r")
    # with open(filename, 'r') as file:
    win32api.ShellExecute
    (
        0,
        "print",
        filename,
        # file,
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
    file.close() 
    print("打印文件%s"%filename)
    return


#     def print_pdf(self, pdf_file_name):
#         """
#         静默打印pdf
#         :param pdf_file_name:
#         :return:
#         """
#         GSPRINT_PATH = 'gsprint'
#         GHOSTSCRIPT_PATH = 'gswin32c'
#         currentprinter = win32print.GetDefaultPrinter()

# win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "PDFFile.pdf"', '.', 0)


# def print_pdf(pdf_file_name, page):
#     """
#         静默打印pdf
#         :param pdf_file_name
#         :page  打印第几页
#         :return:
#         """
#     cmd = 'gsprint -dFirstPage=%s -dLastPage=%s %s' % (page, page, pdf_file_name)
#     print(cmd)
#     p = os.popen(cmd)
#     time.sleep(3)
#     print(p.read())


# if __name__ == '__main__':
#     # curr_path = os.getcwd()
#     curr_path = "D:\PDF"
#     fl = os.listdir(curr_path)
#     # for i in range(2,4):
#     #     print(i)
#     for f in fl:
#         if 'pdf' in f.lower():
#             print_pdf(f, 1)
#         # a = raw_input('请翻转打印纸')


if __name__ == '__main__':
    curr_path = "D:\打印"
    fl = os.listdir(curr_path)

    for f in fl:
        # if 'pdf' in f.lower():
        if os.path.splitext(f.lower())[1]==".pdf":
            file_path = os.path.join(curr_path,f)
            print_file(file_path)