from src.image_map import ImageMap


class DecodeMap:
    def __init__(self, inFile):

        self.inFile = inFile

        unscrambled, scrambled = self.parse_image_file()

        self.unscrambled = unscrambled
        self.scrambled = scrambled

    def parse_image_file(self):

        with open(self.inFile,'r') as f:
            lines = f.readlines()
            count = 0
            n = 0
            max_count = 0

            unscrambled_img = []
            scrambled_img  = []

            for line in lines:
                part_line = line.partition("=")

                if(count == 1):
                    n = int(part_line[2])
                    max_count = n*n*n
                    unscrambled_img = [[[() for k in range(n)] for j in range(n)] for i in range(n)]
                    scrambled_img  = [[[() for k in range(n)] for j in range(n)] for i in range(n)]

                elif(count > 1 and count <= max_count):
                    pixel = part_line[2].strip('"\n')
                    coords = tuple(map(int,part_line[0].split(',')))

                    if(pixel == ""):
                        pixel_tuple = None
                    else:
                        pixel_tuple = tuple(map(int,pixel.split('_')))

                    unscrambled_img[coords[0]][coords[1]][coords[2]] = pixel_tuple

                elif(count > max_count+4):
                    pixel = part_line[2].strip('"\n')
                    coords = tuple(map(int,part_line[0].split(',')))

                    if(pixel == ""):
                        pixel_tuple = None
                    else:
                        pixel_tuple = tuple(map(int,pixel.split('_')))

                    scrambled_img[coords[0]][coords[1]][coords[2]] = pixel_tuple

                count += 1
        
        return ImageMap(unscrambled_img), ImageMap(scrambled_img)
