from server.models.dim_olist_customers import DimOlistCustomers
from server.models.dim_olist_geolocation import DimOlistGeolocation
from server.models.dim_olist_order_items import DimOlistOrderItems
from server.models.dim_olist_order_payments import DimOlistOrderPayments
from server.models.dim_olist_order_reviews import DimOlistOrderReviews
from server.models.dim_olist_orders import DimOlistOrders
from server.models.dim_olist_products import DimOlistProducts
from server.models.dim_olist_sellers import DimOlistSellers
from server.models.dim_product_category_name_translation import DimProductCategoryNameTranslation


class DimensionTables():
    def __init__(self):
        self.dimension_tables_mapping = {
            "product_category_name_translation": DimProductCategoryNameTranslation,
            'olist_sellers': DimOlistSellers,
            'olist_products': DimOlistProducts,
            'olist_orders': DimOlistOrders,
            'olist_order_reviews': DimOlistOrderReviews,
            'olist_order_payments': DimOlistOrderPayments,
            'olist_order_items': DimOlistOrderItems,
            'olist_geolocation': DimOlistGeolocation,
            'olist_customers': DimOlistCustomers
        }

    def populate_dimension_tables(self, event):
        pass
