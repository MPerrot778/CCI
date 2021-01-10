import src.image_map

class Bot:
    def __init__(self, map, drone):
        self.unscrambled_map = map
        self.drone = drone
        self.dimension = self.drone.size
        self.cost = 0
        self.validated_map = [False for _ in range(self.drone.size) for _ in range(self.drone.size)]
        
    def get_map(self):
        pass

    def get_game_map(self):
        """
        Returns the current Game map.
        """
        pass
        
    def filter_map(self):
        for i in range(self.dimension):
            y_range = range(self.dimension)
            if i%2 == 1:
                y_range = range(self.dimension - 1, -1 , -1)
            for j in y_range:
                self.move_drone((i,j))
                while self.drone.get_top_color() != None:
                    self.drone.take()

                if i != 0 and j != 0:
                    for k in range(self.dimension):
                        for l in range(self.dimension):
                            if self.drone.get_memory().get_upper_view()[k][l] in self.drone.get_hopper() and self.drone.get_memory().get_pixel_color((k, l, self.dimension-1)) != None:
                                self.move_drone((k,l))
                                most_present_color = self.drone.get_memory().get_upper_view()[k][l]
                                while most_present_color in self.drone.get_hopper():
                                    self.drone.drop(most_present_color)
                    if len(self.drone.get_hopper()) != 0: 
                        most_present_color = self.drone.get_hopper()[0]  
                        # Move to position [i][j-1]
                        while most_present_color in self.drone.get_hopper():
                            self.drone.drop(most_present_color)


                            
    def move_drone(self, position):
        # Move x
        if self.drone.position[0] < position[0]:
            for x in range(self.drone.position[0] + 1, position[0] + 1):
                self.cost += self.drone.move(x, self.drone.position[1])
        else:
            for x in range(position[0] + 1, self.drone.position[0] + 1, -1):
                self.cost += self.drone.move(x, self.drone.position[1])
        
        # Move y
        if self.drone.position[1] < position[1]:
            for y in range(self.drone.position[1] + 1, position[1] + 1):
                self.cost += self.drone.move(self.drone.position[0], y)
        else:
            for y in range(position[1] + 1, self.drone.position[1] + 1, -1):
                self.cost += self.drone.move(self.drone.position[0], y)

    def reconstruire(self):
        pass
        #for i in range(0,self.dimension,-1):
           # for j in range(self.dimension):




    def create_hole(self):
        pass

    def move(self):
        #filtre des couleurs
        


        #Reconstruction
        

        #Faire les trous
        pass

