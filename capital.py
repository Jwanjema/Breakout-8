def capital(capitals):
    sentences = []
    for loc in capitals:
        for key in loc:
            if key != 'capital':
               sentences.append(f"The capital of {loc[key]} is {loc['capital']}")
    return sentences 
