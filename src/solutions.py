from pprint import pprint
from WordCounter import WordCounter
from TaxMan import TaxMan
from Calculator import Calculator
from CarCollector import CarCollector
from Character import Character

people_list = [

    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},

    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},

    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},

]

def ex1():

    def sort_people(list, far, direction):

        if direction == "asc":

            list.sort(key=lambda p:p[far])

        else:

            list.sort(key=lambda p:p[far], reverse=True)




    sort_people(people_list, "age", "asc")

    print(people_list)


def ex2():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

   
    filtered_list = list(filter(lambda p: p['sex'] == 'male', people_list))
    print(filtered_list)








def calc_bmi (people_list):
    #**p part unpacks the dictionary p. It takes all the key-value pairs from p and includes them in the new dictionary being created. 
    # Then, the 'bmi': round(p['weight_kg'] / p['height_meters'] ** 2, 1) 
    # part adds a new key-value pair 'bmi' with the calculated BMI value.
#   ** operator is used for dictionary unpacking. 
# It allows you to create a new dictionary by merging the key-value pairs from an existing dictionary with 
# additional key-value pairs.

    bm_list = list (map(lambda p: { **p,'Bmi':round(p["weight_kg"]/p["height_meters"]** 2, 1)},people_list))
    return bm_list

    
def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people = calc_bmi (people_list)            
    print(new_people)









def get_people(people_list):
    return [p['name'] for p in people_list if p["age"] >= 15]

def ex4():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    print(get_people(people_list))




def main():

    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.


if __name__ == '__main__':
     main()



def main():
 items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},

        {"id": 3, "desc": "razor", "price": 3.00},
    ]
 tm = TaxMan(items, "10%")
 # tm variable represents an instance of the TaxMan class. 
 #TaxMan constructor is called with items and tax_percentage as arguments to create the instance.
 tm.calc_total()
 print(tm.get_total())

if __name__ == '__main__':
     


     main()

  #ex7
def main():

    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())


if __name__ == '__main__':
     main()


# ex8
def main():
 

 pprint(CarCollector.get_data())

if __name__ == '__main__':
     main()

# ex9

def main ():

 f = Fighter(18)
 d = Dwarf(15)
 print(f)
 print(d)
 f.fight(d)
 d.fight(f)
 print(f)
 print(d)
 
if __name__ == '__main__':
     main()
 