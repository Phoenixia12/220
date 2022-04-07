import graphics


class Door:

    def __init__(self, shape, label, secret):
        self.shape = shape
        self.text = graphics.Text(self.shape.getCenter(), label)
        self.secret = secret

    def get_label(self):
        return self.text.getText()

    def set_label(self, new_label):
        self.text.setText(new_label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def open(self, color, label):
        self.shape.setFill(color)
        self.set_label(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.set_label(label)

    def door_color(self, color):
        self.shape.setFill(color)

    def set_secret(self, secret):
        self.secret = secret

    def is_secret(self):
        return self.secret == True

    def is_clicked(self, point):
        point_1 = self.shape.getP1()
        point_2 = self.shape.getP2()
        if point.getX() < point_1.getX() or point.getX() > point_2.getX():
            return False
        elif point.getY() < point_1.getY() or point.getY() > point_2.getY():
            return False
        else:
            return True






