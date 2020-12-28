def parse_image_file(inFile):

    with open(inFile,'r') as f:
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

            elif(count > 1 and count <= max_count):
                coords = tuple(part_line[0])
                unscrambled_img[int(coords[0])][int(coords[2])][int(coords[4])] = part_line[2].strip('\n')

            elif(count > max_count+4):
                coords = tuple(part_line[0])
                scrambled_img[int(coords[0])][int(coords[2])][int(coords[4])] = part_line[2].strip('\n')
            count +=1
    
    return unscrambled_img, scrambled_img

img0, img1 = parse_image_file("easy.txt")

