from django import template

register=template.Library()

@register.filter(name='currency')
def currency(number):
    return "₹"+str(number)
@register.filter(name='multiply')
def multiply(number,number1):
    return number * number1
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
@register.filter(name='offer_percentage')
def offer_percentage(product_price,sale_price):
    if product_price<=0:
        return 0
    discount=product_price-sale_price
    offer_percentage=(discount/product_price)*100
    return round(offer_percentage,2)


