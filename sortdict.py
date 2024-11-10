def dictionary(input_dict, sort_by='key', order='asc'):
    if sort_by == 'key':
        if order == 'asc':
            sorted_items = sorted(input_dict.items())
        else:
            sorted_items = sorted(input_dict.items(), reverse=True)
    elif sort_by == 'value':
        if order == 'asc':
            sorted_items = sorted(input_dict.items(), key=lambda item: item[1])
        else:
            sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    else:
        print("Error: sort_by must be either 'key' or 'value'.")
        return {}

    return dict(sorted_items)


n = int(input("Enter the limit: "))
print("\n")
data={}
for i in range(0,n):
    key = input("Enter key value: ")
    value = input("Enter value: ")
    print("\n")
    data[key]=value


key_asc = dictionary(data, sort_by='key', order='asc')
print("Sorted by keys (asc):", key_asc)

key_desc = dictionary(data, sort_by='key', order='desc')
print("Sorted by keys (desc):", key_desc)

value_asc = dictionary(data, sort_by='value', order='asc')
print("Sorted by values (asc):", value_asc)

value_desc = dictionary(data, sort_by='value', order='desc')
print("Sorted by values (desc):", value_desc)