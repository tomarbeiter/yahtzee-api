"""Unit tests for each public method of the Player class"""

import pytest
from yahtzee_api.player import Player

class TestPlayer:
    """Class containing all unit tests for the Player class."""

    def test_roll_dice_rolls_left(self):
        """Tests ValueError when roll_dice(dice_to_roll) method is called without any rolls left in the turn."""
        p = Player("Tom")
        p.rolls_left = 0
        with pytest.raises(ValueError):
            p.roll_dice([0, 0, 0, 0, 0])
        
        p.rolls_left = -1
        with pytest.raises(ValueError):
            p.roll_dice([0, 0, 0, 0, 0])

    def test_roll_dice_dice_to_roll_length(self):
        """Tests ValueError when roll_dice(dice_to_roll) method is called with a dice_to_roll list not of length 5."""
        p = Player("Tom")
        with pytest.raises(ValueError):
            p.roll_dice([0, 0, 0, 0])

        with pytest.raises(ValueError):
            p.roll_dice([0, 0, 0, 0, 0, 0])

    def test_roll_dice_dice_to_roll_value_type(self):
        """Tests TypeError when roll_dice(dice_to_roll) method is called with a dice_to_roll list that contains non-binary values."""
        p = Player("Tom")
        with pytest.raises(TypeError):
            p.roll_dice([3, 0, 0, 1, 0])

    def test_roll_dice_first_roll_has_five(self):
        """Tests VaueError when roll_dice(dice_to_roll) method tries to roll fewer than 5 dice on the first roll of the turn."""
        p = Player("Tom")
        with pytest.raises(ValueError):
            p.roll_dice([1, 0, 0, 0, 0])

    def test_roll_dice_dice_to_roll_type(self):
        """Tests TypeError when roll_dice(dice_to_roll) method is called with a dice_to_roll not of type list."""
        p = Player("Tom")
        dice_to_roll = True
        with pytest.raises(TypeError):
            p.roll_dice(dice_to_roll)

    def test_roll_dice_roll_proper_dice(self):
        """Tests that roll_dice(dice_to_roll) method rolls proper dice according to user input list of binary values."""
        p = Player("Tom")
        p.roll_dice([0, 0, 0, 0, 0])
        # Check that dice are all rolled from the initial [0, 0, 0, 0, 0] configuration.
        for i in range(5):
            assert p.dice[i] >= 1 and p.dice[i] <= 6
        
        # Check that the die in a position marked "False" is not rolled.
        temp = p.dice[0]
        p.roll_dice([1, 0, 0, 0, 0])
        assert temp == p.dice[0]

    def test_end_turn_score_type_value(self):
        """Tests ValueError when end_turn(score_type) method is called with score_type not between 0 and 12, inclusive."""
        p = Player("Tom")
        with pytest.raises(ValueError):
            p.end_turn(-1)

        with pytest.raises(ValueError):
            p.end_turn(13)