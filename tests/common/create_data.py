import faker

class create_data:
    def get_phone_number(self):
        f = faker.Faker(locale="zh-CN")
        return f.phone_number()


# print(create_data().get_phone_number())