BOARD_LENGTH = 7
EXIT_ROW = 3
EXIT_COLUMN = 7


class Board:
    """
    A class that create objects from Board type that has two attributes: graphic representation of the board and a list of
    the cars on the board.
    """

    def __init__(self):
        """
        Initializes a Board object with a graphic representation and an empty list of cars.
        """
        self.__graphic_board = self._make_board()
        self.__cars_on_board = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        col_separator = " "
        row_separator = "\n"
        board_row = []
        for row in self.__graphic_board:
            board_row.append(col_separator.join(row))
        board = row_separator.join(board_row)
        return board

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        list_of_cells = []
        for row in range(BOARD_LENGTH):
            for column in range(BOARD_LENGTH):
                list_of_cells.append((row, column))
        list_of_cells.append((EXIT_ROW, EXIT_COLUMN))
        return list_of_cells

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        possible_moves_list = []
        for this_car in self.__cars_on_board:
            this_car_name = this_car.get_name()
            all_moves = this_car.possible_moves()
            this_car_coordinates = this_car.car_coordinates()
            if "u" in all_moves:
                if self._move_is_valid(this_car_coordinates, "u"):
                    possible_moves_list.append((this_car_name, "u", all_moves.get("u")))
                if self._move_is_valid(this_car_coordinates, "d"):
                    possible_moves_list.append((this_car_name, "d", all_moves.get("d")))
            elif "r" in all_moves:
                if self._move_is_valid(this_car_coordinates, "r"):
                    possible_moves_list.append((this_car_name, "r", all_moves.get("r")))
                if self._move_is_valid(this_car_coordinates, "l"):
                    possible_moves_list.append((this_car_name, "l", all_moves.get("l")))
        return possible_moves_list

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return (EXIT_ROW, EXIT_COLUMN)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for this_car in self.__cars_on_board:
            if coordinate in this_car.car_coordinates():
                return this_car.get_name()
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        for car_on_board in self.__cars_on_board:
            if car_on_board.get_name() == car.get_name():
                return False
        if not self._put_is_valid(car):
            return False
        self.__cars_on_board.append(car)
        car_coordinate = car.car_coordinates()
        car_name = car.get_name()
        for coordinate in car_coordinate:
            coordinate_row = coordinate[0]
            coordinate_col = coordinate[1]
            self.__graphic_board[coordinate_row][coordinate_col] = car_name
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        valid_movekey = "udrl"
        valid_name = "YBOGWR"
        if not movekey in valid_movekey:
            return False
        if not name in valid_name:
            return False
        is_car_exists = False
        for car in self.__cars_on_board:
            if car.get_name() == name:
                is_car_exists = True
        if is_car_exists == False:
            return False
        for car in self.__cars_on_board:
            if name == car.get_name():
                car_coordinate = car.car_coordinates()
                break
        if not self._move_is_valid(car_coordinate, movekey):
            return False
        head_row = car_coordinate[0][0]
        head_col = car_coordinate[0][1]
        tail_row = car_coordinate[len(car_coordinate) - 1][0]
        tail_col = car_coordinate[len(car_coordinate) - 1][1]
        if movekey == "u":
            for car in self.__cars_on_board:
                if name == car.get_name():
                    if car.move("u") == False:
                        return False
                self.__graphic_board[head_row - 1][head_col] = name
                self.__graphic_board[tail_row][tail_col] = "_"
        if movekey == "d":
            for car in self.__cars_on_board:
                if name == car.get_name():
                    if car.move("d") == False:
                        return False
                self.__graphic_board[head_row][head_col] = "_"
                self.__graphic_board[tail_row + 1][tail_col] = name
        if movekey == "r":
            for car in self.__cars_on_board:
                if name == car.get_name():
                    if car.move("r") == False:
                        return False
                self.__graphic_board[head_row][head_col] = "_"
                self.__graphic_board[tail_row][tail_col + 1] = name
        if movekey == "l":
            for car in self.__cars_on_board:
                if name == car.get_name():
                    if car.move("l") == False:
                        return False
                self.__graphic_board[head_row][head_col - 1] = name
                self.__graphic_board[tail_row][tail_col] = "_"
        return True

    def _make_board(self):
        """An helper function that creates and returns a valid board."""
        board = []
        for row in range(BOARD_LENGTH):
            board_row = []
            for column in range(BOARD_LENGTH):
                board_row.append("_")
            board.append(board_row)
        board[EXIT_ROW].append("E")
        return board

    def _move_is_valid(self, this_car_coordinates, direction):
        """An helper function that gets a car coordinates and a direction and returns True if the asked move is valid,
        False if isn't."""
        first_coordinate_row = this_car_coordinates[0][0]
        second_coordinate_row = this_car_coordinates[1][0]
        if first_coordinate_row != second_coordinate_row:
            car_orientation = 0
        else:
            car_orientation = 1
        if direction == "u":
            if car_orientation == 1:
                return False
            coordinate_row = this_car_coordinates[0][0]
            coordinate_col = this_car_coordinates[0][1]
            if coordinate_row == 0:
                return False
            if self.__graphic_board[coordinate_row - 1][coordinate_col] != "_":
                return False
            return True
        if direction == "d":
            if car_orientation == 1:
                return False
            coordinate_row = this_car_coordinates[len(this_car_coordinates) - 1][0]
            coordinate_col = this_car_coordinates[0][1]
            if coordinate_row == BOARD_LENGTH - 1:
                return False
            if self.__graphic_board[coordinate_row + 1][coordinate_col] != "_":
                return False
            return True
        if direction == "r":
            if car_orientation == 0:
                return False
            coordinate_row = this_car_coordinates[0][0]
            coordinate_col = this_car_coordinates[len(this_car_coordinates) - 1][1]
            if coordinate_row == EXIT_ROW and coordinate_col == EXIT_COLUMN - 1:
                return True
            if coordinate_col == BOARD_LENGTH - 1:
                return False
            if self.__graphic_board[coordinate_row][coordinate_col + 1] != "_":
                return False
            return True
        if direction == "l":
            if car_orientation == 0:
                return False
            coordinate_row = this_car_coordinates[0][0]
            coordinate_col = this_car_coordinates[0][1]
            if coordinate_col == 0:
                return False
            if self.__graphic_board[coordinate_row][coordinate_col - 1] != "_":
                return False
            return True

    def _put_is_valid(self, car):
        """An helper function that gets an object from Car type and returns True if its possible to place it on the
        current board due to the constraints, False if isnt."""
        car_coordinates = car.car_coordinates()
        for coordinate in car_coordinates:
            coordinate_row = coordinate[0]
            coordinate_col = coordinate[1]
            if coordinate_row < 0 or coordinate_row > BOARD_LENGTH - 1:
                return False
            if coordinate_col < 0 or coordinate_col > BOARD_LENGTH - 1:
                return False
            if self.__graphic_board[coordinate_row][coordinate_col] != "_":
                return False
        return True
