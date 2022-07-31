from typing import List

from Types import Food

class FoodCost:
    """
    Describes a comparable class of a food cost.
    """
    def __init__(self, cost: List[Food]):
        self.cost = {
            Food.ANY: 0,
            Food.INVETEBRATE: 0,
            Food.GRAIN : 0,
            Food.FISH : 0,
            Food.RODENT : 0,
            Food.FRUIT : 0
        }
        for food_type in cost:
            self.cost[food_type] += 1

    def within_budget(self, food: List[Food]):
        """
        Checks if a list of foods can afford this foodcost.
        """
        available_food = FoodCost(food)
        ## Lets just count down from our food stores any matching food initially
        remaining_food = FoodCost(food)
        for food_type in self.cost:
            ## We look at any after
            if food_type == Food.ANY:
                continue
            remaining_food.cost[food_type] -= self.cost[food_type]
        ## Now we can just see if the negatives, times two
        any_missing = self.cost[Food.ANY]
        any_missing += sum([abs(x)*2 for x in remaining_food.cost.values() if x < 0])
        available_food = sum([x for x in remaining_food.cost.values() if x > 0])
        return available_food >= any_missing

    def over_budget(self, food: List[Food]):
        """
        Checks if a list of foods can afford this foodcost.
        TODO Avoid this almost complete code duplication
        """
        available_food = FoodCost(food)
        ## Lets just count down from our food stores any matching food initially
        remaining_food = FoodCost(food)
        for food_type in self.cost:
            ## We look at any after
            if food_type == Food.ANY:
                continue
            remaining_food.cost[food_type] -= self.cost[food_type]
        ## Now we can just see if the negatives, times two
        any_missing = self.cost[Food.ANY]
        any_missing += sum([abs(x)*2 for x in remaining_food.cost.values() if x < 0])
        available_food = sum([x for x in remaining_food.cost.values() if x > 0])
        return available_food > any_missing


    def __str__(self):
        ret = [f"{food} : {self.cost[food]}" for food in self.cost if self.cost[food] > 0]
        ## TODO Replace this with an opposite to split!
        x = ""
        for r in ret:
            x += r
        return x