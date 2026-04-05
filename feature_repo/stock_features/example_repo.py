from feast import Entity
from feast import FeatureView
from feast import Field
from feast.types import Float32
from feast.types import Int64
from feast import FileSource

stock = Entity(
    name="stock_name",
    join_keys=["stock_name"]
)

source = FileSource(
    path="../../data/merged",
    timestamp_field="timestamp"
)

stock_features = FeatureView(

    name="stock_features",

    entities=["stock_name"],

    ttl=None,

    schema=[
        Field(name="rolling_avg_10",dtype=Float32),
        Field(name="volume_sum_10",dtype=Float32),
        Field(name="target",dtype=Int64)
    ],

    online=False,

    source=source
)
