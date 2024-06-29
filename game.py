import sys
import helper
import board
import car

BOARD_LENGTH = 7


class Game:
    """
    A class that create objects from Game type. The goal of the object is to manage the game (get inputs from the user
    and implement it).
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__game_board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        exit_row = self.__game_board.target_location()[0]
        exit_col = self.__game_board.target_location()[1]
        exit_coordinate = (exit_row, exit_col)
        if self.__game_board.cell_content(exit_coordinate) != None:
            print("Congratulations! you won!")
            return
        all_possible_moves = self.__game_board.possible_moves()
        if len(all_possible_moves) == 0:
            print("There are no available moves to do.")
            return
        print(self.__game_board)
        user_input = input(
            "Please Choose the car you want to move and the direction.\nIf you want to exit please press '!' "
        )
        if user_input == "!":
            print("Bye Bye!")
            return
        input_validation = self._is_input_valid(user_input)
        if input_validation == False:
            print("Your input is invalid, try again.")
            return self.__single_turn()
        move_validation = self.__game_board.move_car(user_input[0], user_input[2])
        if move_validation == False:
            print("You can't move to the chosen direction, try again.")
            return self.__single_turn()
        return self.__single_turn()

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        self.__single_turn()
        return None

    def _is_input_valid(self, user_input):
        """An helper function that gets the input from the user and return True if its in the right length, False if isnt. """
        if len(user_input) != 3 or user_input[1] != ",":
            return False
        return True


def is_car_valid(car_name, car_length, car_coordinate, car_orientation, game_board):
    """An helper function that gets a car name, length, coordinates, orientation and the current game board and
    returns True if all the arguments are valids, False if arent"""
    valid_name = "YBOGWR"
    if not car_name in valid_name:
        return False
    if car_length < 2 or car_length > 4:
        return False
    for coordinate in car_coordinate:
        if (
            coordinate[0] < 0
            or coordinate[0] > BOARD_LENGTH - 1
            or coordinate[1] < 0
            or coordinate[1] > BOARD_LENGTH - 1
        ):
            return False
    if car_orientation != 0 and car_orientation != 1:
        return False
    return True


if __name__ == "__main__":
    game_board = board.Board()
    all_cars_dictionary = helper.load_json(sys.argv[1])  # a dictionary
    for current_car in all_cars_dictionary:
        car_name = current_car
        car_length = all_cars_dictionary.get(current_car)[0]
        car_orientation = all_cars_dictionary.get(current_car)[2]
        car_location = []
        for length in range(car_length):
            row_location = all_cars_dictionary.get(current_car)[1][0]
            col_location = all_cars_dictionary.get(current_car)[1][1]
            if car_orientation == 0:
                car_location.append(((row_location + length), col_location))
            if car_orientation == 1:
                car_location.append((row_location, (col_location + length)))
        if is_car_valid(
            car_name, car_length, car_location, car_orientation, game_board
        ):
            game_board.add_car(
                car.Car(car_name, car_length, car_location, car_orientation)
            )
    rush_hour = Game(game_board)
    rush_hour.play()
