from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

coco_gt = COCO(
    r"D:\Lecturs\Machine Vision\Machine_vision_code\coco_annotations_ground.json"
)
coco_pred = COCO(
    r"D:\Lecturs\Machine Vision\Machine_vision_code\coco_annotations_predected.json"
)

coco_eval = COCOeval(coco_gt, coco_pred, "bbox")
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()

mAP_50_to_95 = coco_eval.stats[0]
mAP_50 = coco_eval.stats[1]
mAR_50_to_95 = coco_eval.stats[8]
mAR_50 = coco_eval.stats[9]
print("mAP_50_to_95 :", mAP_50_to_95)
print("mAP_50: ", mAP_50)
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

coco_gt = COCO(
    r"D:\Lecturs\Machine Vision\Machine_vision_code\coco_annotations_ground.json"
)
coco_pred = COCO(
    r"D:\Lecturs\Machine Vision\Machine_vision_code\coco_annotations_predected.json"
)

coco_eval = COCOeval(coco_gt, coco_pred, "bbox")
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()

mAP_50_to_95 = coco_eval.stats[0]
mAP_50 = coco_eval.stats[1]
mAR_50_to_95 = coco_eval.stats[8]
print("mAP_50_to_95 :", mAP_50_to_95)
print("mAP_50: ", mAP_50)
print("mAR_50_to_95: ", mAR_50_to_95)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

coco_gt = COCO(
    r"D:\Lecturs\Machine Vision\Machine_vision_code\coco_annotations_ground.json"
)
coco_pred = COCO(
    r"D:\Lecturs\Machine Vision\Machine_vision_code\coco_annotations_predected.json"
)

coco_eval = COCOeval(coco_gt, coco_pred, "bbox")
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()

mAP_50_to_95 = coco_eval.stats[0]
mAP_50 = coco_eval.stats[1]
mAR_50_to_95 = coco_eval.stats[8]
mAR_50 = coco_eval.stats[9]
print("mAP_50_to_95 :", mAP_50_to_95)
print("mAP_50: ", mAP_50)
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

coco_gt = COCO(
    r"D:\Lecturs\Machine Vision\Machine_vision_code\coco_annotations_ground.json"
)
coco_pred = COCO(
    r"D:\Lecturs\Machine Vision\Machine_vision_code\coco_annotations_predected.json"
)

coco_eval = COCOeval(coco_gt, coco_pred, "bbox")
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()

mAP_50_to_95 = coco_eval.stats[0]
mAP_50 = coco_eval.stats[1]
mAR_50_to_95 = coco_eval.stats[8]
print("mAP_50_to_95 :", mAP_50_to_95)
print("mAP_50: ", mAP_50)
print("mAR_50_to_95: ", mAR_50_to_95)
