class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        tot_sales = 0.0
        for sale in self.sales:
            tot_sales += sale
        return tot_sales

    def get_sales(self):
        return self.sales

    def quota(self, quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        if self.total_sales() < other:
            return -1
        elif self.total_sales() > other:
            return 1
        else:
            return 0

    def __str__(self):
        return self.employee_id, "-", self.name, ":", self.total_sales()
