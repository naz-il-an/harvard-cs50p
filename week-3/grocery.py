def main():
     x = grocery_list()
     sorted_grocery = dict(sorted(x.items()))
     for i in sorted_grocery:
         print(sorted_grocery[i], i)

def grocery_list():
    dict_grocery = {}
    while True:
        try:
            item = input().upper()
            if item in dict_grocery:
                dict_grocery[item] += 1
            else:
                dict_grocery[item] = 1
        
        except EOFError:

            return dict_grocery
            
        except KeyError:
            break

main()