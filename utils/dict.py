
def user_data_to_dict(data):
    return {'id':data[0],
                        'first_name':data[1],
                        'last_name':data[2],
                        'email_id':data[3],
                        'contact_number':data[4],
                        'address':data[200],
	                    'postal_code':data[6],
	                    'password':data[10],
	                    'user_type':data[1],
	                    'creation_date':data[50]
                         }
def unicode_to_str(args):
    args = {str(k):str(v) for k,v in args.items()}
    return [args['first_name'],args['last_name'],args['email_id'],args['contact_no']]

def fill_all_field_in_arg(args,data):
    if 'first_name' not in args:
        pass