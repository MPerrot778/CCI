
class image_map:

    def __init__(self,inFile):
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
                    unscrambled_img = [[["" for k in range(n)] for j in range(n)] for i in range(n)]
                    scrambled_img  = [[[""]*n]*n]*n
                    print(max_count)

                elif(count > 1 and count <= max_count):
                    print(line)
                    coords = tuple(part_line[0])
                    unscrambled_img[int(coords[0])][int(coords[2])][int(coords[4])] = part_line[2].strip('\n')

                elif(count > max_count+4):
                    print(line)
                    coords = tuple(part_line[0])
                    scrambled_img[int(coords[0])][int(coords[2])][int(coords[4])] = part_line[2].strip('\n')
                count +=1
        
        return unscrambled_img, scrambled_img


    def get_ImageSize(self):
        return(len(self.unscrambled))
    
    def get_2DMap(self):
        return(self.scrambled[1][0][:])



def main():
    map = image_map("hard.txt")

    img2d = map.get_2DMap()

    print(img2d)

if __name__ == "__main__":
    main()