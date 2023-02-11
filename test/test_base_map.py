import numpy as np
import hexy as hx

def test_indexer():
    indexer = lambda k,h: h['id']
    hex_map = hx.HexMap(indexer=indexer)
    axial_coords = hx.get_disk([0, 0, 0], 6)
    hexes= [{'id':index,'coords':axials} for index, axials in enumerate(axial_coords)]
    hex_map[axial_coords] = hexes
    assert len(hexes)
    for i, h in enumerate(hexes):
        assert hex_map.hex_from_index(i) == hexes[i]
        assert i == hexes[i]['id']
