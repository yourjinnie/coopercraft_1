from django.db import models
# from store.models.products import Product
# from store.models.sign_up import SignUp



class Order(models.Model):
    # customer=models.ForeignKey(SignUp,on_delete=models.CASCADE)
    # product=models.ForeignKey(Product,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    phone_no = models.IntegerField()
    status = models.BooleanField(default=False)

    def place_order(self):
        self.save()

    @staticmethod
    def get_order_by_customer(user_id):
        return Order \
            .objects \
            .filter(customer=user_id) \
            .order_by('-date')