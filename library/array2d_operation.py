def addsub(mat :list) -> list:
    """
    [[a0, b0], ..., [an, bn]]  ->  [[a0-b0, a0+b0], ..., [an-bn, an+bn]]
    """
    return [[a+b, a-b] for a, b in mat]
 
def sort2d(mat :list, axis :int) -> list:
    """
    sort [[a0, b0], ..., [an, bn]] by "bi" (axis=1)
    """
    return mat.sort(key=lambda x: x[axis])