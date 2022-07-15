class Car:
    objects = []
    
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
        Car.objects.append(self)

    def __str__(self):
        return self
