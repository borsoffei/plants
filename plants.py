class Plant:
    def __init__(self, name, category, filters, photo, description):
        self.name = name
        self.category = category
        self.filters = filters
        self.photo = photo
        self.description = description

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_filters(self):
        return self.filters

    def get_photo(self):
        return self.photo

    def get_description(self):
        return self.description

