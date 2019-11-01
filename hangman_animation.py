hangman = (
    """

|     
|
|
|
|
|\

"""
    ,
    """

|     
|
|
|
|
|\
---------
"""
    ,
    """
_________
|     
|
|
|
|
|\
---------
"""
    ,
    """
_________
|     |
|
|
|
|
|\
---------
"""
    ,
    """
_________
|     |
|     0
|
|
|
|\
---------
"""
    ,
    """
_________
|     |
|     0
|     |
|
|
|\
---------
"""
    ,
    """
_________
|     |
|     0
|     |
|    |
|
|\
---------
"""
    ,
    """
_________
|     |
|     0
|     |
|    | |
|
|\
---------
"""
    ,
    """
_________
|     |
|     0
|    <|
|    | |
|
|\
---------
"""
    ,
    """
_________
|     |
|     0
|    <|>
|    | |
|
|\
---------
"""
    ,
    """
_________
|     |
|     0
|    <|>
|    | |
|Game Over
|\
---------
"""
)


def display(said):
    if len(said) == 0:
        return 0

    print(hangman[len(said) - 1])
