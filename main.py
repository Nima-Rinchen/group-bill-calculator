number_person = int(input('Enter the number of persons: '))
name_list = []

for n in range(number_person):
    name = input('Enter the names of all invovled: ')
    name_list.append(name)

total_cost = int(input('Enter total cost: '))
who_paid = input('name of the payer: ')

def cost_calculator(cost):
    p_item = input('any personal item- y or n: ')
    if p_item == 'n':
        per_head = cost / number_person
        return per_head
    elif p_item == 'y':
        p_item_num = int(input('how many have personal items: '))
        who_p_item = input('name: ')
        who_p_item = who_p_item.split(',')

        for i in range(p_item_num):
            p_cost_list = []
            p_num = int(input('calculating for ' + who_p_item[i] + ' enter the number of items: '))
            for j in range(p_num):
                p_cost = int(input('enter the amount: '))
                p_cost_list.append(p_cost)

            Sum = sum(p_cost_list)

            return Sum



print('per head ' + str(cost_calculator(total_cost)))


