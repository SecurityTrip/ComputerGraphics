class LineDrawer:
    def line1(x0, y0, x1, y1, img):
        t = 0.0
        while t < 1.0:
            x = x0 * (1. - t) + x1 * t
            y = y0 * (1. - t) + y1 * t
            img.putpixel((int(x), int(y)), 255)
            t += 0.01

    def line2(x0, y0, x1, y1, img):
        for i in range(int(x0), int(x1)):
            t = (i - x0) / (float)(x1 - x0)
            y = y0 * (1. - t) + y1 * t
            img.putpixel((round(i), round(y)), 255)

    def line3(x0, y0, x1, y1, img):
        steep = False
        if abs(x0 - x1) < abs(y0 - y1):
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            steep = True

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        for i in range(int(x0), int(x1)):
            t = (i - x0) / (float)(x1 - x0)
            y = y0 * (1. - t) + y1 * t
            if (steep):
                img.putpixel((int(y), int(i)), 255)
            else:
                img.putpixel((int(i), int(y)), 255)

    def line4(x0, y0, x1, y1, img):
        steep = False
        if abs(x0 - x1) < abs(y0 - y1):
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            steep = True

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = x1 - x0
        dy = y1 - y0

        derror = abs(dy / dx)

        error = 0
        y = y0

        for i in range(int(x0), int(x1)):
            t = (i - x0) / (float)(x1 - x0)
            y = y0 * (1. - t) + y1 * t
            if (steep):
                img.putpixel((int(y), int(i)), 255)
            else:
                img.putpixel((int(i), int(y)), 255)

            error += derror
            if error > 0.5:
                if y1 > y0:
                    y += 1
                else:
                    y -= 1

                error -= 1

    def DrawObjModel (p, img):
        v = p.v_arr
        f = p.f_arr
        print(v)
        for i in f:
            LineDrawer.line4(v[int(i[0] - 1)][0] * 10000 - 500, v[int(i[0] - 1)][1] * -10000,
                    v[int(i[1] - 1)][0] * 10000 - 500, v[int(i[1] - 1)][1] * -10000, img)
            LineDrawer.line4(v[int(i[1] - 1)][0] * 10000 - 500, v[int(i[1] - 1)][1] * -10000,
                       v[int(i[2] - 1)][0] * 10000 - 500, v[int(i[2] - 1)][1] * -10000, img)
            LineDrawer.line4(v[int(i[2] - 1)][0] * 10000 - 500, v[int(i[2] - 1)][1] * -10000,
                       v[int(i[0] - 1)][0] * 10000 - 500, v[int(i[0] - 1)][1] * -10000, img)

    def DrawObjPoints(p, img):
        for i in p.v_arr:
            img.putpixel((int(i[0] * 10000) - 500, int(i[1] * -10000)), 255)
