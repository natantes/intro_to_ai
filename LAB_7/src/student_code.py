import common
import math 

def detect_slope_intercept(image):
    m_step, b_step = 20.0 / 2000, 2000.0 / 2000

    space = common.init_space(2000, 2000)
    for y in range(200):
        for x in range(200):
            if image[y][x] == 0:  
                for m_idx in range(2000):
                    b = y - (m_idx * m_step - 10) * x
                    b_idx = int((b + 1000) / b_step)
                    if 0 <= b_idx < 2000:
                        space[b_idx][m_idx] += 1

    max_votes, line = 0, common.Line()
    for b_idx in range(2000):
        for m_idx in range(2000):
            if space[b_idx][m_idx] > max_votes:
                max_votes, line.b, line.m = space[b_idx][m_idx], b_idx * b_step - 1000, m_idx * m_step - 10
    return line

def detect_circles(image):
    space = common.init_space(200, 200)
    r, circles = 30, 0
    for y in range(200):
        for x in range(200):
            if image[y][x] == 0:  
                for theta in range(360):
                    a, b = x - r * math.cos(math.radians(theta)), y - r * math.sin(math.radians(theta))
                    if 0 <= a < common.constants.WIDTH and 0 <= b < common.constants.HEIGHT:
                        space[int(b)][int(a)] += 1

    threshold = max(n for row in space for n in row)
    for y in range(0, len(space)):  
        for x in range(0, len(space[y])):  
            circles += math.floor(2 * math.pi * r) <= space[y][x] <= threshold
    return circles