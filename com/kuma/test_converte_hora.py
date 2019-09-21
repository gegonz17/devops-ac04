import pytest
from com.kuma.converte_hora import converteHora

def test_hora():
        converteHora = converteHora()
        assert converteHora([25, 70]) == None, "Should be None"