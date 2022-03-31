import graphics


class Button:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = graphics.Text(self.shape.getCenter(), label)

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

    def is_clicked(self, point):
        point_1 = self.shape.getP1()
        point_2 = self.shape.getP2()
        if point.getX() < point_1.getX() or point_1.getX() > point_2.getX():
            return False
        elif point.getY() < point_1.getY() or point.getY() > point_2.getY():
            return False
        else:
            return True

    def color_button(self, color):
        self.shape.setFill(color)
