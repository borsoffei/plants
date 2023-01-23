class Symptom:
    def __init__(self, name, category):
        self.name = str(name)
        self.category = str(category)

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category
