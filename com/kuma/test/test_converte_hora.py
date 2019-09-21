import pytest
from com.kuma.converte_hora import converteHora

def test_hora():
    converteHora = converteHora()
    assert converteHora(25, 70) == None, "Should be None"

def test_hora1():
    converteHora = converteHora()
    assert converteHora(11, 0) == '11:00'

def test_hora2():
    converteHora = converteHora()
    assert converteHora(14, 0) == '2:00'
    