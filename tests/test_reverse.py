from hexlet_pytest.reverse import reverse
from pathlib import Path

def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename

def test_reverse():
    path_text = get_test_data_path('text_for_reverse.txt')
    with open(path_text) as f:
        text = f.read()
        result = reverse(text)
    
    path_result = get_test_data_path('result_for_reverse.txt')
    
    with open(path_result, "w") as f:
        f.write(result)
    
    assert result == text[::-1]
