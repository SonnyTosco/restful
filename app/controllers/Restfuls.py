from system.core.controller import *

class Restfuls(Controller):
    def __init__(self, action):
        super(Restfuls, self).__init__(action)
        self.load_model('Restful')
        self.db = self._app.db

    def index(self):
        print "hit index"
        products=self.models['Restful'].product()
        return self.load_view('index.html', products=products)

    def show(self, id):
        print "hit show controller"
        show=self.models['Restful'].show_product(id)
        print "This is the name", show[0]['name']
        print show
        return self.load_view('show.html', product=show[0])

    def edit(self, id):
        show=self.models['Restful'].show_product(id)
        return self.load_view('edit.html', product=show[0])

    def new(self):
        return self.load_view('new.html')

    def create(self):
        print "hit create method in controller"
        products = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
        }
        self.models['Restful'].add_product(products)
        return redirect('/')

    def destroy(self, id):
        print "hit destroy"
        delete={
            'id': id,
        }
        self.models['Restful'].delete(delete)
        return redirect('/')

    def update(self, id):
        print "hit update controller"
        update = {
            'id': id,
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
        }
        self.models['Restful'].update_product(update)
        return redirect('/')
