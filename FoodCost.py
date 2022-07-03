from typing import List

from Types import FoodTypes

class FoodCost:
    """
    Describes a comparable class of a food cost. 
    """
    def __init__(self, cost: List[FoodTypes]=[]):
        self.cost = {
            FoodTypes.ANY: 0,
            FoodTypes.INVETEBRATE: 0, 
            FoodTypes.GRAIN : 0,
            FoodTypes.FISH : 0,
            FoodTypes.RODENT : 0,
            FoodTypes.FRUIT : 0
        }
        for food_type in cost:
            self.cost[food_type] += 1

    def within_budget(self, food: List[FoodTypes]=[]):
        """
        Checks if a list of foods can afford this foodcost.
        """
        available_food = FoodCost(food)
        ## Lets just count down from our food stores any matching food initially
        remaining_food = FoodCost(food)
        for food_type in self.cost:
            ## We look at any after
            if food_type == FoodTypes.ANY:
                continue
            remaining_food.cost[food_type] -= self.cost[food_type]
        ## Now we can just see if the negatives, times two
        any_missing = self.cost[FoodTypes.ANY]
        any_missing += sum([abs(x)*2 for x in remaining_food.cost.values() if x < 0])
        available_food = sum([x for x in remaining_food.cost.values() if x > 0])
        return available_food >= any_missing

    def __str__(self):
        return f"{self.cost}"