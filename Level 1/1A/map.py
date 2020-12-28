class create_map:

    def __init__(self,img_map):
        
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
 
    # Image map setter

    def set_pixelColor(self,coordinates,color):
        self.img_map[coordinates[0]][coordinates[1]][coordinates[2]] = color
    
