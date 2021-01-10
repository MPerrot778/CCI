import image_map.py
class Bot:
    def __init__(self, map, drone):
        self.map = map
        self.drone = drone
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
            for j in range(self.dimension):#A modifier pour ligne pair a gauche et ligne impair a droite
                #Move to position [i][j]
                while self.map[i][j] != "blanc":
                    self.drone.take()
                if i != 0 and j != 0:
                    actual_known_map = self.drone.get_memory()
                    for k in range(self.dimension):
                        for l in range(self.dimension):
                            if map.get_upper_view()[k][l] in self.drone.get_hopper(): #and map.get_upper_view() is not full:
                                # Move to position [k][l]
                                most_present_color = map.get_upper_view()[k][l]
                                while most_present_color in self.drone.get_hopper():
                                    self.drone.drop(most_present_color) # Implementer une fonction qui drop le premier pixel de la couleur nommer quelle trouve dans le hopper
                    if self.drone.get_hopper() not Empty: #Synthaxe incorrect
                        most_present_color = self.drone.get_hopper()[0] # Implementer un tri du hopper()
                        if most_present_color == map.get_upper_view()[k][l]:  
                            # Move to position [i][j-1]
                            while most_present_color == self.drone.get_hopper()[0]
                                self.drone.drop(self.drone.get_hopper()[0]) # Implementer une fonction qui drop le premier pixel de la couleur nommer quelle trouve dans le hopper

    def move_drone(drone, x, y):
        pass

    def reconstruire(self):
        pass                    

    def create_hole(self):
        pass

    def move(self):
        #filtre des couleurs
        


        #Reconstruction
        

        #Faire les trous
        pass

