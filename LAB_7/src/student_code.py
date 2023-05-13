import common
import math 

def detect_slope_intercept(image):
    m_bins = b_bins = 2000
    m_step, b_step = 20.0 / m_bins, 2000.0 / b_bins 

    space = common.init_space(b_bins, m_bins)
    for y in range(200):
        for x in range(200):
            if image[y][x] == 0:  
                for m_idx in range(m_bins):
                    m = m_idx * m_step - 10
                    b = y - m * x
                    b_idx = int((b + 1000) / b_step)
                    if 0 <= b_idx < b_bins:
                        space[b_idx][m_idx] += 1

    max_votes, line = 0, common.Line()
    for b_idx in range(b_bins):
        for m_idx in range(m_bins):
            if space[b_idx][m_idx] > max_votes:
                max_votes, line.b, line.m = space[b_idx][m_idx], b_idx * b_step - 1000, m_idx * m_step - 10
    return line

def detect_circles(image):
    space = common.init_space(common.constants.HEIGHT, common.constants.WIDTH)
    r, circles = 30, 0
    threshold = 2 * math.pi * r
    for y in range(common.constants.HEIGHT):
        for x in range(common.constants.WIDTH):
            if image[y][x] == 0:  
                for theta in range(360):
                    a = x - r * math.cos(math.radians(theta))
                    b = y - r * math.sin(math.radians(theta))
                    if 0 <= a < common.constants.WIDTH and 0 <= b < common.constants.HEIGHT:
                        space[int(b)][int(a)] += 1

    for y in range(1, len(space)):  
        for x in range(1, len(space[y])):  
            circles += space[y][x] > threshold
    return circles
				