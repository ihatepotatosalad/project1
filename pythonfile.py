print('hello form file')


def hello():
    print('hello user')


def pack(item_1, item_2, item_3):
    return [item_1, item_2, item_3]


def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print('there is no lunch')
    else:
        for i in range(len(lunch_items)):
            if i == 0:
                print(f'first i eat {lunch_items[i]}')
            else:
                print(f'next i eat {lunch_items[i]}')


eat_lunch(['pork', 'juice', 'burger', 'yummy sauce'])
