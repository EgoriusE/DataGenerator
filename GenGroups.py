from BaseGenerator import BaseGenerator


class GenGroups(BaseGenerator):

    def get_params(self):
        group = {
            'country': self.address.calling_code(),
            'icon_path': self.generic.path.project_dir(),
            'desc': self.text.sentence()
        }
        print(group)
        return group

    def get_primary_key_data(self, num):
        self.clear_data()
        while num != 0:
            name = self.person.name()
            if not (name in self.data):
                self.data.add(name)
                num = num - 1
