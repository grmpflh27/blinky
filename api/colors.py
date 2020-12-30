from enum import Enum

from math import floor
from typing import Tuple


# https://stackoverflow.com/questions/21117842/converting-an-rgbw-color-to-a-standard-rgb-hsb-representation
def rgb_to_rgbw(rgb=Tuple[int, int, int]) -> Tuple[int, int, int, int]:
    Ri, Gi, Bi = rgb
    M = max(Ri, Gi, Bi)
    m = min(Ri, Gi, Bi)

    if (m/M < 0.5):
        Wo = (m*M) / (M-m) 
    else:
        Wo =  M 
    
    Q = 255
    K = (Wo + M) / m
    Ro = floor((K * Ri - Wo) / Q )
    Go = floor((K * Gi - Wo) / Q )
    Bo = floor((K * Bi - Wo) / Q )

    return (Ro, Go, Bo, round(Wo))


COLORS = dict(
    BLUE = (33, 150, 243, 0),
    ORANGE = (255, 152, 0, 0),
    BROWN = (121, 85, 72, 0),
    RED = (244, 67, 54, 0),
    GREEN = (76, 175, 80, 0),
    WHITE = (255, 255, 255, 0),
    YELLOW = (255, 235, 59, 0),
    CYAN = (0, 255, 255, 0),
    LIME = (255, 235, 59, 0),
    BLACK = (0, 0, 0, 0),
    BLUE_DARK = (255, 235, 59, 0),
    GREY = (158, 158, 158, 0),
    TEAL = (0, 150, 136, 0),
)