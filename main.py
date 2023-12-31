def linear_search_product(product_list, target_product):
    indices = []
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target_product = "Apple"
result = linear_search_product(products, target_product)
if result:
    print(f"{target_product} found at indices: {result}")
else:
    print(f"{target_product} not found in the list.")
