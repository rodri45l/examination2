import unittest
import OopPigGame as game
import PIGClasses as pigC
import io
import sys
from PIGClasses import bcolors as LetCol
from unittest.mock import patch
DIVIDER = "===================================================================\
======================================="


class TestPigGame(unittest.TestCase):

    def test_Dice(self):
        '''Test Dice class'''
        die = pigC.Dice()
        self.assertIsInstance(die, pigC.Dice)
    
    
    def test_Player(self):
        playerTest = pigC.Player('Rodri')
        self.assertIsInstance(playerTest, pigC.Player)
    
    def test_sumTurnScore(self):
        playerTest = pigC.Player('Rodri')
        playerTest.score = 6
        playerTest.turnScore = 6
        playerTest.sumTurnScore()
        exp = playerTest.score == 12
        self.assertTrue(exp)
    
    def test_roll_dice(self):
        die = pigC.Dice()
        die.rollDice(True)
        exp = 1 <= die.roll <= 6
        self.assertTrue(exp)

    @patch('builtins.print')
    def test_printWelcomeMessage(self, mock_print):
        game.printWelcomeMessage()
        str = f'{LetCol.HEADER}{DIVIDER}\n\
{LetCol.OKBLUE}{LetCol.UNDERLINE}Welcome to the dice game PIG\n\
{LetCol.NOT_UNDERLINED}{LetCol.OKCYAN}In this game wins the first player to reach 100 points{LetCol.OKCYAN}\n\
Players take turns to roll a single dice as many times\
as they wish,    \nadding all roll results to a running total, but losing \
their gained score for the turn if they roll a 1.\n{LetCol.HEADER}{DIVIDER}'
        mock_print.assert_called_with(str)
