with source as (
    select
        "Date",
        "Close",
        simbolo
    from 
        {{ source('dbsales_fz80', 'commodities') }}
),
-- Renomeando e mudando tipo
renamed as (
    select
        cast("Date" as date) as data,
        "Close" as valor_fechamento,
        simbolo
    from source
)

select
    data,
    valor_fechamento,
    simbolo
from renamed
