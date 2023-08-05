class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            return "Error: lengths must be positive"
        else:
            self.width = width
            self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2 * (self.width) + 2 * (self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    
    def get_picture(self):
        #Edge Case
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ''
        for _ in range(self.height):
            picture += '*' * self.width + '\n'

        return picture
        
    def get_amount_inside(self, another):
        count = 0

        if another.height > self.height or another.width > self.width:
            return count
        
        #Eat Vertical then eat horizontal
        num_of_vertical_copies = self.height // another.height
        num_of_horizontal_copies = self.width // another.width
        count = num_of_vertical_copies * num_of_horizontal_copies #How many copies of another can fit in to self
        return count

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
        



class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)
    
    def set_side(self, width):
        self.width = width
        self.height = width
    
    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_width(self, width):
        self.set_side(width)

    def set_height(self, width):
        self.set_side(width)
