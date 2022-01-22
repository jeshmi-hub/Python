def skip_elements(elements):
    
    # Initialize variables
    new_list = []

    # Iterate through the list
                                 # start index:end index: step (slicing)
        # Does this element belong in the resulting list?
        for item in element[::2]:
                if item not in new_list:
                    new_list.append(item)
            # Add this element to the resulting list
            
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be [
