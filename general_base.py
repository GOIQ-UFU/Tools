def general_base(dimensions):
    dic_psis = {}
    ranges = [ range(d) for d in dimensions] # ex.:  [0, 1]  [0, 1]  [0, 1]  [0, 1]  [0, 5]  [0, 5]
    for index in product(* ranges): # product with all combinations
        key =  ''.join(str(j) for j in index) # names criation
        psi = tensor(*[basis(d, j) for d, j in zip(dimensions, index)]) # vector for each combination
        dic_psis[key] = psi

    return dic_psis
