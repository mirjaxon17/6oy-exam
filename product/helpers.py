import uuid
from django.db.models import TextChoices


class SaveMediaFiles(object):
    def type_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"product/types/{uuid.uuid4()}.{image_extension}"
    

    def product_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"product/product/{uuid.uuid4()}.{image_extension}"
    
    def bonus_image_path(instance, filename):
        image_extensions = filename.split('.')[-1]
        return f"product/bonus_discount/{uuid.uuid4}.{image_extensions}"
    
    def organic_image_path(instance, filename):
        image_extensions = filename.split('.')[-1]
        return f"product/organic/{uuid.uuid4}.{image_extensions}"
    
    def testiminal_image_path(instance, filename):
        image_extensions = filename.split('.')[-1]
        return f"product/testiminial/{uuid.uuid4}.{image_extensions}"
    
    


class Choises(object):
    class PriceType(TextChoices):
        s = '$', 'USD'
        sum = 'UZS', "so'm"