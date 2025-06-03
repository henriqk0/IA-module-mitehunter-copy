class ConvertYolo():

    def convert_to_yolo_format(self, detection, image_width, image_height):
        """
        Converte uma detecção do formato [x1, y1, x2, y2, conf, cls]
        para o formato YOLO: [xc, yc, w, h], normalizado.
        """
        x1, y1, x2, y2, conf, cls = detection

        xc = ((x1 + x2) / 2) / image_width
        yc = ((y1 + y2) / 2) / image_height
        w = (x2 - x1) / image_width
        h = (y2 - y1) / image_height

        return [xc, yc, w, h, conf, cls]