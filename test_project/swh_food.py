from restaurant import restaurant
import random

# restaurant data entry
man_hing_kee = restaurant("man hing kee", True, 50, False, "HK", True, True, True)
lams_car_noodle = restaurant("lams car noodle", True, 40, False, "HK", False, True, True)
zeppelin_hot_dog = restaurant("zeppelin hot dog", True, 50, True, "HK", False, False, False)
daigo_tw = restaurant("daigo tw", True, 60, False, "TW", True, True, False)
liu_jp = restaurant("liu jp", True, 80, True, "JP", True, True, True)
jariya_thai = restaurant("jariya thai", True, 150, True, "TH", True, True, True)
pizza_pie = restaurant("pizza pie", True, 100, True, "HK", False, False, False)
tamjai = restaurant("tamjai", False, 50, False, "HK", False, True, True)
ultimate_car_noodle = restaurant("ultimate car noodle", True, 40, False, "HK", False, True, True)
sakura = restaurant("sakura", True, 30, False, "JP", True, False, False)
wo_kee = restaurant("wo kee", True, 60, False, "HK", True, True, False)
ho_kee = restaurant("ho kee", True, 50, False, "HK", True, True, True)
golden_chicken = restaurant("golden chicken", True, 50, False, "TH", True, False, False)
wheat_kitchen = restaurant("wheat kitchen", True, 50, False, "HK", True, True, False)
food_angel_13 = restaurant("food angel 13", True, 80, False, "US", True, True, False)
little_chong_hing = restaurant("little chong hing", False, 50, False, "CN", False, True, False)
fairwood = restaurant("fairwood", True, 50, False, "HK", True, True, False)
chiu_mai_roll = restaurant("chiu mai roll", True, 50, False, "HK", True, False, False)

restaurant_list = [man_hing_kee, lams_car_noodle, zeppelin_hot_dog, daigo_tw, liu_jp,
                   jariya_thai, pizza_pie, tamjai, ultimate_car_noodle, sakura, wo_kee,
                   ho_kee, golden_chicken, wheat_kitchen, food_angel_13, little_chong_hing,
                   fairwood, chiu_mai_roll]
fit_choice = []
fit_choice_country_shadow = []
fit_choice_food_type_shadow = []
criteria_console = ["Budget", "Which country is it from", "Type of food", "Hot-air or not"]


def print_criteria_console():
    print('\n'.join(['{}. {}'.format(i + 1, val) for i, val in (enumerate(criteria_console))]))


# print details of the restaurant suggested
def print_details(resto):
    print("\nYour suggestion is: \n" + resto.name)
    if resto.is_yellow:
        if resto.is_hot_air:
            print("It's a yellow shop offering hot-air " + resto.country + " cuisines.")
        else:
            print("It's a yellow shop offering non-hot-air " + resto.country + " cuisines.")
    else:
        if resto.is_hot_air:
            print("It's not a yellow shop, and it offers hot-air " + resto.country + " cuisines.")
        else:
            print("It's not a yellow shop, and it offers non-hot-air " + resto.country + " cuisines.")
    print("The budget is around $" + str(resto.price) + " for each person.")
    food_choice = []
    if resto.have_rice:
        food_choice.append("rice")
    if resto.have_noodle:
        food_choice.append("noodle")
    if resto.have_veggie:
        food_choice.append("veggie")
    if len(food_choice) != 0:
        print("You can have ", end="")
        print(*food_choice, sep=", ", end="")
        print(" here.\n")


# non hot air step 4
def criteria_is_hot_air():
    exclude_hot_air = 0
    while exclude_hot_air != "n" and exclude_hot_air != "y":
        print("\nDo you want to exclude all hot-air food? y/n")
        exclude_hot_air = str(input("")).lower()
        if exclude_hot_air == "y":
            if len(fit_choice) == 0:
                for i in restaurant_list:
                    if not i.is_hot_air:
                        fit_choice.append(i)
            for i in fit_choice:
                if i.is_hot_air:
                    fit_choice.remove(i)
        hot_air_next = 0
        while hot_air_next != "y" and hot_air_next != "n":
            print("\nDo you want to add another criteria? y/n")
            hot_air_next = input("If no, a suggestion will be given based on your set criteria.\n")
            if hot_air_next == "y":
                criteria()
            elif hot_air_next == "n":
                if len(fit_choice) == 0:
                    fit_choice.extend(restaurant_list)
                random_recommend()
            else:
                print("Please enter again.")
        else:
            print("Please enter correctly!")


# budget step 4
def criteria_budget():
    try:
        budget = int(input("\nWhat's your maximum budget?\n"))
        if len(fit_choice) == 0:
            for i in restaurant_list:
                if i.price <= budget:
                    fit_choice.append(i)
        for i in fit_choice:
            if i.price >= budget:
                fit_choice.remove(i)
        budget_next = 0
        while budget_next != "y" and budget_next != "n":
            print("\nDo you want to add another criteria? y/n")
            budget_next = input("If no, a suggestion will be given based on your set criteria.\n")
            if budget_next == "y":
                criteria()
            elif budget_next == "n":
                random_recommend()
            else:
                print("Please enter again.")
    except ValueError:
        print("Please enter an integer!")
        criteria_budget()


# country step 4
def criteria_country():
    print("1. HK\n2. TW\n3. JP\n4. Thai\n5. US\n6. CN")
    print("Please specify which countries' cuisines you like.")
    print("Enter the respective number one by one. Enter OK to finish.")
    country_enter = 0
    hk_terminate = 0
    tw_terminate = 0
    jp_terminate = 0
    th_terminate = 0
    us_terminate = 0
    cn_terminate = 0
    first_round = False
    if len(fit_choice) == 0:
        first_round = True
    while country_enter != "ok":
        country_enter = input("")
        if country_enter == "1":
            print("HK food, gotcha. Anymore? Enter OK to finish.")
            if hk_terminate == 0:
                if first_round:
                    for i in restaurant_list:
                        if i.country == "HK":
                            fit_choice.append(i)
                for i in fit_choice:
                    if i.country == "HK":
                        fit_choice_country_shadow.append(i)
            hk_terminate += 1
        elif country_enter == "2":
            print("TW food, gotcha. Anymore? Enter OK to finish.")
            if tw_terminate == 0:
                if first_round:
                    for i in restaurant_list:
                        if i.country == "TW":
                            fit_choice.append(i)
                for i in fit_choice:
                    if i.country == "TW":
                        fit_choice_country_shadow.append(i)
            tw_terminate += 1
        elif country_enter == "3":
            print("JP food, gotcha. Anymore? Enter OK to finish.")
            if jp_terminate == 0:
                if first_round:
                    for i in restaurant_list:
                        if i.country == "JP":
                            fit_choice.append(i)
                for i in fit_choice:
                    if i.country == "JP":
                        fit_choice_country_shadow.append(i)
            jp_terminate += 1
        elif country_enter == "4":
            print("Thai food, gotcha. Anymore? Enter OK to finish.")
            if th_terminate == 0:
                if first_round:
                    for i in restaurant_list:
                        if i.country == "TH":
                            fit_choice.append(i)
                for i in fit_choice:
                    if i.country == "TH":
                        fit_choice_country_shadow.append(i)
            th_terminate += 1
        elif country_enter == "5":
            print("US food, gotcha. Anymore? Enter OK to finish.")
            if us_terminate == 0:
                if first_round:
                    for i in restaurant_list:
                        if i.country == "US":
                            fit_choice.append(i)
                for i in fit_choice:
                    if i.country == "US":
                        fit_choice_country_shadow.append(i)
            us_terminate += 1
        elif country_enter == "6":
            print("CN food, what??? Fine! Anymore? Enter OK to finish.")
            if cn_terminate == 0:
                if first_round:
                    for i in restaurant_list:
                        if i.country == "CN":
                            fit_choice.append(i)
                for i in fit_choice:
                    if i.country == "CN":
                        fit_choice_country_shadow.append(i)
            cn_terminate += 1
        elif country_enter == "ok":
            fit_choice.clear()
            fit_choice.extend(fit_choice_country_shadow)
            print("Your preferences are saved.")
            country_next = 0
            while country_next != "y" and country_next != "n":
                print("\nDo you want to add another criteria? y/n")
                country_next = input("If no, a suggestion will be given based on your set criteria.\n")
                if country_next == "y":
                    criteria()
                elif country_next == "n":
                    random_recommend()
                else:
                    print("Please enter again.")
        else:
            print("Please enter a valid integer!")


# food type step 4
def criteria_food_type():
    print("1. Rice\n2. Noodle\n3. Veggie\n4. Other food")
    print("Please specify which type of food you like.")
    print("Enter the respective number one by one. Enter OK to finish.")
    food_type_enter = 0
    rice_terminate = 0
    noodle_terminate = 0
    veggie_terminate = 0
    others_terminate = 0
    first_round = False
    if len(fit_choice) == 0:
        first_round = True
    while food_type_enter != "ok":
        food_type_enter = input("").lower()
        if food_type_enter == "1":
            print("Rice, gotcha. Anymore? Enter OK to finish.")
            if rice_terminate == 0:
                if first_round:
                    for i in restaurant_list:
                        if i.have_rice:
                            fit_choice.append(i)
                for i in fit_choice:
                    if i.have_rice:
                        if i not in fit_choice_food_type_shadow:
                            fit_choice_food_type_shadow.append(i)
            rice_terminate += 1
        elif food_type_enter == "2":
            print("Noodle, gotcha. Anymore? Enter OK to finish.")
            if noodle_terminate == 0:
                if len(fit_choice) == 0:
                    for i in restaurant_list:
                        if i.have_noodle:
                            fit_choice.append(i)
                for i in fit_choice:
                    if i.have_noodle:
                        if i not in fit_choice_food_type_shadow:
                            fit_choice_food_type_shadow.append(i)
            noodle_terminate += 1
        elif food_type_enter == "3":
            print("Veggie, gotcha. Anymore? Enter OK to finish.")
            if veggie_terminate == 0:
                if len(fit_choice) == 0:
                    for i in restaurant_list:
                        if i.have_veggie:
                            fit_choice.append(i)
                for i in fit_choice:
                    if i.have_veggie:
                        if i not in fit_choice_food_type_shadow:
                            fit_choice_food_type_shadow.append(i)
            veggie_terminate += 1
        elif food_type_enter == "4":
            print("Other food, gotcha. Anymore? Enter OK to finish.")
            if others_terminate == 0:
                if len(fit_choice) == 0:
                    for i in restaurant_list:
                        if not i.have_rice and not i.have_veggie and not i.have_noodle:
                            fit_choice.append(i)
                for i in fit_choice:
                    if not i.have_rice and not i.have_veggie and not i.have_noodle:
                        if i not in fit_choice_food_type_shadow:
                            fit_choice_country_shadow.append(i)
            others_terminate += 1
        elif food_type_enter == "ok":
            fit_choice.clear()
            fit_choice.extend(fit_choice_food_type_shadow)
            print("Your preferences are saved.")
            food_type_next = 0
            while food_type_next != "y" and food_type_next != "n":
                print("\nDo you want to add another criteria? y/n")
                food_type_next = input("If no, a suggestion will be given based on your set criteria.\n")
                if food_type_next == "y":
                    criteria()
                elif food_type_next == "n":
                    random_recommend()
                else:
                    print("Please enter again.")
        else:
            print("Please enter a valid integer!")


# step 3
def criteria():
    print_criteria_console()
    if criteria_console == 0:
        print("You have already set all the criteria!")
        random_recommend()
    else:
        try:
            criteria_ = int(input("\nPlease enter the number: "))
            if criteria_ in list(range(1, len(criteria_console) + 1)):
                if criteria_console[criteria_ - 1] == "Budget":
                    criteria_console.remove("Budget")
                    criteria_budget()
                elif criteria_console[criteria_ - 1] == "Which country is it from":
                    criteria_console.remove("Which country is it from")
                    criteria_country()
                elif criteria_console[criteria_ - 1] == "Type of food":
                    criteria_console.remove("Type of food")
                    criteria_food_type()
                elif criteria_console[criteria_ - 1] == "Hot-air or not" and criteria_ != 0:
                    criteria_console.remove("Hot-air or not")
                    criteria_is_hot_air()
            else:
                print("Please enter correctly!")
                criteria()
        except ValueError:
            print("Please enter an Integer!")
            criteria()


# suggest a random restaurant 3
def random_recommend():
    random_repick = "y"
    while random_repick == "y":
        if len(fit_choice) == 0:
            random_repick = 0
            print("\nNo restaurant matched...")
            restart = 0
            while restart != "y" and restart != "n":
                restart = input("Try again? y/n\n").lower()
                if restart == "y":
                    start()
                elif restart == "n":
                    print("See you next time!")
                else:
                    print("please enter again.")
        else:
            random_pick = random.choice(fit_choice)
            print_details(random_pick)
            random_repick = 0
            while random_repick != "n" and random_repick != "y":
                random_repick = input("Another suggestion? y/n\n").lower()
                if random_repick == "n":
                    print("Enjoy!")
                elif random_repick != "y":
                    print("Please enter again.")


# testing
def random_recommend2():
    for i in fit_choice:
        print(i.name)


# main 2
def recommend():
    print("\nOkay! Let me help you pick the best food to have in Sai Wan Ho.")
    criteria_or_random = 0
    while criteria_or_random != "y" and criteria_or_random != "n":
        criteria_or_random = input("Do you want to set a criteria? y/n\n").lower()
        if criteria_or_random == "y":
            criteria()
        elif criteria_or_random == "n":
            print("Here's your random pick.")
            fit_choice.extend(restaurant_list)
            random_recommend()
        else:
            print("\nPlease input again.")


# start 1
def start():
    is_hungry = input("\nAre you hungry? y/n\n").lower()
    fit_choice.clear()
    fit_choice_country_shadow.clear()
    fit_choice_food_type_shadow.clear()
    criteria_console.clear()
    criteria_console.append("Budget")
    criteria_console.append("Which country is it from")
    criteria_console.append("Type of food")
    criteria_console.append("Hot-air or not")
    if is_hungry == "y":
        recommend()
    elif is_hungry == "n":
        print("\nYou can call me again anytime you need.")
        print("(Enter y to call again.)")
        call_again = 0
        while call_again != "y":
            call_again = input("").lower()
            if call_again == "y":
                start()
    else:
        print("Wrong input! Please enter again.")
        start()


# initiation
print("\n**********************************************")
print("Welcome to the super Sai Wan Ho food guide 1.0")
print("                                              ")
print("                                         by JK")
print("**********************************************")
print("")
start()
