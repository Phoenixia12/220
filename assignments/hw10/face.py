from graphics import Circle, Line, Point, Polygon


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        mouth_dist = (self.mouth.getP2().getX() - self.mouth.getP1().getX()) + (self.mouth.getP1().getX() / 2)
        print(mouth_dist)
        smile_meet = Point(mouth_dist, (self.mouth.getP2().getY() + (self.mouth.getP2().getY() / 12)))
        smile = Polygon(self.mouth.getP1(), self.mouth.getP2(), smile_meet)
        self.mouth.undraw()
        self.mouth = smile
        self.mouth.draw(self.window)

    def shock(self):
        mouth_center = self.mouth.getCenter()
        shock_face = Circle(mouth_center, self.left_eye.getRadius())
        self.mouth.undraw()
        self.mouth = shock_face
        self.mouth.draw(self.window)

    def wink(self):
        wink_center = self.left_eye.getCenter()
        p1 = Point((wink_center.getX() - self.left_eye.getRadius()), wink_center.getY())
        p2 = Point((wink_center.getX() + self.left_eye.getRadius()), wink_center.getY())
        self.left_eye.undraw()
        self.left_eye = Line(p1, p2)
        self.left_eye.draw(self.window)
        self.smile()


