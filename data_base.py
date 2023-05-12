import psycopg2

from Contact_book.contact import Contact

DB_NAME = "Contact_Book"
DB_USER = "postgres"
DB_PASS = "K@1ina44D"
DB_HOST = "localhost"
DB_PORT = "5432"  # we can don't use this, because it is standard port


class DataBase:
    def __init__(self):
        # connect to exist database
        self.connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        self.connection.autocommit = True
        print("Database connected successfully...")

    def get_data(self):
        # get data from a table
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM "Contact_data" ORDER BY first_name;
                """
            )

            all_data = cursor.fetchall()
            print("Download all data from Database...")

        return all_data

    def add_contact(self, new_contact: Contact):
        # insert data into a table
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"""
                INSERT INTO "Contact_data" 
                    (first_name, last_name, phone_number, department, favorites) 
                VALUES
                    ('{new_contact.first_name}', 
                    '{new_contact.last_name}', 
                    '{new_contact.phone_number}', 
                    '{new_contact.department}', 
                    {new_contact.favorites});
                """
            )

            print("Data was successfully inserted...")

    def delete_contact(self, phone_number):
        # delete one row from a table
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"""
                DELETE FROM "Contact_data" 
                WHERE phone_number='{phone_number}';
                """
            )

            print("Deleted one row from Database successfully...")

    def edit_contact(self, new_contact: Contact, old_number):
        # update one row in a table
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"""UPDATE "Contact_data" 
                SET first_name = '{new_contact.first_name}',
                    last_name = '{new_contact.last_name}',
                    phone_number = '{new_contact.phone_number}'
                WHERE phone_number = '{old_number}';"""
            )

            print("Update one row in a Database successfully...")

    def add_to_favorites(self, phone_number):
        # Update favorites to True
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"""
                UPDATE "Contact_data" 
                SET favorites = True
                WHERE phone_number = '{phone_number}';
                """
            )

            print("Update contact's favorites to True in a Database successfully...")

    def delete_from_favorites(self, phone_number):
        # Update favorites to False
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"""
                        UPDATE "Contact_data" 
                        SET favorites = False
                        WHERE phone_number = '{phone_number}';
                        """
            )

            print("Update contact's favorites to False in a Database successfully...")

    def close_connection(self):
        self.connection.close()
        print("Database connection closed...")
