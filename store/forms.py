from django import forms
from store.models.wishlist import Wishlist

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['product']
        widgets = {
            'product': forms.HiddenInput()
        }
