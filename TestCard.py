"""
Test for the Card test!
"""

# from Card import Food, Food


l = [1,2,3, -4]

filtered_list = [x for x in l if x > 0]
print(filtered_list)
# def test_foodcost():
#     """Test the Foodcost class and if we can afford things as expected"""
#     simple_cost = FoodCost([Food.FISH, Food.FISH])
#     unsufficient_food = [Food.FISH, Food.GRAIN]
#     assert simple_cost.less_than(unsufficient_food)
#     available_fish = [Food.FISH, Food.INVETEBRATE, Food.FISH]
#     assert not simple_cost.less_than(available_fish)
#     available_replacement = [Food.INVETEBRATE, Food.INVETEBRATE, Food.INVETEBRATE, Food.INVETEBRATE]
#     assert not simple_cost.less_than(available_replacement)
