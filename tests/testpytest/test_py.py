import pytest


@pytest.mark.usefixtures("study_fix")
class TestPractice:
    @pytest.mark.run(order=2)
    def test_01(self):
        print("case1dd")
    # @pytest.mark.mam
    @pytest.mark.run(order=1)
    def test_02(self):
        print("case2ff")
        assert 1==2


# if __name__ == '__main__':
#     pytest.main(["-sv", "./test_py.py","-m=tee"])
