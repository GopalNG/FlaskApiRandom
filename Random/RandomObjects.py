import random
import string
import os
from datetime import datetime

Folder_Path = os.path.join(os.path.abspath(os.getcwd()), "saved_files")


def file_name(filename=datetime.now().strftime("%y%m%d%H%M")):
    return filename  # os.path.join(Folder_Path, filename + '.txt'), filename


class RandomObjects:

    def __init__(self, k_value=500, _bytes=2097152):
        """
        :param k_value: a random number between this number # large number you give looping count decrease
        :param _bytes: out put file size # here 2097152 is 2 mb in binary (system)
        :param file_name: out put file name
        """
        self._bytes = _bytes
        self.k_value = k_value
        self.file_name = file_name()

    @staticmethod
    def _get_digit(k_value):
        return ''.join(random.choices(string.digits, k=k_value))

    @staticmethod
    def _get_float(k_value):
        _value = str(round(random.uniform(1.1, float(k_value)), k_value))
        return _value

    @staticmethod
    def _get_alphanumeric(k_value):
        def randstr(chars=string.ascii_uppercase + string.digits, n=10):
            return ''.join(random.choice(chars) for _ in range(n))

        return randstr(n=k_value)

    @staticmethod
    def _get_alphabets(k_value):
        return ''.join(random.choices(string.ascii_lowercase, k=k_value))

    @staticmethod
    def random_def(_k_value) -> tuple:
        """
        :param _k_value: is a number to generate the random string or length of individual string
        :return: type (tuple) index 0 for string generated and 1st index independent object lengths
        """

        r_k_value = _k_value - 4  # ","
        _k_value = [r_k_value // 4 + (1 if x < r_k_value % 4 else 0) for x in range(4)]  # spilt passed value

        f_rtn = RandomObjects._get_float(_k_value[0])
        if len(f_rtn) != _k_value[0]:
            _k_value[1] = _k_value[1] + (_k_value[0] - len(f_rtn))
        d_rtn = RandomObjects._get_digit(_k_value[1])
        a_rtn = RandomObjects._get_alphanumeric(_k_value[2])
        al_rtn = RandomObjects._get_alphabets(_k_value[3])

        full_string = f_rtn + "," + d_rtn + "," + a_rtn + "," + al_rtn + ","
        list_independent_lens = [len(f_rtn), len(d_rtn), len(a_rtn), len(al_rtn)]

        return full_string, list_independent_lens

    def random_objects_main(self) -> tuple:
        """
        :return: a tuple first index are independent values of each object and 2nd file location
        """
        # with open(self.path, 'w') as f:
        _counter = 0
        k_value = None
        length_of_each_objects = [0, 0, 0, 0]
        results = list()

        while True:
            # Assign K
            if k_value is None:
                k_value = random.randint(1, self.k_value)
            else:
                k_value = random.randint(5, self.k_value)
                _check_value = _counter + k_value
                if _check_value > self._bytes:
                    k_value = self._bytes - _counter

            followed_value = self.random_def(k_value)
            _o_value = len(followed_value[0])
            _counter += _o_value
            length_of_each_objects = list(map(sum, zip(*[length_of_each_objects, followed_value[1]])))

            # f.write(followed_value[0])
            results.append(followed_value[0])

            if _counter >= self._bytes:
                break

        return length_of_each_objects, results, self.file_name
