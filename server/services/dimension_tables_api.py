from server.models.dim_olist_products import DimOlistProducts
from server.models.dim_olist_sellers import DimOlistSellers
from server.models.dim_product_category_name_translation import DimProductCategoryNameTranslation


class DimensionTables():
    def __init__(self):
        self.dimension_tables_mapping = {
            "product_category_name_translation":DimProductCategoryNameTranslation,
            'olist_sellers':DimOlistSellers,
            'olist_products': DimOlistProducts,
            'olist_orders':DimOlistOrders,#'tb_dim_olist_orders_dataset',
            'olist_order_reviews':DimOlistOrderReviews,#'tb_dim_olist_order_reviews',
            'olist_order_payments': DimOlistOrderPayments,#'tb_dim_olist_order_payments_dataset'
            'olist_order_items':DimOlistOrderItems,
            'olist_geolocation':DimOlistGeolocation,
            'olist_customers_dataset':DimOlistCustomers
        }

    def populate_dimension_tables(self):
        pass
