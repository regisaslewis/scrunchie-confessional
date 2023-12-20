import React from "react";
import { NavLink } from "react-router-dom";

function OneReview({reviewItem, user, setReview, handleReviewDelete}) {

    const { product, rating, comment} = reviewItem
    const starCount = "⭐".repeat(rating)

    return (
        <div id="review">
            <h2>{reviewItem.user.username} on {product.name}</h2>
            <p>{comment}</p>
            <h3>{rating}/5 {starCount}</h3>
            {user.id === reviewItem.user_id ?
            <div>
                <NavLink to="/editreviewform">
                    <button onClick={() => setReview(reviewItem)}>Edit Review</button>
                </NavLink>
                <NavLink to="/">
                    <button onClick={() => handleReviewDelete(reviewItem.id)}>Delete Review</button>
                </NavLink>
            </div>:
            ""
            }
        </div>
    );
}

export default OneReview;