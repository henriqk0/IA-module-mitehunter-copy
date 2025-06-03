from numpy import ndarray


class PatchDivider:
    def divide(self, image: ndarray, LS: float) -> list[tuple]:
        height, width = image.shape[:2]
        max_dim = max(width, height)
        num_horizontal = 3 if max_dim <= LS else 4
        num_vertical = 2 if max_dim <= LS else 3

        patch_w = width // num_horizontal
        patch_h = height // num_vertical

        patches = []
        for i in range(num_vertical):
            for j in range(num_horizontal):
                x1 = j * patch_w
                y1 = i * patch_h
                x2 = min((j + 1) * patch_w, width)
                y2 = min((i + 1) * patch_h, height)
                patches.append((image[y1:y2, x1:x2], (x1, y1)))

        return patches