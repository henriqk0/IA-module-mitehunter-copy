import numpy as np
from numpy import array

class DetectionMerger:
    def merge(self, detections_list: list, offsets: list[tuple]):
        combined = []
        for dets, (x_off, y_off) in zip(detections_list, offsets):
            for x1, y1, x2, y2, conf, cls in dets:
                combined.append([x1 + x_off, y1 + y_off, x2 + x_off, y2 + y_off, conf, cls])
        return np.array(combined)
