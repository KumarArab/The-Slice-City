from flask import Flask, render_template, request

app = Flask(__name__)

#Variable declaration
cart = {}
total_price = 0.0
discount = 0.0
offers = {}

#Price declaration
prices = {
    'Margherita':9,
    'American-Pepperoni': 12,
    'La-Reine': 18,
    'Hot-Honey':10,
    'Etna':15,
    'Pollo-Froza':20,
    'Pomodero-Pesto':14,
    'Calabrese':17,
    'Impossible-Teriyaki':21,
    'Giardiniera':25,
    'Hawaii-Not':22,
    'Carbonara':15,
}

menu_items = (('Classic Pizzas','classic/classic-main.jpg'), ('Romana Pizzas','romana/romana-main.jpg',) ,('Veg Pizzas','veg/veg-main.jpg',),
              ('Non-Veg Pizzas', 'non-veg/non-veg-main.jpg', ),('Extraas', 'pizza-mania/pizza-mania-main.jpg',),( 'Dessert and Beverages','beverages/beverages-main.jpg',),)

classic_menu_items = [
    ["Margherita", "https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539755747-LBLXZ8TYX6M1QPYMCENP/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyD4IQ_uEhoqbBUjTJFcqKvko9JlUzuVmtjr1UPhOA5qkTLSJODyitRxw8OQt1oetw/Classic+-+Margherita.png", 9, ],
    ["American-Pepperoni", "https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539768464-K0RJN9AJT9E34AJYR1NQ/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyD4IQ_uEhoqbBUjTJFcqKvko9JlUzuVmtjr1UPhOA5qkTLSJODyitRxw8OQt1oetw/Classic+-+American.png", 12, ],
    ["La-Reine", "https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539778893-4ZWF8WTNRCL8IQPPQPE6/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyD4IQ_uEhoqbBUjTJFcqKvko9JlUzuVmtjr1UPhOA5qkTLSJODyitRxw8OQt1oetw/Classic+-+La+Reine.png", 18],
    ["Hot-Honey", "https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539790677-6W68ZT0H39OOCERMK0B3/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyD4IQ_uEhoqbBUjTJFcqKvko9JlUzuVmtjr1UPhOA5qkTLSJODyitRxw8OQt1oetw/Classic+-+Hot+Honey.png", 10],
    ["Etna", "https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539804812-HKN2QA00PPO632UL61S4/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyD4IQ_uEhoqbBUjTJFcqKvko9JlUzuVmtjr1UPhOA5qkTLSJODyitRxw8OQt1oetw/Classic+-+Etna.png", 15],
    ["Pollo-Froza", "https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539818137-F68Z3UFRYC7B2GUUE8S3/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyD4IQ_uEhoqbBUjTJFcqKvko9JlUzuVmtjr1UPhOA5qkTLSJODyitRxw8OQt1oetw/Classic+-+Pollo+Forza.png", 20],
]

romana_menu_items = [
    ["Pomodero-Pesto", "https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539662265-43COKZG1IUO9MZ4X3AGV/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyD4IQ_uEhoqbBUjTJFcqKvko9JlUzuVmtjr1UPhOA5qkTLSJODyitRxw8OQt1oetw/Romana+-+Pomodoro+Pesto.png",14,],
    ["Calabrese", "https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539673556-A7XL9JHDILTJR1I8OZ02/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyD4IQ_uEhoqbBUjTJFcqKvko9JlUzuVmtjr1UPhOA5qkTLSJODyitRxw8OQt1oetw/Romana+-+Calabrese.png", 17],
    ["Impossible-Teriyaki", "https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539688958-VTIB7ERII057ZW518J0L/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyD4IQ_uEhoqbBUjTJFcqKvko9JlUzuVmtjr1UPhOA5qkTLSJODyitRxw8OQt1oetw/Romana+-+Impossible+Teriyaki.png", 21],
    ["Giardiniera","https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539704123-7A1OODLQZ3WDSGYP0MEL/ke17ZwdGBToddI8pDm48kKxV1HjDlKmWwPrddk-1eqlZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpxIp3boBRzC4-pIRLvxsXdvfOpho_f8YMLZSJIpVJMiM1kVsD2ymYah8XvRUlaUYA4/Romana+-+Giardiniera.png",25],
    ["Hawaii-Not","https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539719102-KZIBC7I2XXDR5JON4XQ7/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyD4IQ_uEhoqbBUjTJFcqKvko9JlUzuVmtjr1UPhOA5qkTLSJODyitRxw8OQt1oetw/Romana+-+Hawaii-Not.png",22],
    ["Carbonara","https://images.squarespace-cdn.com/content/v1/5d82f7e96faf7d39e22a6468/1605539732732-EAK80TZU7NJ8CRDTNENT/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyD4IQ_uEhoqbBUjTJFcqKvko9JlUzuVmtjr1UPhOA5qkTLSJODyitRxw8OQt1oetw/Romana+-+Carbonara.png",15],
]

# ROUTES WITH DEFINTIONS

# Classic Menu
@app.route('/classic-menu.html', methods=['GET','POST'])
def classic():
    global total_price  # reffering to global declared variables
    global discount
    if request.method == 'POST':        # fetching data from Add to Cart Form
        if request.form.get("product_name") in cart:        # If items exits in the cart then increment the quantity or just create a new entry
            cart[request.form.get("product_name")]["quantity"] += 1
            cart[request.form.get("product_name")]["price"] += prices[request.form.get("product_name")]
        else:
            cart[request.form.get("product_name")] = {
                "quantity": 1,
                "price": prices[request.form.get("product_name")]
            }
        total_price += prices[request.form.get("product_name")]     # summing total price

# OFFERS ZONE STARTS

        if len(cart) > 2:       # offer : Buy 3 or more different types of pizzas and get a Marghertia pizza for free
            if "THREEFREE" not in offers:
                offers["THREEFREE"] = {'product': ' Free Margherita','price':9}
                discount += 9
        if "Giardiniera" in cart:   #offer : Buy 2 or more Giardiniera pizza and get beverages free worth SGD 20
            if cart["Giardiniera"]["quantity"] > 2:
                if "BEVRICH" not in offers:
                    offers["BEVRICH"] = {'product':'Beverages','price':20}
                    discount += 20
        if total_price > 59:        #offer : CartValue of $59 and above gets free delivery
            if  "FREEDELIVERY" not in offers:
                offers["FREEDELIVERY"] = {'product':"Free Delivery",'price':9}
                discount += 9

# OFFER ZONE ENDS

    return render_template('classic-menu.html', classic_menu_items=classic_menu_items)


# Romana Menu

@app.route('/romana-menu.html', methods=['GET','POST'])
def romana():
    global total_price
    global discount
    if request.method == 'POST':
        if request.form.get("product_name") in cart:
            cart[request.form.get("product_name")]["quantity"] += 1
            cart[request.form.get("product_name")]["price"] += prices[request.form.get("product_name")]
        else:
            cart[request.form.get("product_name")] = {
                "quantity": 1,
                "price": prices[request.form.get("product_name")]
            }
        total_price += prices[request.form.get("product_name")]

# OFFERS ZONE STARTS

        if len(cart) > 2:
            if "THREEFREE" not in offers:
                offers["THREEFREE"] = {'product': ' Free Margherita','price':9}
                discount += 9
        if "Giardiniera" in cart:
            if cart["Giardiniera"]["quantity"] >= 2:
                if "BEVRICH" not in offers:
                    offers["BEVRICH"] = {'product':'Beverages','price':20}
                    discount += 20
        if total_price > 59:
            if  "FREEDELIVERY" not in offers:
                offers["FREEDELIVERY"] = {'product':"Free Delivery",'price':9}
                discount += 9

# OFFER ZONE ENDS

    return render_template('romana-menu.html', romana_menu_items=romana_menu_items)




# Home: The Slice City
@app.route('/slice.html')
def home():
    return render_template('slice.html', menu_items=menu_items,  cart = cart, total= total_price, offers= offers, discount=discount)

# ROUTE ENDS



# MAIN
if __name__ == '__main__':
    app.run(debug=True)

# remove "debug = True" before submission