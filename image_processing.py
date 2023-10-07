import cv2
import numpy as np
from imutils import contours
import pytesseract
import copy
from solver import solve_to_sudoku


def solve(path):
    src = cv2.imread(path)

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    gray = cv2.bitwise_not(gray)
    bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)

    horizontal = np.copy(bw)
    vertical = np.copy(bw)

    cols = horizontal.shape[1]
    horizontal_size = cols // 10
    horizontalStructre = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
    horizontal = cv2.erode(horizontal, horizontalStructre)
    horizontal = cv2.dilate(horizontal, horizontalStructre)

    rows = vertical.shape[0]
    vertical_size = rows // 10
    verticalStructre = cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_size))
    vertical = cv2.erode(vertical, verticalStructre)
    vertical = cv2.dilate(vertical, verticalStructre)

    new_image = cv2.bitwise_or(vertical, horizontal)

    new_im = cv2.bitwise_not(new_image)

    edges = cv2.adaptiveThreshold(new_im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, -2)

    kernel = np.ones((2, 2), np.uint8)
    edges = cv2.dilate(edges, kernel)

    smooth = cv2.blur(edges, (2, 2))

    cnts, hierarchy = cv2.findContours(image=smooth, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    cp = src.copy()
    cv2.drawContours(image=cp, contours=cnts, contourIdx=-1, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

    cnts, _ = contours.sort_contours(cnts, method="left-to-right")
    cnts, _ = contours.sort_contours(cnts, method="top-to-bottom")

    def get_num(img):
        return pytesseract.image_to_string(img, config=r'--oem 1 --psm 13 outputbase digits')

    cp = src.copy()
    count = 0
    num = []
    for c in cnts:
        if 1000 < cv2.contourArea(c) < 5000:
            count += 1
            rect = cv2.boundingRect(c)
            x, y, w, h = rect
            array = np.array(cp[y:y + h, x:x + w])
            num.append(get_num(array))

    def divide_chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i: i + n]

    n = 9
    matrix = list(divide_chunks(num, n))

    mat = copy.deepcopy(matrix)
    for n in mat:
        for j, i in enumerate(n):
            if i == "":
                n[j] = i.replace("", "0")
            else:
                n[j] = i.replace(i, i[0])

    for row in mat:
        for j, i in enumerate(row):
            row[j] = int(i)

    grid = copy.deepcopy(mat)

    grid = solve_to_sudoku(grid)

    bound = []
    count = 0
    for c in cnts:
        if 1000 < cv2.contourArea(c) < 5000:
            count += 1
            rect = cv2.boundingRect(c)
            bound.append(rect)

    n = 9
    bound = list(divide_chunks(bound, n))

    cp = src.copy()
    for i, m in enumerate(mat):
        for j, n in enumerate(m):
            if mat[i][j] != grid[i][j]:
                x, y, w, h = bound[i][j]
                cv2.putText(cp, str(grid[i][j]), (x + w - 40, y + h - 20), 0, 0.9, (0, 0, 255))

    cv2.imwrite("example.png", cp)
