from dojo_app.config.mysqlconnection import connectToMySQL
from dojo_app.models import ninja_model 

class Dojo:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.name = data['name']


    def __repr__(self) -> str:
        return self.name
    
    @classmethod
    def create(cls,data):
        query = """
                INSERT INTO dojos (name)
                VALUES( %(name)s )
                """
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
    

    @classmethod
    def get_all(cls):

        query = "SELECT * FROM dojos"

        results = connectToMySQL('dojos_and_ninjas').query_db(query)

        dojos = []

        if results:
            for row in results:
                new_dojo = cls(row)

                dojos.append(new_dojo)

        return dojos
    
    @classmethod
    def get_one(cls, id):

        data = {
            "id": id,
        }

        query = """
            SELECT * FROM dojos WHERE id = %(id)s
        """

        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)

        result = results[0]

        dojos = cls(result)

        return dojos
    

    @classmethod
    def get_one_with_ninjas(cls,id):
        data = {
            'id' : id
        }

        query = "SELECT * FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
    
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)

        if results:
            dojo = cls(results[0])

            ninjas = []

            for row in results:

                ninjas_data = {
                    **row,
                    'id' : row['ninjas.id'],
                    'created_at' : row['created_at'],
                    'updated_at' : row['updated_at']

                }

                new_ninja = ninja_model.Ninja(ninjas_data)

                ninjas.append(new_ninja)

            dojo.ninjas = ninjas

        return dojo