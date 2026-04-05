from feast import Entity
from feast import FeatureView
from feast import Field
from feast.types import Float32
from feast.types import Int64
from feast import FileSource


driver = Entity(
    name="driver_id",
    join_keys=["driver_id"]
)


source = FileSource(
    path="data/driver_stats.parquet",
    timestamp_field="event_timestamp"
)


driver_stats_fv = FeatureView(

    name="driver_stats",

    entities=[driver],

    ttl=None,

    schema=[
        Field(name="conv_rate",dtype=Float32),
        Field(name="acc_rate",dtype=Float32),
        Field(name="avg_daily_trips",dtype=Int64)
    ],

    online=False,

    source=source
)