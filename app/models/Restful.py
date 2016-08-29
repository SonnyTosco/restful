from system.core.model import Model

class Restful(Model):
    def __init__(self):
        super(Restful, self).__init__()

    def product(self):
        print "hit all products"
        query = "SELECT * from products"
        return self.db.query_db(query)

    def add_product(self, products):
        print "hit add_products model"
        query = """INSERT INTO products (name, description, price, created_at, updated_at)
                VALUES(:name, :description, :price, NOW(), NOW())"""
        return self.db.query_db(query, products)

    def show_product(self, id):
        query = "SELECT * FROM products WHERE products.id = :id LIMIT 1"
        data = {
            'id': id
        }
        return self.db.query_db(query, data)

    def update_product(self, update):
        query = """UPDATE products
                SET name=:name, description=:description, price=:price, created_at=NOW(), updated_at=NOW()
                WHERE id = :id"""
        return self.db.query_db(query, update)

    def delete(self, delete):
        query="""DELETE FROM products WHERE products.id = :id"""
        self.db.query_db(query, delete)
