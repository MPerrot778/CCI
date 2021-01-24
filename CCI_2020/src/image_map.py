class ImageMap:

    @staticmethod
    def create(size):
        empty_img = [[[None for k in range(size)] for j in range(size)] for i in range(size)]
        return ImageMap(empty_img)

    def __init__(self, img_map):
        self.img_map = img_map

    # Image map getter

    def get_imageSize(self):
        return(len(self.img_map))

    def get_2dImage(self,layer):
        return(self.img_map[layer])

    def get_3d(self):
        return self.img_map

    def get_pixelColor(self,coordinates):
        return self.img_map[coordinates[0]][coordinates[1]][coordinates[2]]
    
    def get_upper_view(self):
        """
        :return: 2d array of colors
        """
        imgSize = self.get_imageSize()
        upperView =  [[None for j in range(imgSize)] for i in range(imgSize)]
        
        for i in range(imgSize):
            for j in range(imgSize):
                for k in range(imgSize-1,-1,-1):
                    pixel = self.get_pixelColor((i,j,k))
                    if(pixel != None):
                        upperView[i][j] = pixel
                        break
    
        return upperView

        
    def get_empty_positions(self) -> list:
        """
        Finds the (x,y) positions where there are no blocks
        :return: The list of positions
        """
        img_size = self.get_imageSize()
        empty_list = []

        for i in range(img_size):
            for j in range(img_size):
                for k in range(img_size):
                    pixel = self.get_pixelColor((i,j,k))
                    if(pixel == None):
                        empty_list += [(i,j,k)]

        return empty_list

    # Image map setter

    def set_pixelColor(self,coordinates,color):
        self.img_map[coordinates[0]][coordinates[1]][coordinates[2]] = color

    # Operator

    def __eq__(self, other):
        equal = True
        for x in range(self.get_imageSize()):
            for y in range(self.get_imageSize()):
                for z in range(self.get_imageSize()):
                    if self.img_map[x][y][z] != other[x][y][z]:
                        equal = False
        return equal

    def is_position_accessible(self, position) -> bool:
        """
        Validates if we can take a block at the position.
        :param position: (x,y,z) position
        :return: True if the position is valid
        """
        pixel = self.get_pixelColor(position)

        if(pixel != None):
            
            if(position[0] == 0 or position[0] == self.get_imageSize()-1):
                return True
            elif(position[1] == 0 or position[1] == self.get_imageSize()-1):
                return True
            else:
                north_pixel = self.get_pixelColor((position[0],position[1]-1,position[2]))
                south_pixel = self.get_pixelColor((position[0],position[1]+1,position[2]))
                east_pixel = self.get_pixelColor((position[0]-1,position[1],position[2]))
                west_pixel = self.get_pixelColor((position[0],position[1]+1,position[2]))

                if(north_pixel == None or south_pixel == None or east_pixel == None or west_pixel == None):
                    return True
                else:
                    return False
        else:
            return False

        