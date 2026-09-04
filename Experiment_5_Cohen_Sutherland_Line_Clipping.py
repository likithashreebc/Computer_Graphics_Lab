# EXPERIMENT – 5
# IMPLEMENT THE COHEN–SUTHERLAND LINE CLIPPING ALGORITHM
#
# Aim:
# To implement the Cohen–Sutherland line clipping algorithm
# using Python and OpenGL-style 2D graphics concepts.

import matplotlib.pyplot as plt


# Clipping window
X_MIN = 100
X_MAX = 400
Y_MIN = 100
Y_MAX = 300

# Region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


def compute_code(x, y):
    """Calculate the region code for a point."""
    code = INSIDE

    if x < X_MIN:
        code |= LEFT
    elif x > X_MAX:
        code |= RIGHT

    if y < Y_MIN:
        code |= BOTTOM
    elif y > Y_MAX:
        code |= TOP

    return code


def cohen_sutherland_clip(x1, y1, x2, y2):
    """Clip a line using the Cohen–Sutherland algorithm."""
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    while True:

        # Both points are inside
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2

        # Line is completely outside
        elif (code1 & code2) != 0:
            return None

        else:
            # Choose a point that is outside
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection with clipping boundary
            if code_out & TOP:
                x = x1 + (x2 - x1) * (Y_MAX - y1) / (y2 - y1)
                y = Y_MAX

            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (Y_MIN - y1) / (y2 - y1)
                y = Y_MIN

            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (X_MAX - x1) / (x2 - x1)
                x = X_MAX

            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (X_MIN - x1) / (x2 - x1)
                x = X_MIN

            # Replace the outside point with intersection point
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)


def main():
    # Example line
    x1, y1 = 50, 50
    x2, y2 = 450, 350

    clipped_line = cohen_sutherland_clip(x1, y1, x2, y2)

    # Display result
    plt.figure(figsize=(8, 6))

    # Draw clipping window
    window_x = [X_MIN, X_MAX, X_MAX, X_MIN, X_MIN]
    window_y = [Y_MIN, Y_MIN, Y_MAX, Y_MAX, Y_MIN]
    plt.plot(window_x, window_y, 'k-', linewidth=2, label='Clipping Window')

    # Draw original line
    plt.plot([x1, x2], [y1, y2], 'r--', linewidth=2, label='Original Line')

    # Draw clipped line
    if clipped_line is not None:
        cx1, cy1, cx2, cy2 = clipped_line
        plt.plot(
            [cx1, cx2],
            [cy1, cy2],
            'b-',
            linewidth=4,
            label='Clipped Line'
        )

        print("Line accepted.")
        print(f"Clipped line: ({cx1:.2f}, {cy1:.2f}) to "
              f"({cx2:.2f}, {cy2:.2f})")
    else:
        print("Line rejected. It lies completely outside the window.")

    plt.xlim(0, 500)
    plt.ylim(0, 400)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Cohen–Sutherland Line Clipping Algorithm")
    plt.grid(True)
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == "__main__":
    main()
