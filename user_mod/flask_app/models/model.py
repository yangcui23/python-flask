from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    def __repr__(self):
        return self.first_name

    @classmethod
    def get_all(cls):

        query = "SELECT  * FROM users"

        results = connectToMySQL('users_schema').query_db(query)

        users = []

        if results:
            for row in results:
                new_user = cls(row)

                users.append(new_user)

        return users

    @classmethod
    def create(cls, data):

        query = """
                INSERT INTO users (first_name,last_name,email)
                VALUES( %(first_name)s,%(last_name)s , %(email)s )
                """
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_one(cls, id):

        data = {
            "id": id,
        }

        query = """
            SELECT * FROM users WHERE id = %(id)s
        """

        results = connectToMySQL('users_schema').query_db(query,data)

        result = results[0]

        user = cls(result)

        return user

    @classmethod
    def edit(cls, form ,id):


        data = {
            **form,
            "id" : id

        }
        query = """
            UPDATE users SET 
            first_name = %(first_name)s,
            last_name = %(last_name)s,
            email = %(email)s
            WHERE id = %(id)s
            """
        return connectToMySQL('users_schema').query_db(query,data)
    
    

    @classmethod
    def delete(cls, id):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL('users_schema').query_db(query, data)


