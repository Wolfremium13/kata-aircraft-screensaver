# 📔 Here you can see the list of changes made in the kata

## ♻️ changed create as a factory method of the class

- Reason: seems weird to use the constructor of Aircraft class outside of the class definition importing the module itself to use it instead. So I moved the constructor as a static method inside the class definition to keep the same imports structure across the project.

## ♻️ simplify direction change

- Reason: the change direction logic was changing the direction of the aircraft class if a new direction was specified on the move method. We're mutating the direction of the class and then overriding the direction parameter of the method, this doesn't make sense, so we just modify the direction of the class and then we use it.

## ♻️ put aircraft variables as private

- Reason: the aircraft variables should not expose all the variables from the start, so I moved to private variables instead.

## ♻️ use is_empty method

- Reason: the assert method is comparing the length of the list see if it empty or not, so I used the `is_empty()` assert method to improve legibility.

## ♻️ move all bouncing test inside another class

- Reason: all the test are mixing concepts on `TestAircraft` so as first refactor I moved outside the test related with bouncing in order to improve legibility.

## ❌ added movement tests based on direction

- Reason: it's not clear to me that the movement behavior doesn't overlap the bounce behavior so I created a new class and a bunch of test that doesn't move on the limits of the territory. I saw that the code it's prepared for bounce but not for a normal movement on a direction different of `NorthEast`.

## ♻️ simplify the match pattern

- Reason: the match pattern could generate a cognitive charge and it's difficult to simplify later. I choose `dict` instead in order to make legible the movement for this context.

## ♻️ change movement from properties to methods

- Reason: In this case, methods are a good choice because each one returns a new position based on the current position, and there is no single "next position" that can be represented as a property. Additionally, methods involve a calculation or processing that is performed to obtain the new position, which is consistent with the idea of a method. On the other hand, if it were necessary to access the next position frequently, then a property could be a better option. A property is a faster and more direct way to obtain information that does not require any additional calculation. In summary, in this particular case, methods seem to be an appropriate option as they represent operations that are performed on the current position and return a new position based on that operation.

## ♻️ simplify ternary operator using opposite on direction

- Reason: Due to the boolean complexity in the kata, I have shifted all the ternary operators related to movement based on direction to the "Direction" class, making the first method easier to understand.
