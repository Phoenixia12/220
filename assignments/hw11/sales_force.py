class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        in_file = open(file_name, 'r')
        in_file = in_file.readlines()
        for line in in_file:
            sales_person = line.__str__()
            self.sales_people += [sales_person]
