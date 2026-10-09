"""
collisions: puck-vs-paddle collision handling.
"""


import math


def handle_paddle_collision(puck, paddle):
    """
    If the puck overlaps the paddle, bounce it off.
    Returns True if a collision was handled this frame.
    """
    dx = puck.x - paddle.x
    dy = puck.y - paddle.y
    distance = math.hypot(dx, dy)
    min_dist = puck.radius + paddle.radius

    if distance < min_dist:
        # Avoid division by zero if centers coincide exactly
        if distance == 0:
            nx, ny = 1.0, 0.0
        else:
            nx = dx / distance
            ny = dy / distance

        # 1. Positional correction: place puck outside the paddle along collision normal
        puck.x = paddle.x + nx * min_dist
        puck.y = paddle.y + ny * min_dist

        # 2. Velocity reflection: reflect velocity across collision normal
        dot = puck.vx * nx + puck.vy * ny
        if dot < 0:
            puck.vx -= 2 * dot * nx
            puck.vy -= 2 * dot * ny
        elif puck.vx == 0 and puck.vy == 0:
            speed = 4.5
            puck.vx = nx * speed
            puck.vy = ny * speed

        return True

    return False

