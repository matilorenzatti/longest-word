from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            new_game = Game()

            # exercise
            grid = new_game.grid

            # verify
            assert isinstance(grid, list)
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase



    def test_game_is_valid(self):

        # setup
        new_game = Game()
        test_grid = 'OQUWRBAZE'
        test_word = 'BAROQUE'

        # exercise
        new_game.grid = list(test_grid)

        result = new_game.is_valid(test_word)

        # verify
        assert result is True



    def test_game_is_invalid(self):

        # setup
        new_game = Game()
        test_grid = 'OQUWRBAZE'
        test_word = 'BAROQUM'

        # exercise
        new_game.grid = list(test_grid)

        result = new_game.is_valid(test_word)

        # verify
        assert result is False


    def test_unknown_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
