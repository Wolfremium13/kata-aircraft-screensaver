# 📔 Here you can see the list of changes made in the kata

## ♻️ changed create as a factory method of the class

- Reason: seems weird to use the constructor of Aircraft class outside of the class definition importing the module itself to use it instead. So I moved the constructor as a static method inside the class definition to keep the same imports structure across the project.

## ♻️ simplify direction change

- Reason: the change direction logic was changing the direction of the aircraft class if a new direction was specified on the move method. We're mutating the direction of the class and then overriding the direction parameter of the method, this doesn't make sense, so we just modify the direction of the class and then we use it.

## ♻️ put aircraft variables as private

- Reason: the aircraft variables should not expose all the variables from the start, so I moved to private variables instead.

## ♻️ use is_empty method

- Reason: the assert method is comparing the length of the list see if it empty or not, so I used the `is_empty()` assert method to improve legibility.
