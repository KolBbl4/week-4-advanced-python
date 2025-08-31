def generator_sqr(m)->int:
    for i in range(m):
        yield i**2


def main()->None:
    VarSQRT = [x**2 for x in range(5)]
    print(VarSQRT)
    m = 5
    res = generator_sqr(m)
    for _ in range(m):
        print(next(res))
        

if __name__ == "__main__":
    main()