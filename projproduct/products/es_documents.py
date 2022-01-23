from django_elasticsearch_dsl import (Document,fields,Index,)
from django_elasticsearch_dsl.registries import registry
from products.models import ProductDetails

# product_details_index = Index('product_details')
# product_details_index.settings(number_of_shard=1, number_of_replicas=0)


# @product_details_index.Document
@registry.register_document
class ProductDetailsDocument(Document):

    # name = fields.TextField(attr='name', fields={'suggest': fields.Completion()})
    # price = fields.IntegerField()
    # quantity = fields.IntegerField()

    # class Meta:
    #     model = ProductDetails
    #     fields = ['id', 'name', 'price', 'quantity']

    class Index:
        name = 'product_details'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    class Django:
        model = ProductDetails
        fields = ['id', 'name', 'price', 'quantity']