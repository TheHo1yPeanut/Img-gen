from PIL import Image, ImageDraw
import math 
import random

background = (0, 0, 0, 255)
size = (1000, 1000)


main = Image.new(
    "RGBA",
    size
)

image_draw = ImageDraw.Draw(main)

class _Shape:
    def __init__(
        self, 
        position: tuple[int, int],
        color: tuple[int, int, int, int])->None:
        self.position = position 
        self.color = color

    def draw(self, imDraw: ImageDraw.ImageDraw):
        pass

    def set_position(self, new_position:tuple[int, int]):
        self.position = new_position


class square(_Shape):
    def __init__(
            self, 
            position: tuple[int, int],
            size, 
            color: tuple[int, int, int, int]):
        super().__init__(position, color)
        self = self
        self.size = size    
    
    def draw(self, imDraw: ImageDraw.ImageDraw):
        imDraw.rectangle((self.position[0], 1000-self.position[1], self.size+self.position[0], self.size+(1000-self.position[1])), self.color)

class circle(_Shape):
    def __init__(
            self, 
            position: tuple[int, int], 
            rad, 
            color: tuple[int, int, int, int]
            ):
        super().__init__(position, color)
        self = self
        self.rad = rad

    def draw(self, imDraw: ImageDraw.ImageDraw):
        imDraw.ellipse([self.position[0]-self.rad, self.position[1]-self.rad, self.position[0]+self.rad, self.position[1]+self.rad], self.color)
        

class star(_Shape):
    def __init__(self, position: tuple[int, int], rad, color: tuple[int, int, int, int]):
        super().__init__(position, color)
        self = self
        self.rad = rad
        self.points = []

    def draw(self, imDraw: ImageDraw.ImageDraw):
        #start with inner point
        for i in range(1, 11):
            if i%2 != 0:
                self.points.append((self.position[0] + math.cos(2*math.pi*(i/10))*(self.rad/2), self.position[1] + math.sin(2*math.pi*(i/10))*(self.rad/2)))
            else: 
                self.points.append((self.position[0] + math.cos(2*math.pi*(i/10))*self.rad, self.position[1] + math.sin(2*math.pi*(i/10))*self.rad))
        print(self.points)
        imDraw.polygon(self.points, self.color)



class skull(_Shape):
    def __init__(self, position:tuple[int, int], color:tuple[int, int, int, int]):
        super().__init__(position, color)
        self = self
        self.squares = []

    def draw(self, imDraw: ImageDraw.ImageDraw):

        self.squares.append(square(self.position, 300, self.color)) #head
        for i in range(3):
            self.squares.append(square([self.position[0]+25+100*(i), self.position[1]-300], 50, self.color))
        self.squares.append(square([self.position[0]+25, self.position[1]-50], 75, background))
        self.squares.append(square([self.position[0]+200, self.position[1]-50], 75, background))

        i = 0
        while i < len(self.squares):
            self.squares[i].draw(imDraw)
            i+=1



class Picture:
    def __init__(self):
        self.layers = []
        self.usedLayerCntr = 0

    def addLayer(self):
        tempVar = Image.new("RGBA", size)
        tempDraw = ImageDraw.Draw(tempVar)
        self.layers.append((tempVar, tempDraw))

    def addShape(self, shape):
        print(self.usedLayerCntr)
        shape.draw(self.layers[self.usedLayerCntr][1])
        self.usedLayerCntr += 1

    def compose(self):
        for element in self.layers:
            main.alpha_composite(element[0])


        
picture = Picture()

star1 = star((300, 300), 200, (255, 255, 0, 150))
skull1 = skull((500, 500), (255, 255, 255, 150))
skull1.set_position((700, 600))
star1.set_position((700, 600))

picture.addLayer()
picture.addLayer()

picture.addShape(star1)
picture.addShape(skull1)

picture.compose()

main.show()



