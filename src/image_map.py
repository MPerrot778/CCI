class ImageMap:

    @staticmethod
    def create(size):
        pass

    def __init__(self, img_map):
        self.img_map = img_map

    def get_imageSize(self):
        return(len(self.img_map))

    # Image map getter
    
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
        pass

    def is_position_accessible(self, position) -> bool:
        """
        Validates if we can take a block at the position.
        :param position: (x,y,z) position
        :return: True if the position is valid
        """
        pass
 
    # Image map setter

    def set_pixelColor(self,coordinates,color):
        self.img_map[coordinates[0]][coordinates[1]][coordinates[2]] = color
    
