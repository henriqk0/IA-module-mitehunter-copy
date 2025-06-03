from numpy import ndarray


class NMSProcessor:
    def __calculate_diou(self, box1: ndarray, box2: ndarray) -> float:
        # box1 e box2 são listas no formato [x1, y1, x2, y2]
        x1, y1, x2, y2 = box1
        x1g, y1g, x2g, y2g = box2

        # Calcular IoU
        inter_x1 = max(x1, x1g)
        inter_y1 = max(y1, y1g)
        inter_x2 = min(x2, x2g)
        inter_y2 = min(y2, y2g)
        inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)
        box1_area = (x2 - x1) * (y2 - y1)
        box2_area = (x2g - x1g) * (y2g - y1g)
        iou = inter_area / (box1_area + box2_area - inter_area)

        # Calcular distância entre centros
        center_x1 = (x1 + x2) / 2
        center_y1 = (y1 + y2) / 2
        center_x2 = (x1g + x2g) / 2
        center_y2 = (y1g + y2g) / 2
        rho2 = (center_x1 - center_x2) ** 2 + (center_y1 - center_y2) ** 2

        # Calcular diagonal da menor caixa envolvente
        c_x1 = min(x1, x1g)
        c_y1 = min(y1, y1g)
        c_x2 = max(x2, x2g)
        c_y2 = max(y2, y2g)
        c2 = (c_x2 - c_x1) ** 2 + (c_y2 - c_y1) ** 2

        diou = iou - rho2 / c2
        return diou

    def __calculate_iou(self, box1: ndarray, box2: ndarray) -> float:
        x1 = max(box1[0], box2[0])
        y1 = max(box1[1], box2[1])
        x2 = min(box1[2], box2[2])
        y2 = min(box1[3], box2[3])

        inter_area = max(0, x2 - x1) * max(0, y2 - y1)
        box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
        box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])

        return inter_area / (box1_area + box2_area - inter_area)

    def apply(self, detections: ndarray, iou_threshold: float = 0.5, use_diou: bool = True) -> list:
        if len(detections) == 0:
            return []

        detections = sorted(detections, key=lambda x: x[4], reverse=True)
        keep = []

        while detections:
            current = detections.pop(0)
            keep.append(current)
            filtered = []
            for detection in detections:
                if use_diou:
                    diou = self.__calculate_diou(current[:4], detection[:4])
                    if diou < iou_threshold:
                        filtered.append(detection)
                else:
                    iou = self.__calculate_iou(current[:4], detection[:4])
                    if iou < iou_threshold:
                        filtered.append(detection)
        return keep
