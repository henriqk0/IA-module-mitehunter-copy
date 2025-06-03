from numpy import ndarray


class PatchInferenceRunner:
    def __init__(self, model) -> None:
        self.model = model # está sendo interpretado como um YOLO neste ponto

    def run(self, patch: ndarray) -> ndarray:
        
        results = self.model(patch)
        return results[0].boxes.data.cpu().numpy()