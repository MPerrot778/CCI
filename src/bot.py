import src.image_map
from src.drone import Drone
from src.image_map import ImageMap

class Bot:
    def __init__(self, map:ImageMap, drone:Drone):
        self.unscrambled_map = map
        self.drone = drone
        self.dimension = self.drone.size
        self.cost = 0
        self.validated_map = [[False for _ in range(self.drone.size)] for _ in range(self.drone.size)]

    def get_map(self):
        pass

    def get_game_map(self):
        """
        Returns the current Game map.
        """
        pass

    def filter_map(self):
        last_color_stack_position = (0,0)
        position_counter = 0
        for x in range(self.dimension):
            y_range = range(self.dimension)
            if x%2 == 1:
                y_range = range(self.dimension - 1, -1 , -1)
            for y in y_range:
                self.move_drone((x,y))
                while self.drone.get_top_color() is not None \
                        and len(self.drone.get_hopper()) < self.drone.get_max_hopper_size():
                    self.drone.take()

                if x != 0 or y != 0:
                    for k in range(self.dimension):
                        for l in range(self.dimension):
                            if self.drone.get_memory().get_upper_view()[k][l] in self.drone.get_hopper() and self.drone.get_memory().get_pixelColor((k, l, self.dimension-1)) is None:
                                self.move_drone((k,l))
                                most_present_color = self.drone.get_memory().get_upper_view()[k][l]
                                while most_present_color in self.drone.get_hopper() \
                                        and self.drone.get_memory().get_pixelColor((k, l, self.dimension-1)) is None:
                                    self.drone.drop(most_present_color)
                    if len(self.drone.get_hopper()) != 0:
                        most_present_color = self.drone.get_hopper()[0]
                        self.move_drone(last_color_stack_position)
                        while most_present_color in self.drone.get_hopper() \
                                and self.drone.get_memory().get_pixelColor((last_color_stack_position[0], last_color_stack_position[1], self.dimension-1)) is None:
                            self.drone.drop(most_present_color)
                        position_counter += 1

                        if (position_counter // self.dimension) % 2 == 0:
                            last_position_y = position_counter % self.dimension
                        else:
                            last_position_y = self.dimension - 1 - (position_counter % self.dimension)
                        last_color_stack_position = (position_counter // self.dimension, last_position_y)



    def move_drone(self, position):
        # Move x
        if self.drone.position[0] < position[0]:
            for x in range(self.drone.position[0] + 1, position[0] + 1):
                self.cost += self.drone.move((x, self.drone.position[1]))
        else:
            for x in range(self.drone.position[0] - 1, position[0] - 1, -1):
                self.cost += self.drone.move((x, self.drone.position[1]))

        # Move y
        if self.drone.position[1] < position[1]:
            for y in range(self.drone.position[1] + 1, position[1] + 1):
                self.cost += self.drone.move((self.drone.position[0], y))
        else:
            for y in range(self.drone.position[1] - 1, position[1] - 1, -1):
                self.cost += self.drone.move((self.drone.position[0], y))

    def reconstruire(self):
        for x in range(self.dimension -1, -1, -1):
            for y in range(self.dimension):
                self.move_drone((x,y))
                colors = self.get_stack_color((x,y))
                needed_colors = sorted(colors)
                for color in needed_colors:
                    next_pos = self.get_closest_color(color)
                    self.move_drone(next_pos)
                    self.drone.take()
                self.move_drone((x,y))
                for color in colors:
                    self.drone.drop(color)
                self.validated_map[x][y] = True


    def get_stack_color(self, position):
        column = self.unscrambled_map.get_3d()[position[0]][position[1]]
        out = []
        for element in column:
            if element is not None:
                out.append(element)
        return out

    def get_closest_color(self, color):
        """
        Retourne le tuple de la position de la couleur similaire la plus proche
        """
        best_pos = (0,0)
        delta = 999
        for x in range(self.dimension):
            for y in range(self.dimension):
                if self.drone.get_memory().get_upper_view()[x][y] == color and not self.validated_map[x][y]:
                    new_delta = abs(self.drone.position[0]-x) + abs(self.drone.position[1] - y)
                    if delta >= new_delta:
                        delta = new_delta
                        best_pos = (x,y)
        return best_pos

    def create_hole(self):
        for i in range(self.dimension): #Position en x
            for j in range(self.dimension): #Position en y
                if all(self.unscrambled_map.get_empty_positions(((i, j, k))) for k in range(self.dimension)):  #Si toutes les cases d'une colonne sont vides, la colonne est considérée comme validée
                    self.validated_map[i][j] = True



        for i in range(self.dimension): #Position en x
            for j in range(self.dimension): #Position en y
                #On se déplace dans le coin en haut à gauche pour commencer
                self.move_drone(i, j)
                while (self.drone.get_top_color() != None): #On s'assure que la colonne contienne au moins un bloc
                    self.drone.take()
                while len(self.drone.get_hopper()) != 0: #Si la colonne n'est pas vide, on poursuit
                    for k in range(self.dimension): #Position en z
                        coordinates = (i, j, k)
                        if self.unscrambled_map.get_pixelColor(coordinates) != None:
                            couleur = self.unscrambled_map.get_pixelColor(coordinates)
                            self.drone.place(couleur, k)




    def move(self):
        #filtre des couleurs
        self.filter_map()
        #Reconstruction
        self.reconstruire()
        #Faire les trous
        #self.create_hole()

