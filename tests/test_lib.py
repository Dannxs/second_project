from second_project.lib import absolute_value

def test_absolute_value(num = 1):
    assert type(absolute_value(num)) is int
    
