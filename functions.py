def generate_personalized_recommendation(user_id, cursor):
    cursor.execute("SELECT product_name FROM user_recommendations WHERE user_id = ?", (user_id,))
    feedbacks = cursor.fetchall()
    
    if not feedbacks:
        return f"No recommendations available for User {user_id}."
    
    recommendations = []
    for product_name, in feedbacks:
        recommendation_text = f"Since you liked {product_name}, we recommend similar products."
        recommendations.append(recommendation_text)
    
    return " ".join(recommendations)







