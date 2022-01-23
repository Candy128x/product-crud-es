from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer
from products.models import ProductDetails

# product_details_index = Index('product_details')
# product_details_index.settings(number_of_shards=1, number_of_replicas=1)
# html_strip = analyzer('html_strip', tokenizer="standard", filter=["standard", "lowercase", "stop", "snowball"], char_filter=["html_strip"])


# @product_details_index.doc_type
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
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    # settings = {
    #     'number_of_shards': 1,
    #     'number_of_replicas': 0
    # }

    class Django:
        model = ProductDetails
        fields = ['name', 'price', 'quantity']