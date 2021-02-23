def f21(x):
    tree_dictioinary = {
        "terra": 10,
        "lua": {
            "kit": {
                1978: 3,
                1976: {
                    2011: 4,
                    2015: 5,
                    1958: 6
                },
                2015: {
                    2011: 7,
                    2015: 8,
                    1958: 9
                }
            },
            "gosu": {
                1978: 0,
                1976: 1,
                2015: 2,
            }
        }
    }

    result = tree_dictioinary[x[2]]
    if type(result) is not dict:
        return result
    result = result[x[3]]
    if type(result) is not dict:
        return result
    result = result[x[1]]
    if type(result) is not dict:
        return result
    result = result[x[0]]
    if type(result) is not dict:
        return result


print(f21([2011, 1976, "terra", "gosu", "r"]))
print(f21([1958, 1976, "lua", "kit", "swift"]))

