
class FoodList: 

    def food_greater(self, a, b): 
        if self.foods[a] == self.foods[b]: 
            return a < b
        
        return self.foods[a] > self.foods[b]

    def __init__(self):
        self.highest = None
        self.foods = dict()

    def add_food(self, name, rating): 
        self.foods[name] = rating
        if self.highest == None or self.food_greater(name, self.highest): 
            self.highest = name 
    
    def change_rating(self, name, new_rating): 
        self.add_food(name, new_rating)

    def get_highest(self): 
        return self.highest

    
from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):

        self.cuisines = dict()
        self.food_to_cuisine = dict()
        self.food_to_rating = dict()
        self.food_order = {}

        for i, food in enumerate(sorted(foods)): 
            self.food_order[food] = -1 * i

        for name, cuisine, rating in zip(foods, cuisines, ratings):
            if cuisine not in self.cuisines: 
                self.cuisines[cuisine] = SortedSet()
            self.cuisines[cuisine].add((rating, self.food_order[name], name))
            self.food_to_cuisine[name] = cuisine
            self.food_to_rating[name] = rating        

        self.count = 0

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        curr_rating = self.food_to_rating[food]
        food_index = self.food_order[food]

        self.cuisines[cuisine].discard((curr_rating, food_index, food))
        self.food_to_rating[food] = newRating
        self.cuisines[cuisine].add((newRating, food_index, food))


    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][-1][2]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)