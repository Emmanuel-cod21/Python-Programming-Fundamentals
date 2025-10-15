# Emmanuel Uzoma
# 2/19/2025 
# Professor Evaluation Report using OOP
# This program defines a Rating class to represent a professor's evaluation ratings.
# It creates 3 Rating objects, stores them in a list, and displays each professor's 
# ratings and average. It then finds and displays the professor with the highest
# average rating.

class Rating:
    def __init__(self, name, easy, helpful, clear):
        self.__name = name
        self.__easy = easy
        self.__helpful = helpful
        self.__clear = clear
    
    def get_name(self):
        return self.__name

    def get_easy(self):
        return self.__easy
    
    def get_helpful(self):
        return self.__helpful
    
    def get_clear(self):
        return self.__clear
    
    def set_name(self, name):
        self.__name = name

    def set_easy(self, easy):
        self.__easy = easy

    def set_helpful(self, helpful):
        self.__helpful = helpful

    def set_clear(self, clear):
        self.__clear = clear

    def calcAvgRating(self):
        return (self.__easy + self.__helpful + self.__clear) / 3


def displayRating(rateList):
    print(f"{'Professor Name':15} {'Easy':8} {'Helpful':8} {'Clear':8} {'Average':8}")
    for rating in rateList:
        print(f"{rating.get_name():15} {rating.get_easy():8} {rating.get_helpful():8} "
              f"{rating.get_clear():8} {rating.calcAvgRating():8.2f}")

def findHiIndex(rateList):
    hiIndex = 0
    hiAvg = 0
    for i in range(len(rateList)):
        avg = rateList[i].calcAvgRating()
        if avg > hiAvg:
            hiAvg = avg 
            hiIndex = i
    return hiIndex

def displayHiRating(rateList, hiIndex):
    hiRating = rateList[hiIndex]
    print(f"\nHighest Average Rating:")
    print(f"Professor {hiRating.get_name()} with rating {hiRating.calcAvgRating():.2f}")

def main():
    rate1 = Rating("Mary", 5, 5, 5)  
    rate2 = Rating("Joe", 4, 5, 3)
    rate3 = Rating("Ria", 4, 4, 5)
    
    rateList = [rate1, rate2, rate3]

    print("Professor Ratings:")
    displayRating(rateList)

    hiIndex = findHiIndex(rateList)
    displayHiRating(rateList, hiIndex)

main()
