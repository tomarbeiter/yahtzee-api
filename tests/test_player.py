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
            p.roll_dice([True, True, True, True, True])
        
        p.rolls_left = -1
        with pytest.raises(ValueError):
            p.roll_dice([True, True, True, True, True])

    def test_roll_dice_dice_to_roll_length(self):
        """Tests ValueError when roll_dice(dice_to_roll) method is called with a dice_to_roll list not of length 5."""
        p = Player("Tom")
        with pytest.raises(ValueError):
            p.roll_dice([True, True, True, True])

        with pytest.raises(ValueError):
            p.roll_dice([True, True, True, True, True, True])

    def test_roll_dice_dice_to_roll_value_type(self):
        """Tests TypeError when roll_dice(dice_to_roll) method is called with a dice_to_roll list that contains non-boolean values."""
        p = Player("Tom")
        with pytest.raises(TypeError):
            p.roll_dice([3, True, True, False, True])

    def test_roll_dice_first_roll_has_five(self):
        """Tests VaueError when roll_dice(dice_to_roll) method tries to roll fewer than 5 dice on the first roll of the turn."""
        p = Player("Tom")
        with pytest.raises(ValueError):
            p.roll_dice([False, True, True, True, True])

    def test_roll_dice_dice_to_roll_type(self):
        """Tests TypeError when roll_dice(dice_to_roll) method is called with a dice_to_roll not of type list."""
        p = Player("Tom")
        dice_to_roll = True
        with pytest.raises(TypeError):
            p.roll_dice(dice_to_roll)

    def test_roll_dice_roll_proper_dice(self):
        """Tests that roll_dice(dice_to_roll) method rolls proper dice according to user input list of boolean values."""
        p = Player("Tom")
        p.roll_dice([True, True, True, True, True])
        # Check that dice are all rolled from the initial [0, 0, 0, 0, 0] configuration.
        for i in range(5):
            assert p.dice[i] >= 1 and p.dice[i] <= 6
        
        # Check that the die in a position marked "False" is not rolled.
        temp = p.dice[0]
        p.roll_dice([False, True, True, True, True])
        assert temp == p.dice[0]

    def test_set_dice_to_reroll_index(self):
        """Tests that input index to set_dice_to_reroll is in range."""
        p = Player("Tom")
        p.rolls_left = 2
        with pytest.raises(ValueError):
            p.set_dice_to_reroll(-1)

        with pytest.raises(ValueError):
            p.set_dice_to_reroll(13)

    def test_set_dice_to_reroll_second_roll(self):
        """Tests that the method will only run on the 2nd and 3rd roll of a player's turn."""
        p = Player("Tom")
        with pytest.raises(ValueError):
            p.set_dice_to_reroll(3)
    
    def test_set_dice_to_reroll_return_length(self):
        """Tests that set_dice_to_reroll returns a list of length 5."""
        p = Player("Tom")
        p.roll_dice([True, True, True, True, True])
        assert len(p.set_dice_to_reroll(2)) == 5

    def test_end_turn_score_type_value(self):
        """Tests ValueError when end_turn(score_type) method is called with score_type not between 0 and 12, inclusive."""
        p = Player("Tom")
        with pytest.raises(ValueError):
            p.end_turn(-1)

        with pytest.raises(ValueError):
            p.end_turn(13)