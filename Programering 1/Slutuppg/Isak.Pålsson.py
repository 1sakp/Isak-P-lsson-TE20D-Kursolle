import random as rd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#refrencess
#   https://matplotlib.org/stable/api/animation_api.html
#   https://stackoverflow.com/questions/44594887/how-to-update-plot-title-with-matplotlib-using-animation
#   https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
#   https://realpython.com/introduction-to-python-generators/
#   https://matplotlib.org/stable/api/axis_api.html


#generator swaper: swapps
def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]

#generator that yields the changed list after
#   https://realpython.com/introduction-to-python-generators/

#Bubble sort just swaps bigger to higher place in list if the one occupying that space is smaler.
def bubblesort(_list_):
    if len(_list_) == 1:
        return
    swapped = True
    for i in range(len(_list_) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(_list_) - 1 - i):
            if _list_[j] > _list_[j + 1]:
                swap(_list_, j, j + 1)
                swapped = True
            yield _list_

#Insertion sort goes from left to right while checking if the one behind itself is smaler or larger if it's smaler
#it will swap places and check again.
def insertionsort(_list_):
    for i in range(1, len(_list_)):
        j = i
        while j > 0 and _list_[j] < _list_[j - 1]:
            swap(_list_, j, j - 1)
            j -= 1
            yield _list_

#   https://www.geeksforgeeks.org/python-program-for-selection-sort/
#switches places with the corect one for it's current place.
def selectionsort(_list_):
    if len(_list_) == 1:
        return
    for i in range(len(_list_)):
        minVal = _list_[i]
        minIdx = i
        for j in range(i, len(_list_)):
            if _list_[j] < minVal:
                minVal = _list_[j]
                minIdx = j
            yield _list_
        swap(_list_, i, minIdx)
        yield _list_

# in if __name__ == "__main__" means that it won't be wrongfully triggred and will trigger on it's own (future proofing)
if __name__ == "__main__":
    def input_func():
        global number
        try:
            number = int(input("Enter number of integers: "))
        except ValueError:
            input_func()
        
    input_func()
    
    #defines and shuffles list
    _list_ = [x + 1 for x in range(number)]
    rd.shuffle(_list_)

    #generators chooser
    #uses true or false instead of try exept
    #   https://realpython.com/introduction-to-python-generators/
    chooser = True
    while chooser == True:
        choise = input("Bubble or insert or selection:   ")
        if "bubble" in choise.lower():
            generator = bubblesort(_list_)
            chooser = False
        elif "insert" in choise.lower():
            generator = insertionsort(_list_)
            chooser = False
        elif "selection" in choise.lower():
            generator = selectionsort(_list_)
            chooser = False

    #figure and axis.
    #   https://matplotlib.org/stable/api/axis_api.html
    fig, ax = plt.subplots()
    ax.set_title("bar")

    #start bar plot.
    #   https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
    bar_rectangle = ax.bar(range(len(_list_)), _list_, align="edge")

    #limit's
    ax.set_xlim(0, number)
    ax.set_ylim(0, int(1.07 * number))

    #text
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    #Define update by ticking the rectangle in zip with limit of val
    tick = [0]
    def update_fig(_list_, rectangle, tick):
        for rect, val in zip(rectangle, _list_):
            rect.set_height(val)
        tick[0] += 1
        
    #animation generating frames from the generator and changes 
    #   https://stackoverflow.com/questions/44594887/how-to-update-plot-title-with-matplotlib-using-animation
    #   https://matplotlib.org/stable/api/animation_api.html
    anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rectangle, tick), frames=generator, interval=1, repeat=False)
    plt.show()
    
    
#it's possible to count how much time and how manny itterations it loops through but i don't have time for that nor the knowhow
#