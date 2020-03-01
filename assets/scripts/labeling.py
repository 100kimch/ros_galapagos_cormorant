import sys
import os
import timeit
import cv2
import numpy as np
import copy
import matplotlib.pyplot as plt
import pandas as pd
from pyzbar import pyzbar

start = timeit.default_timer()

path_images = os.getcwd() + "/assets/images/"
path_csv = "/Users/KJH/OneDrive - konkuk.ac.kr/git/ros_galapagos_cormorant/assets/data/test.csv"

name_aperture = {
    "1r2": "f/1.4",
    "2": "f/2",
    "2r2": "f/2.8",
    "4": "f/4",
    "4r2": "f/5.6",
    "8": "f/8",
    "8r2": "f/11",
    "16": "f/16",
}
infos = []


def get_file_names(dirname):
    filenames = os.listdir(dirname)
    return filenames


def compress_img(img):
    return cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)


def labeling(selected=None, expected_score=5):
    p_img = path_images

    if selected:
        num_files = len(selected)
        print("{:d} files selected.".format(num_files))
    else:
        num_files = 0
        for k in ["5-codes/", "3-codes/"]:
            for i in get_file_names(p_img + k):
                if len(i.split("-")) == 2:
                    for j in get_file_names(p_img + k + i + "/labeled"):
                        if j.split(".")[1] in ["png", "jpg", "jpeg"]:
                            num_files += 1

        print("{:d} files detected.".format(num_files))

    try:
        num_progress = -1
        num_selected_progress = -1
        for k in ["5-codes/", "3-codes/"]:
            for i in get_file_names(p_img + k):
                if len(i.split("-")) == 2:
                    aperture, focal_length = i.split("-")
                    info = {
                        "aperture": name_aperture[aperture],
                        "focal_length": focal_length,
                    }
                    for j in get_file_names(p_img + k + i + "/labeled"):
                        if not (j.split(".")[1] in ["png", "jpg", "jpeg"]):
                            continue
                        num_progress += 1

                        if selected:
                            if not num_progress in selected:
                                continue
                            num_selected_progress += 1
                            percentage = int(
                                (num_selected_progress / num_files) * 20 + 1
                            )
                            print(
                                "Executing {:30s} [{:20s}] ({:d}/{:d})".format(
                                    i + "/labeled/" + j,
                                    "#" * percentage,
                                    num_selected_progress,
                                    num_files,
                                ),
                                end="",
                            )
                        else:
                            percentage = int((num_progress / num_files) * 20 + 1)
                            print(
                                "Executing {:30s} [{:20s}] ({:d}/{:d})".format(
                                    i + "/labeled/" + j,
                                    "#" * percentage,
                                    num_progress,
                                    num_files,
                                ),
                                end="",
                            )

                        info["path"] = p_img + k + i + "/labeled/" + j

                        try:
                            img = cv2.imread(info["path"])
                            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        except Exception as e:
                            print()
                            print("Error occured.")
                            print(i.split("-"))
                            print(info)
                            print(e)

                        img_compressed = compress_img(img)
                        img_equalized = cv2.equalizeHist(img)
                        # img_compressed_hist = cv2.resize(
                        #     img_hist, dsize=(640, 480), interpolation=cv2.INTER_AREA
                        # )

                        thresh, img_bin = cv2.threshold(
                            img_equalized, 60, 255, cv2.THRESH_BINARY
                        )
                        info["qr_data"] = []
                        info["qr_rect"] = []
                        barcodes = pyzbar.decode(img_bin)
                        info["qr_score"] = (len(barcodes) / int(k[0])) * 5
                        info["is_optimal"] = info["qr_score"] == expected_score
                        for barcode in barcodes:
                            if len(barcode.data.decode("utf-8")) == 0:
                                continue
                            info["qr_data"].append(
                                int(barcode.data.decode("utf-8").split("cm")[0][-1])
                            )
                            info["qr_rect"].append(
                                [
                                    barcode.rect[0],
                                    barcode.rect[1],
                                    barcode.rect[2],
                                    barcode.rect[3],
                                ]
                            )

                        mean, stddev = cv2.meanStdDev(img_compressed)
                        info["mean_cmp"], info["stddev_cmp"] = mean[0][0], stddev[0][0]
                        mean, stddev = cv2.meanStdDev(img_equalized)
                        info["mean_eq"], info["stddev_eq"] = mean[0][0], stddev[0][0]

                        if selected:
                            print(
                                "  with {:d} barcodes".format(len(barcodes)), end="\r"
                            )
                            cv2.imshow("img0", img_compressed)
                            cv2.imshow("img1", compress_img(img_equalized))
                            cv2.imshow("img2", compress_img(img_bin))
                            cv2.waitKey(0)

                        info["path"] = i + "/labeled/" + j
                        info["distance"], info["env"] = j.split(".")[0].split("-")

                        infos.append(info.copy())

                        print(end="\r")
                        continue
    except Exception as e:
        print()
        print("Error occurred: ", e, " at {:d}".format(num_progress))
        print(sys.exc_info().value.strerror)
        print(info)
        if barcode:
            print(barcode.data.decode("utf-8"))

    print("Labeling of {:d} files finished.        ".format(len(infos)))

    dataframe = pd.DataFrame(infos)
    dataframe = dataframe[
        [
            "is_optimal",
            "path",
            "aperture",
            "focal_length",
            "distance",
            "env",
            "mean_cmp",
            "stddev_cmp",
            "mean_eq",
            "stddev_eq",
            "qr_score",
            "qr_data",
            "qr_rect",
        ]
    ]
    # dataframe.to_csv(
    #     path_csv, header=True, index=True,
    # )

    # print("CSV saved to {:s}".format(path_csv))


try:
    labeling([582, 84, 1160, 1577])
    # labeling([200, 1073])
    # labeling()
except KeyboardInterrupt as e:
    print("Crawler halted", e)

print("Crawler finished at ", end="")
print(timeit.default_timer() - start)
# labeling([85, 90, 95, 105, 110, 195, 200, 210, 220])
# labeling([ 29, 31, 36, 42, 43, 51, 52, 53, 60, 65, 85, 86, 87, 88, 89, 90, 91, 93, 94, 96, 98, 99, 100, 101, 102, 103, 104, 105, 108, 109, 110, 111, 194, 195, 196, 197, 198, 199, 200, 202, 203, 205, 206, 208, 209, 210, 211, 213, 215, 216, 217, 218, 219, 220, 279, 281, 282, 283, 284, 285, 287, 288, 292, 293, 294, 295, 296, 297, 300, 303, 304, 305, 307, 308, 310, 311, 312, 313, 316, 317, 321, 322, 323, 324, 325, 329, 332, 333])

# for i in [6, 101, 156]:
#     # for i in [6, 101, 156, 202, 256, 306, 356, 406]:
#     img = cv2.imread(infos[i]["path"])
#     # bgr_planes = cv2.split(img)
#     # print(bgr_planes)
#     # histSize = 256
#     # histRange = (0, 256)
#     # accumulate = False

#     # b_hist = cv2.calcHist(
#     #     bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate
#     # )
#     # g_hist = cv2.calcHist(
#     #     bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate
#     # )
#     # r_hist = cv2.calcHist(
#     #     bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate
#     # )

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     gray_hist = cv2.equalizeHist(gray)

#     gray = cv2.resize(gray, dsize=(640, 480), interpolation=cv2.INTER_AREA)
#     gray_hist = cv2.resize(gray_hist, dsize=(640, 480), interpolation=cv2.INTER_AREA)

#     print(cv2.meanStdDev(gray))

#     cv2.imshow("img_gray", gray)
#     cv2.imshow("img_gray_hist", gray_hist)
#     plt.hist(gray.ravel(), 256, [0, 256])
#     plt.show()

# # vals = np.random.normal(0, 1, 100)
# # plt.figure(figsize=(10, 6))
# # # plt.figure(figsize=(255, 500))
# # ys, xs, patches = plt.hist(
# #     b_hist,
# #     bins=256,
# #     density=True,
# #     cumulative=False,
# #     histtype="bar",
# #     orientation="vertical",
# #     rwidth=0.9,
# #     color="indigo",
# # )

# # y_min, y_max = plt.ylim()
# # plt.ylim(y_min, y_max + 0.05)

# # # plt.yticks([])
# # plt.xticks(
# #     [(xs[i] + xs[i + 1]) / 2 for i in range(0, len(xs) - 1)],
# #     ["{:.1f} ~ {:.1f}".format(xs[i], xs[i + 1]) for i in range(0, len(xs) - 1)],
# # )

# # plt.show()
# # plt.get_current_fig_manager().window.wm_geometry("-600-400")
# # fig, ax = plt.subplots()
# # print(matplotlib.get_backend())
# # mngr = fig.canvas.manager.window.setPosition((x, y))

# # hist_w = 512
# # hist_h = 400
# # bin_w = int(round(hisw_w / histSize))
# # histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)


# # cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type)

# # data = [[1, 2, 3, 4], [5, 6, 7, 8]]

# # dataframe = pd.DataFrame(data)
# # dataframe.to_csv(
# #     "/Users/KJH/OneDrive - konkuk.ac.kr/git/ros_galapagos_cormorant/test.csv",
# #     header=False,
# #     index=False,
# # )
