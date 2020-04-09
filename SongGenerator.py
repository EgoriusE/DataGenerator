from BaseGenerator import BaseGenerator


class SongGenerator(BaseGenerator):

    def get_primary_key_data(self, num):
        return range(0, num - 1)

    def get_params(self):
        pass
