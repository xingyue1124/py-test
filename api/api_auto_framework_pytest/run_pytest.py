import pytest
import sys
sys.path.append('C:\\Users\\xingy\\PycharmProjects\\untitled\\')

if __name__ == '__main__':
    pytest.main(["-s","./frameworkddt/common_pytest.py","--alluredir", "./report/xml"])
