from project.calculation import calculate_school_average

def test_calculate_school_average_with_values():
    
    data = [1, 2, 3]
    result = calculate_school_average(data)
    assert result == 2, f"We expected average 2, got {result}"

def test_calculate_school_average_empty():
    
    data = []
    result = calculate_school_average(data)
    assert result == 0, "We expected 0 when data is empty"
