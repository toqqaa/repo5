import imageio.v2 as imageio
import matplotlib.pyplot
import matplotlib.patches
import cv2


path = r"D:\Lecturs\Machine Vision\Machine_vision_code\Pics\Cat.jpg"


def intersection_over_union(gt_box, pred_box):
    inter_box_top_left = [max(gt_box[0], pred_box[0]), max(gt_box[1], pred_box[1])]
    inter_box_bottom_right = [
        min(gt_box[0] + gt_box[2], pred_box[0] + pred_box[2]),
        min(gt_box[1] + gt_box[3], pred_box[1] + pred_box[3]),
    ]

    inter_box_w = inter_box_bottom_right[0] - inter_box_top_left[0]
    inter_box_h = inter_box_bottom_right[1] - inter_box_top_left[1]

    intersection = inter_box_w * inter_box_h
    union = gt_box[2] * gt_box[3] + pred_box[2] * pred_box[3] - intersection

    iou = intersection / union

    return iou, intersection, union


im = imageio.imread(path)

gt_box = [1900, 222, 2000, 3650]
pred_box = [2200, 400, 2200, 3000]

fig, ax = matplotlib.pyplot.subplots(1)
ax.imshow(im)

gt_rect = matplotlib.patches.Rectangle(
    (gt_box[0], gt_box[1]),
    gt_box[2],
    gt_box[3],
    linewidth=5,
    edgecolor="r",
    facecolor="none",
)

pred_rect = matplotlib.patches.Rectangle(
    (pred_box[0], pred_box[1]),
    pred_box[2],
    pred_box[3],
    linewidth=5,
    edgecolor=(1, 1, 0),
    facecolor="none",
)
ax.add_patch(gt_rect)
ax.add_patch(pred_rect)

ax.axes.get_xaxis().set_ticks([])
ax.axes.get_yaxis().set_ticks([])

iou, intersect, union = intersection_over_union(gt_box, pred_box)
print(iou, intersect, union)

# matplotlib.pyplot.figure(figsize=(10, 10))
# matplotlib.pyplot.imshow(im[:, :, ::-1])
matplotlib.pyplot.show()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      import imageio.v2 as imageio
import matplotlib.pyplot
import matplotlib.patches
import cv2


path = r"D:\Lecturs\Machine Vision\Machine_vision_code\Pics\Cat.jpg"


def intersection_over_union(gt_box, pred_box):
    inter_box_top_left = [max(gt_box[0], pred_box[0]), max(gt_box[1], pred_box[1])]
    inter_box_bottom_right = [
        min(gt_box[0] + gt_box[2], pred_box[0] + pred_box[2]),
        min(gt_box[1] + gt_box[3], pred_box[1] + pred_box[3]),
    ]

    inter_box_w = inter_box_bottom_right[0] - inter_box_top_left[0]
    inter_box_h = inter_box_bottom_right[1] - inter_box_top_left[1]

    intersection = inter_box_w * inter_box_h
    union = gt_box[2] * gt_box[3] + pred_box[2] * pred_box[3] - intersection

    iou = intersection / union

    return iou, intersection, union


im = imageio.imread(path)

gt_box = [1900, 222, 2000, 3650]
pred_box = [2200, 400, 2200, 3000]

fig, ax = matplotlib.pyplot.subplots(1)
ax.imshow(im)

gt_rect = matplotlib.patches.Rectangle(
    (gt_box[0], gt_box[1]),
    gt_box[2],
    gt_box[3],
    linewidth=5,
    edgecolor="r",
    facecolor="none",
)

pred_rect = matplotlib.patches.Rectangle(
    (pred_box[0], pred_box[1]),
    pred_box[2],
    pred_box[3],
    linewidth=5,
    edgecolor=(1, 1, 0),
    facecolor="none",
)
ax.add_patch(gt_rect)
ax.add_patch(pred_rect)

ax.axes.get_xaxis().set_ticks([])
ax.axes.get_yaxis().set_ticks([])

iou, intersect, union = intersection_over_union(gt_box, pred_box)
print(iou, intersect, union)

# matplotlib.pyplot.figure(figsize=(10, 10))
# matplotlib.pyplot.imshow(im[:, :, ::-1])
matplotlib.pyplot.show()
