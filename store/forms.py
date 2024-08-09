from django import forms
from store.models.wishlist import Wishlist
from store.models.review import Review

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['product']
        widgets = {
            'product': forms.HiddenInput()
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'message']
