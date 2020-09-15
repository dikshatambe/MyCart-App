
def raw_data_to_user_model(data, user):
    user.id = data[0]
    user.first_name = data[1]
    user.last_name = data[2]
    user.email_id = data[3]
    user.contact_number = data[4]
    user.address = data[5]
    user.postal_code = data[6]
    user.password = data[7]
    user.user_type = data[8]
    user.creation_date = data[9]

    return user


def raw_data_to_category_model(data, category):
    category.id = data[0]
    category.cname = data[1]
    category.info = data[2]
    category.is_deleted = data[3]
    category.creation_date = data[4]
    return category


def raw_data_to_product_model(data, products):
    products.id = data[0]
    products.product_name = data[1]
    products.category_id = data[2]
    products.info = data[3]
    products.color = data[4]
    products.product_size = data[5]
    products.price = data[6]
    products.creation_date = data[7]
    return products


def raw_data_to_discount_model(data, discount):
    discount.id = data[0]
    discount.name = data[1]
    discount.amount = data[2]
    discount.discount = data[3]
    discount.discount_type = data[4]
    discount.creation_date = data[5]


def raw_data_to_order_model(data, orders):
    orders.id = data[0]
    orders.user_id = data[1]
    orders.address = data[2]
    orders.discount_id = data[3]
    orders.product_id = data[4]
    orders.quantity = data[5]
    orders.status = data[6]
    orders.amount = data[7]
    orders.creation_date = data[8]
    orders.modification_date = data[9]


def raw_data_to_cart_model(data, userCart):
    userCart.user_cart_id = data[0]
    userCart.order_id = data[1]
    userCart.saved_for_later = data[2]
    userCart.quantity = data[3]
    userCart.creation_date = data[4]


def raw_data_to_cartinfo_model(data, cartInfo):
    cartInfo.cart_id = data[0]
    cartInfo.user_id = data[1]
    cartInfo.product_id = data[2]
    cartInfo.creation_date = data[3]


def user_data_to_dict(data):
    return {'id': data[0],
            'first_name': data[1],
            'last_name': data[2],
            'email_id': data[3],
            'contact_number': data[4],
            'address': data[200],
            'postal_code': data[6],
            'password': data[10],
            'user_type': data[1],
            'creation_date': data[50]
            }


def unicode_to_str(args):
    args = {str(k): str(v) for k, v in args.items()}
    return [args['first_name'], args['last_name'], args['email_id'], args['contact_no']]


def fill_all_field_in_arg(args, data):
    if 'first_name' not in args:
        pass
