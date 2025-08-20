from collections import Counter

def recommend_products(user_history, product_catalog):
    """
    Recommends products based on user history, provides explanations, and user feedback options.

    Args:
        user_history (list): List of product IDs the user has interacted with.
        product_catalog (dict): Dictionary of product_id: product_info.

    Returns:
        list: List of recommendation dicts with explanation and feedback options.
    """
    # Simple content-based filtering: recommend products similar to those in user_history
    # For demonstration, assume product_info has 'category' field

    # Gather categories from user history
    categories = [product_catalog[pid]['category'] for pid in user_history if pid in product_catalog]
    if not categories:
        return []

    # Find most common category
    most_common_category = Counter(categories).most_common(1)[0][0]

    # Recommend products from the most common category not already in user_history
    recommendations = []
    for pid, info in product_catalog.items():
        if info['category'] == most_common_category and pid not in user_history:
            explanation = f"Recommended because you viewed products in the '{most_common_category}' category."
            feedback_options = ["👍 Like", "👎 Dislike", "Not relevant"]
            recommendations.append({
                'product_id': pid,
                'product_info': info,
                'explanation': explanation,
                'feedback_options': feedback_options
            })

    return recommendations

# Example usage:
if __name__ == "__main__":
    user_history = [1, 2]
    product_catalog = {
        1: {'name': 'Red Shirt', 'category': 'Clothing'},
        2: {'name': 'Blue Jeans', 'category': 'Clothing'},
        3: {'name': 'Sneakers', 'category': 'Footwear'},
        4: {'name': 'Green T-Shirt', 'category': 'Clothing'},
        5: {'name': 'Sandals', 'category': 'Footwear'}
    }
    recs = recommend_products(user_history, product_catalog)
    for rec in recs:
        print(f"Product: {rec['product_info']['name']}")
        print(f"Explanation: {rec['explanation']}")
        print(f"Feedback options: {rec['feedback_options']}\n")