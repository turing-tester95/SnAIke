import random


class Map:
    """A class for the map. Contains all attributes which are needed for the bot.

    """

    def __init__(self, ):
        # Window size
        self.__window_x = 72
        self.__window_y = 48
        # defining snake default position
        self.__snake_position = [10, 5]
        # defining first 4 blocks of snake body
        self.__snake_body = [[10, 5],
                             [9, 5],
                             [8, 5],
                             [7, 5]]
        self.__blue_segments = 0
        self.__yellow_segments = 0
        # set a seed for the generator
        random.seed(8)
        # fruit position
        self.__white_fruit = [random.randrange(1, self.__window_x),
                              random.randrange(1, self.__window_y)]

        self.__red_fruits = [[random.randrange(1, self.__window_x),
                              random.randrange(1, self.__window_y)]]

        self.__blue_fruits = [[random.randrange(1, self.__window_x),
                               random.randrange(1, self.__window_y)]]

        self.__yellow_fruit = []

        self.__fruit_spawn = True

        # setting default snake direction towards right
        self.__snake_direction = 'RIGHT'

    @property
    def window_x(self) -> int:
        """ Maximum size of the map in x dimension.

        :return: Maximum x value
        :rtype: int
        """
        return self.__window_x

    @property
    def window_y(self) -> int:
        """Maximum size of the map in y dimension.

        :return: Maximum y value
        :rtype: int
        """
        return self.__window_y

    @property
    def snake_position(self) -> list:
        """Position of the head of the snake.

        :return: x and y coordinates [x,y]
        :rtype: list
        """
        return self.__snake_position

    @snake_position.setter
    def snake_position(self, snake_position: list) -> list:
        self.__snake_position = snake_position

    @property
    def snake_body(self) -> [list]:
        """Coordinates of all parts of the snake body

        :return: x and y coordinates of all body parts
        :rtype: [list]
        """
        return self.__snake_body

    @snake_body.setter
    def snake_body(self, snake_body: list) -> list:
        self.__snake_body = snake_body

    @property
    def white_fruit(self) -> list:
        """Coordinates of the fruit

        :return: x and y coordinates of the fruit
        :rtype: list
        """
        return self.__white_fruit

    @white_fruit.setter
    def fruit_position(self, fruit_position: list):
        self.__white_fruit = fruit_position

    @property
    def red_fruits(self) -> [list]:
        """Coordinates of the poison food

        :return: x and y of the poison food
        :rtype: [list]
        """
        return self.__red_fruits

    @red_fruits.setter
    def red_fruits(self, red_fruits: list):
        self.__red_fruits = red_fruits

    @property
    def blue_fruits(self):
        return self.__blue_fruits

    @blue_fruits.setter
    def blue_fruits(self, blue_fruits: list):
        self.__blue_fruits = blue_fruits

    @property
    def yellow_fruit(self) -> list:
        """Coordinates of super food.

        :return: x and y of super food
        :rtype: list
        """
        return self.__yellow_fruit

    @yellow_fruit.setter
    def yellow_fruit(self, yellow_fruit: list):
        self.__yellow_fruit = yellow_fruit

    @property
    def fruit_spawn(self) -> bool:
        return self.__fruit_spawn

    @fruit_spawn.setter
    def fruit_spawn(self, fruit_spawn: bool):
        self.__fruit_spawn = fruit_spawn

    @property
    def snake_direction(self) -> str:
        """The direction in which the snake is currently heading.

        :return: Directions can be: UP|DOWN|LEFT|RIGHT
        :rtype: str
        """
        return self.__snake_direction

    @property
    def blue_segments(self) -> int:
        return self.__blue_segments

    @blue_segments.setter
    def blue_segments(self, num: int):
        self.__blue_segments = num

    @property
    def yellow_segments(self) -> int:
        return self.__yellow_segments

    @yellow_segments.setter
    def yellow_segments(self, num: int):
        self.__yellow_segments = num

    @snake_direction.setter
    def snake_direction(self, snake_direction: bool):
        self.__snake_direction = snake_direction

    def spawn_white_fruit(self):
        self.__white_fruit = [random.randrange(1, self.__window_x),
                              random.randrange(1, self.__window_y)]
        if self.__white_fruit in self.__blue_fruits or self.__white_fruit in self.__red_fruits:
            self.spawn_white_fruit()
        elif self.__white_fruit == self.__yellow_fruit or self.__white_fruit == self.snake_position:
            self.spawn_white_fruit()

    def spawn_red_fruit(self):
        red_fruit = [random.randrange(1, self.__window_x),
                     random.randrange(1, self.__window_y)]
        if red_fruit in self.__blue_fruits or red_fruit == self.__white_fruit:
            self.spawn_red_fruit()
        elif red_fruit in self.__red_fruits or red_fruit == self.__yellow_fruit:
            self.spawn_red_fruit()
        elif red_fruit == self.__snake_position:
            self.spawn_red_fruit()
        else:
            self.__red_fruits.append(red_fruit)

    def spawn_blue_fruit(self):
        blue_fruit = [random.randrange(1, self.__window_x),
                      random.randrange(1, self.__window_y)]

        if blue_fruit in self.__red_fruits or blue_fruit == self.__white_fruit:
            self.spawn_blue_fruit()
        elif blue_fruit in self.__blue_fruits or blue_fruit == self.__yellow_fruit:
            self.spawn_blue_fruit()
        elif blue_fruit == self.__snake_position:
            self.spawn_blue_fruit()
        else:
            self.__blue_fruits.append(blue_fruit)

    def spawn_yellow_fruit(self):
        self.__yellow_fruit = [random.randrange(1, self.__window_x),
                               random.randrange(1, self.__window_y)]

        if self.__yellow_fruit in self.__red_fruits or self.__yellow_fruit == self.__white_fruit:
            self.spawn_yellow_fruit()
        elif self.__yellow_fruit in self.__blue_fruits or self.__yellow_fruit == self.__snake_position:
            self.spawn_yellow_fruit()
