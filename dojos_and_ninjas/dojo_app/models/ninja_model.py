from dojo_app.config.mysqlconnection import connectToMySQL
from dojo_app.models import dojo_model 


class Ninja:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']

    def __repr__(self):
        return self.first_name

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO ninjas (first_name,last_name,age,dojo_id)
                VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
                """
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_one(cls, id):

        data = {
            "id": id,
        }

        query = """
             SELECT * FROM ninjas WHERE id = %(id)s
            """

        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        result = results[0]

        ninjas = cls(result)
        print(ninjas)
        return ninjas

    @classmethod
    def get_all(cls):

        query = "SELECT * FROM ninjas"

        results = connectToMySQL('dojos_and_ninjas').query_db(query)

        ninjas = []

        if results:
            for row in results:
                new_ninja = cls(row)

                ninjas.append(new_ninja)
        print(results)
        return ninjas
    


