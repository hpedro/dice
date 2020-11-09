# -*- coding: UTF-8 -*-

# Import from standard library
import os
import dices
import pandas as pd
# Import from our lib
from dices.lib import clean_data
from dices.lib import throw_dice
import pytest


def test_clean_data():
    datapath = os.path.dirname(os.path.abspath(dices.__file__)) + '/data'
    df = pd.read_csv('{}/data.csv.gz'.format(datapath))
    first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
    assert list(df.columns)[:6] == first_cols
    assert df.shape == (999, 142)
    out = clean_data(df)
    assert out.shape == (985, 119)

def test_throw_dice():
    assert throw_dice() in [1, 2, 3, 4, 5, 6]
