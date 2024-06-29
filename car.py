class Car:
    """
    A class that create objects from Car type that has four attributes: name, length, location and orientation.
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__car_name = name
        self.__car_length = length
        self.__car_location = location
        self.__car_orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coordinates_list = []
        if self.__car_orientation == 1:
            for i in range(self.__car_length):
                coordinates_list.append(
                    (self.__car_location[0][0], self.__car_location[0][1] + i)
                )
        elif self.__car_orientation == 0:
            for i in range(self.__car_length):
                add_coordinate = (
                    self.__car_location[0][0] + i,
                    self.__car_location[0][1],
                )
                coordinates_list.append(add_coordinate)
        return coordinates_list

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        vertical_moves = {
            "u": "cause the car to move one step up",
            "d": "cause the car to move one step down",
        }
        horizontal_moves = {
            "l": "cause the car to move one step left",
            "r": "cause the car to move one step right",
        }
        if self.__car_orientation == 1:
            return horizontal_moves
        if self.__car_orientation == 0:
            return vertical_moves

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        required_cell = []
        if movekey == "u":
            required_cell.append(
                (self.__car_location[0][0] - 1, self.__car_location[0][1])
            )
            return required_cell
        if movekey == "d":
            required_cell.append(
                (self.__car_location[0][0] + 1, self.__car_location[0][1])
            )
            return required_cell
        if movekey == "l":
            required_cell.append(
                (self.__car_location[0][0], self.__car_location[0][1] - 1)
            )
            return required_cell
        if movekey == "r":
            required_cell.append(
                (self.__car_location[0][0], self.__car_location[0][1] + 1)
            )
            return required_cell

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if self.__car_orientation == 1 and (movekey == "r" or movekey == "l"):
            self.__car_location = self.movement_requirements(movekey)
            return True
        if self.__car_orientation == 0 and (movekey == "u" or movekey == "d"):
            self.__car_location = self.movement_requirements(movekey)
            return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__car_name
