class Illness:
    def __init__(self, name, plant, symptoms, photo, description):
        self.name = name
        self.plant = plant
        self.symptoms = symptoms
        self.photo = photo
        self.description = description

    def get_name(self):
        return self.name

    def get_plant(self):
        return self.plant

    def get_symptoms(self):
        return self.symptoms

    def get_photo(self):
        return self.photo

    def get_description(self):
        return self.description


