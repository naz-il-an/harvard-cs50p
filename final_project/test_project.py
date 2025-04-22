import project

screen = project.screen

def test_draw_snake():
    assert project.draw_snake() == None

def test_location_x():
    assert project.x == 240

def test_location_y():    
    assert project.y == 160
