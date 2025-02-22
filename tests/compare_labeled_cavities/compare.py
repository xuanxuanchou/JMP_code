import os
import numpy as np
import csv

file_path1 = "F:/workdir/n2_calculate/data/labeled_cavities/6531eca5c059807382725fd5.npy"
file_path2 = "F:/workdir/n2_calculate/data/labeled_cavities/HCH_PRT.npy"

save_path1 = "F:/workdir/n2_calculate/tests/compare_labeled_cavities/file1.csv"
save_path2 = "F:/workdir/n2_calculate/tests/compare_labeled_cavities/file2.csv"

data1 = np.load(file_path1)
data2 = np.load(file_path2)

cavity_position1 = list(np.argwhere(data1 == 4))
cavity_position2 = list(np.argwhere(data2 == 4))

with open(save_path1, 'w', newline="") as file1:
    writer = csv.writer(file1)

    for item in cavity_position1:
        writer.writerow([item])

with open(save_path2, 'w', newline="") as file2:
    writer = csv.writer(file2)

    for item in cavity_position1:
        writer.writerow([item])
