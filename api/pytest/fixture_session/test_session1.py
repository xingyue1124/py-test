import pytest

class TestSession1():
    def test_1(self,get_token):
        token="23657DGYUSGD126731638712GE18271H"
        assert get_token==token

if __name__ == '__main__':
    pytest.main(["-s","test_session1.py","test_session2.py"])